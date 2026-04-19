#!/usr/bin/env python3
import sqlite3
from pathlib import Path

script_directory = Path(__file__).resolve().parent.parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

cursor.execute("""INSERT INTO players (name, first_name)
               VALUES ("Kane","Harry"),
               ("Olise","Michael");
               """)
cursor.execute("""INSERT INTO clubs (name)
               VALUES ("FC Bayern München"),
               ("RB Leipzig");
               """)
cursor.execute("""INSERT INTO player_club (player_id, club_id)
               VALUES (1,1),
               (2,1);
               """)
cursor.execute("""INSERT INTO matches (home_club_id, away_club_id, match_day)
               VALUES(1,2,1);
               """)

conn.commit()