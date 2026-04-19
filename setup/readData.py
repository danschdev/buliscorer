#!/usr/bin/env python3
import sqlite3
from pathlib import Path

script_directory = Path(__file__).resolve().parent.parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

cursor.execute("SELECT * FROM players")

for row in cursor.fetchall():
    print(row[1]+ " heisst mit Vornamen " + row[2])