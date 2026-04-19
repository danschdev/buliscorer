#!/usr/bin/env python3
import sqlite3
from pathlib import Path

script_directory = Path(__file__).resolve().parent.parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

cursor.execute("""SELECT clubs.name, players.name, players.first_name, players.id FROM players
               INNER JOIN player_club ON players.id = player_club.player_id
               INNER JOIN clubs ON player_club.club_id = clubs.id
""")

for row in cursor.fetchall():
    print(row[1]+ " heisst mit Vornamen " + row[2] + ", hat die ID " + str(row[3]) + " und spielt für " + row[0])