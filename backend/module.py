"""
SQL文の実行とトークンが最新のものであるか確認するモジュール
"""

import sqlite3
from contextlib import closing
from typing import Optional

from config import DBInfo


def db(sql, data=None) -> Optional[dict]:
    """SQL送信"""

    rows = []
    with closing(sqlite3.connect(DBInfo.db_path)) as conn:
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute(sql, data)
        rows = c.fetchall()
        conn.commit()

    return dict(rows[0]) if rows else None


def auth_jti(user_id, token_jti) -> bool:
    """古いトークンの使用禁止"""

    sql = "SELECT username, jti FROM authinfo WHERE user_id=?;"
    user = db(sql, [user_id])
    if token_jti == user["jti"]:
        return {"username": user["username"]}

    return False
