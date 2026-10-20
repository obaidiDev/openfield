"""SQLite state: jobs, media, OAuth tokens and device codes."""
from __future__ import annotations

import json
import sqlite3
import threading
import time
import uuid

SCHEMA = """
CREATE TABLE IF NOT EXISTS jobs(
  id TEXT PRIMARY KEY,
  job_type TEXT NOT NULL,
  status TEXT NOT NULL,
  params TEXT NOT NULL,
  created_at REAL NOT NULL,
  updated_at REAL NOT NULL,
  credits REAL DEFAULT 0,
  result_url TEXT,
  min_result_url TEXT,
  thumbnail_url TEXT,
  error TEXT
);
CREATE TABLE IF NOT EXISTS media(
  id TEXT PRIMARY KEY,
  type TEXT NOT NULL,
  filename TEXT NOT NULL,
  content_type TEXT,
  status TEXT NOT NULL,
  created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS devices(
  device_code TEXT PRIMARY KEY,
  user_code TEXT,
  client_id TEXT,
  state TEXT NOT NULL,
  approved_ip TEXT,
  created_at REAL NOT NULL,
  expires_at REAL NOT NULL,
  interval REAL DEFAULT 5,
  access_token TEXT,
  refresh_token TEXT
);
CREATE TABLE IF NOT EXISTS tokens(
  access_token TEXT PRIMARY KEY,
  refresh_token TEXT,
  sub TEXT,
  email TEXT,
  id_token TEXT,
  expires_at REAL NOT NULL
);
"""


def new_id() -> str:
    return str(uuid.uuid4())


class Store:
    def __init__(self, data_dir):
        self.db_path = str(data_dir / "openfield.sqlite3")
        self._lock = threading.Lock()
        self._conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self._conn.executescript(SCHEMA)
        self._conn.commit()

    def _execute(self, sql, args=()):
        with self._lock:
            cur = self._conn.execute(sql, args)
            self._conn.commit()
            return cur

    # ---- jobs -------------------------------------------------------------
    def create_job(self, job_type, params):
        job_id = new_id()
        now = time.time()
        self._execute(
            "INSERT INTO jobs(id,job_type,status,params,created_at,updated_at) VALUES(?,?,?,?,?,?)",
            (job_id, job_type, "queued", json.dumps(params), now, now),
        )
        return job_id

    def get_job(self, job_id):
        with self._lock:
            row = self._conn.execute(
                "SELECT id,job_type,status,params,created_at,credits,result_url,"
                "min_result_url,thumbnail_url,error FROM jobs WHERE id=?",
                (job_id,),
            ).fetchone()
        if not row:
            return None
        return {
            "id": row[0],
            "job_type": row[1],
            "status": row[2],
            "params": json.loads(row[3]),
            "created_at": row[4],
            "credits": row[5] or 0.0,
            "result_url": row[6],
            "min_result_url": row[7],
            "thumbnail_url": row[8],
            "error": row[9],
        }

    def update_job(self, job_id, **fields):
        allowed = {"status", "credits", "result_url", "min_result_url", "thumbnail_url", "error"}
        sets = ", ".join(f"{k}=?" for k in fields if k in allowed)
        vals = [fields[k] for k in fields if k in allowed]
        if not sets:
            return
        vals += [time.time(), job_id]
        self._execute(f"UPDATE jobs SET {sets}, updated_at=? WHERE id=?", vals)

    def list_jobs(self, limit=50, offset=0, status=None, jtype=None):
        sql = "SELECT id FROM jobs"
        where = []
        args = []
        if status:
            where.append("status=?")
            args.append(status)
        if jtype:
            where.append("job_type=?")
            args.append(jtype)
        if where:
            sql += " WHERE " + " AND ".join(where)
        sql += " ORDER BY created_at DESC LIMIT ? OFFSET ?"
        args += [limit, offset]
        with self._lock:
            rows = self._conn.execute(sql, args).fetchall()
        return [r[0] for r in rows]

    # ---- media ------------------------------------------------------------
    def create_media(self, media_type, filename, content_type, status="pending"):
        media_id = new_id()
        self._execute(
            "INSERT INTO media(id,type,filename,content_type,status,created_at)"
            " VALUES(?,?,?,?,?,?)",
            (media_id, media_type, filename, content_type, status, time.time()),
        )
        return media_id

    def get_media(self, media_id):
        with self._lock:
            row = self._conn.execute(
                "SELECT id,type,filename,content_type,status FROM media WHERE id=?",
                (media_id,),
            ).fetchone()
        if not row:
            return None
        return {
            "id": row[0],
            "type": row[1],
            "filename": row[2],
            "content_type": row[3],
            "status": row[4],
        }

    def set_media_status(self, media_id, status):
        self._execute("UPDATE media SET status=? WHERE id=?", (status, media_id))

    # ---- OAuth ------------------------------------------------------------
    def create_device(self, client_id, interval=5.0, ttl=600.0):
        device_code = new_id()
        user_code = uuid.uuid4().hex[:8].upper()
        now = time.time()
        self._execute(
            "INSERT INTO devices(device_code,user_code,client_id,state,created_at,expires_at,interval)"
            " VALUES(?,?,?,?,?,?,?)",
            (device_code, user_code, client_id, "pending", now, now + ttl, interval),
        )
        return device_code, user_code

    def get_device(self, device_code):
        with self._lock:
            row = self._conn.execute(
                "SELECT device_code,user_code,state,expires_at,interval,access_token,refresh_token"
                " FROM devices WHERE device_code=?",
                (device_code,),
            ).fetchone()
        if not row:
            return None
        return {
            "device_code": row[0],
            "user_code": row[1],
            "state": row[2],
            "expires_at": row[3],
            "interval": row[4],
            "access_token": row[5],
            "refresh_token": row[6],
        }

    def approve_pending_devices(self, max_age_seconds=0.0):
        with self._lock:
            rows = self._conn.execute(
                "SELECT device_code FROM devices WHERE state='pending'"
            ).fetchall()
        codes = [r[0] for r in rows]
        for code in codes:
            self._execute("UPDATE devices SET state='approved' WHERE device_code=?", (code,))
        return codes

    def issue_tokens(self, device_code, access, refresh, id_token, expires_at):
        self._execute(
            "UPDATE devices SET state='issued', access_token=?, refresh_token=? WHERE device_code=?",
            (access, refresh, device_code),
        )
        self._execute(
            "INSERT OR REPLACE INTO tokens(access_token,refresh_token,sub,email,id_token,expires_at)"
            " VALUES(?,?,?,?,?,?)",
            (access, refresh, "local-user", "local@localhost", id_token, expires_at),
        )

    def get_token(self, access_token):
        with self._lock:
            row = self._conn.execute(
                "SELECT access_token,refresh_token,id_token,expires_at FROM tokens WHERE access_token=?",
                (access_token,),
            ).fetchone()
        if not row:
            return None
        return {"access_token": row[0], "refresh_token": row[1], "id_token": row[2], "expires_at": row[3]}

    def rotate_refresh(self, refresh_token):
        """Find the token row owning a refresh token and delete the old access token."""
        with self._lock:
            row = self._conn.execute(
                "SELECT access_token,refresh_token FROM tokens WHERE refresh_token=?",
                (refresh_token,),
            ).fetchone()
        return {"access_token": row[0], "refresh_token": row[1]} if row else None

    def drop_token(self, access_token):
        self._execute("DELETE FROM tokens WHERE access_token=?", (access_token,))
