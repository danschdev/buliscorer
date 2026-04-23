#!/usr/bin/env python3

import requests
import sqlite3
from pathlib import Path

script_directory = Path(__file__).resolve().parent.parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

url = "https://api.openligadb.de/getmatchdata/bl1/2011/1"

response = requests.get(url)

for spiel in range (0, 9):
    team1Id = response.json()[spiel]["team1"]["teamId"]
    team1Name = response.json()[spiel]["team1"]["teamName"]
    team2Id = response.json()[spiel]["team2"]["teamId"]
    team2Name = response.json()[spiel]["team2"]["teamName"]

    statement = (
        "INSERT OR IGNORE INTO clubs (id, name) "
        "VALUES (?, ?);"
    )
    data = [
        (team1Id,team1Name),
        (team2Id,team2Name)
    ]

    cursor.executemany(statement,data)

conn.commit()