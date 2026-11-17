import sqlite3
import hashlib
import hmac
import secrets

from contextlib import closing

import database


# ==========================================
# SPRINT 4 - USER AUTHENTICATION
# ==========================================


# Create users table
def create_users_table():

    with closing(sqlite3.connect(database.DATABASE_NAME)) as connection:
        with connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password_hash BLOB NOT NULL,
                    salt BLOB NOT NULL
                )
            """)


# ==========================================
# REGISTER USER
# ==========================================

def register_user(username, password):

    # Validate username
    if not isinstance(username, str) or not username.strip():
        return False

    # Validate password
    if not isinstance(password, str) or len(password) < 12:
        return False

    username = username.strip()

    # Generate random salt
    salt = secrets.token_bytes(16)

    # Hash password securely
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600000
    )

    create_users_table()

    try:
        with closing(sqlite3.connect(database.DATABASE_NAME)) as connection:
            with connection:
                connection.execute("""
                    INSERT INTO users (username, password_hash, salt)
                    VALUES (?, ?, ?)
                """, (username, password_hash, salt))

        return True

    except sqlite3.IntegrityError:
        return False


# ==========================================
# AUTHENTICATE USER
# ==========================================

def authenticate_user(username, password):

    # Validate input types
    if not isinstance(username, str) or not isinstance(password, str):
        return False

    create_users_table()

    # Retrieve stored password hash
    with closing(sqlite3.connect(database.DATABASE_NAME)) as connection:

        cursor = connection.execute("""
            SELECT password_hash, salt
            FROM users
            WHERE username = ?
        """, (username.strip(),))

        user = cursor.fetchone()

    # Reject unknown username
    if user is None:
        return False

    stored_hash, salt = user

    # Hash entered password
    entered_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600000
    )

    # Compare password hashes securely
    return hmac.compare_digest(stored_hash, entered_hash)