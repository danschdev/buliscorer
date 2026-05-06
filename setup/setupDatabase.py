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
               CREATE TABLE IF NOT EXISTS player_club (
               player_id INTEGER NOT NULL,
               club_id INTEGER NOT NULL,
               PRIMARY KEY (player_id, club_id),
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
               date DATETIME NOT NULL,
               CONSTRAINT fk_home_club
               FOREIGN KEY(home_club_id)
               REFERENCES clubs(id),
               CONSTRAINT fk_away_club
               FOREIGN KEY (away_club_id)
               REFERENCES clubs(id))
               """)
cursor.execute("""
               CREATE TABLE IF NOT EXISTS goals (id INTEGER PRIMARY KEY AUTOINCREMENT,
               match_id INTEGER NOT NULL,
               scorer_id INTEGER NOT NULL,
               assist_id INTEGER DEFAUL NULL,
               is_own_goal BOOLEAN DEFAULT 0,
               is_penalty BOOLEAN DEFAULT 0)
               """)
cursor.execute("""
               CREATE VIEW v_player_club AS 
               SELECT players.id AS pid, players.name as pname, clubs.id AS cid, clubs.name AS cname
               FROM players
               INNER JOIN player_club ON players.id = player_club.player_id
               INNER JOIN clubs ON player_club.club_id = clubs.id
               """)
conn.close()
