#!/usr/bin/env python3
import sqlite3
from pathlib import Path

script_directory = Path(__file__).resolve().parent.parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               first_name TEXT);
               """)
cursor.execute("""
               CREATE TABLE IF NOT EXISTS clubs (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL);
               """)
cursor.execute("""
               CREATE TABLE IF NOT EXISTS player_club (id INTEGER PRIMARY KEY AUTOINCREMENT,
               player_id INTEGER NOT NULL,
               club_id INTEGER NOT NULL,
               CONSTRAINT fk_player
               FOREIGN KEY (player_id)
               REFERENCES players(id),
               CONSTRAINT fk_club
               FOREIGN KEY (club_id)
               REFERENCES clubs(id))
               """)
cursor.execute("""
               CREATE TABLE IF NOT EXISTS matches (id INTEGER PRIMARY KEY AUTOINCREMENT,
               home_club_id INTEGER NOT NULL,
               away_club_id INTEGER NOT NULL,
               match_day INTEGER NOT NULL,
               CONSTRAINT fk_home_club
               FOREIGN KEY(home_club_id)
               REFERENCES clubs(id),
               CONSTRAINT fk_away_club
               FOREIGN KEY (away_club_id)
               REFERENCES clubs(id))
               """)

conn.close();