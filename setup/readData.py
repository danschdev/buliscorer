#!/usr/bin/env python3
import sqlite3
from pathlib import Path

script_directory = Path(__file__).resolve().parent.parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

#cursor.execute("""SELECT clubs.name, players.name, players.first_name, players.id FROM players
#               INNER JOIN player_club ON players.id = player_club.player_id
#               INNER JOIN clubs ON player_club.club_id = clubs.id
#""")

#for row in cursor.fetchall():
#    print(row[1]+ " heisst mit Vornamen " + row[2] + ", hat die ID " + str(row[3]) + " und spielt für " + row[0])

cursor.execute("""SELECT home_club.name, away_club.name, match_day, date, match.id, scorer.name, assist.name
               FROM clubs AS home_club
               INNER JOIN matches AS match ON match.home_club_id = home_club.id
               INNER JOIN clubs AS away_club ON match.away_club_id = away_club.id
               INNER JOIN goals AS goal ON goal.match_id = match.id
               INNER JOIN players AS scorer on scorer.id = goal.scorer_id
               LEFT JOIN players AS assist on assist.id = goal.assist_id
               """)

cursor.execute("""SELECT * FROM matches""")

rows = cursor.fetchall()

#print (rows)

#homeClub = row[0]
#awayClub = row[1]
#matchDay = row[2]
#date = row[3]

#print(homeClub + " hat an Spieltag " + str(matchDay) + " " + awayClub + " zu Gast. Datum des Spiels: " + str(date) +".")

for row in rows:
    print (row)

cursor.execute("""SELECT players.name, COUNT(goals.id) FROM goals
               LEFT JOIN players ON goals.scorer_id = players.id""")

rows = cursor.fetchall()

for row in rows:
    print (row)
