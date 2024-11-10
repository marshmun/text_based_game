import sqlite3
from pathlib import Path

DATABASE_PATH = Path(_file_).parent/"game_data.db"

def connect():
    return sqlite3.connect(DATABASE_PATH)

def create_tables():
    with connect() as conn:
        cursor = conn.cursor()

        cursor.execute