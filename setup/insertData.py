#!/usr/bin/env python3
import sqlite3
from pathlib import Path

script_directory = Path(__file__).resolve().parent.parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

cursor.execute("""INSERT INTO players (name, first_name)
               VALUES ("Kane","Harry"),
               ("Olise","Michael"),
               ("Gnabry","Serge"),
               ("Luis Diaz",NULL),
               ("Min-Jae Kim",NULL)
               ;""")
cursor.execute("""INSERT INTO clubs (name)
               VALUES ("FC Bayern München"),
               ("RB Leipzig");
               """)
cursor.execute("""INSERT INTO player_club (player_id, club_id)
               VALUES (1,1),
               (2,1);
               """)
cursor.execute("""INSERT INTO matches (home_club_id, away_club_id, match_day, date)
               VALUES(1,2,1,"2025-08-01T20:30:00Z");
               """)
cursor.execute("""INSERT INTO goals (match_id, scorer_id, assist_id)
               VALUES (1,1,NULL),
               (1,4,3),
               (1,2,3),
               (1,1,4),
               (1,1,4),
               (1,1,5);
               """)
conn.commit()