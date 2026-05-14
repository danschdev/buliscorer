#!/usr/bin/env python3
import pandas
import sqlite3
from pathlib import Path

script_directory = Path(__file__).resolve().parent.parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)

query = """SELECT players.name AS pname, COUNT(DISTINCT goals.id) AS gcount, GROUP_CONCAT(DISTINCT clubs.name) AS cname FROM goals
               LEFT JOIN players ON goals.scorer_id = players.id
               LEFT JOIN player_club ON players.id = player_club.player_id
               LEFT JOIN clubs ON clubs.id = player_club.club_id
               GROUP BY players.id
               HAVING COUNT(DISTINCT goals.id) >= 10
               ORDER BY COUNT(goals.id) DESC"""

df = pandas.read_sql(query, conn)

for index, row in df.iterrows():
    print(index + 1)  # computer counts from 0, human from 1
    print(row.pname + " " + str(row.gcount) + " " + row.cname)
