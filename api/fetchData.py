#!/usr/bin/env python3

import requests
import sqlite3
from pathlib import Path

script_directory = Path(__file__).resolve().parent.parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()


for spieltag in range (1, 34):
    url = "https://api.openligadb.de/getmatchdata/bl1/2011/" + str(spieltag)

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

        statement = (
            "INSERT OR IGNORE INTO matches (id, home_club_id, away_club_id, match_day, date) "
            "VALUES (? ,?, ?, ?, ?)"
        )
        matchData = [
            response.json()[spiel]["matchID"],
            team1Id,
            team2Id,
            response.json()[spiel]["group"]["groupOrderID"],
            response.json()[spiel]["matchDateTime"],
        ]
        cursor.execute(statement, matchData)
        goalData = response.json()[spiel]["goals"]
        for goal in goalData:
            statement = (
                "INSERT OR IGNORE INTO goals (id, match_id, scorer_id, is_own_goal, is_penalty)"
                "VALUES (?, ?, ?, ?, ?)"
            )
            cursor.execute(statement,  [
                goal["goalID"],
                response.json()[spiel]["matchID"],
                goal["goalGetterID"],
                goal["isOwnGoal"],
                goal["isPenalty"]
            ]) 
            playerStatement = (
                "INSERT OR IGNORE INTO players (id, name, first_name)"
                "VALUES (?, ?, ?)"
            )
            cursor.execute(playerStatement, [
                goal["goalGetterID"],
                goal["goalGetterName"],
                None
            ])
conn.commit()