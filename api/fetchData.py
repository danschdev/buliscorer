#!/usr/bin/env python3

import requests
import sqlite3
from pathlib import Path

script_directory = Path(__file__).resolve().parent.parent
db = script_directory / "data" / "database.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()


for spieltag in range (1, 35):
    url = "https://api.openligadb.de/getmatchdata/bl1/2011/" + str(spieltag)

    response = requests.get(url)
    responseData = response.json()

    for spiel in range (0, 9):
        team1Id = responseData[spiel]["team1"]["teamId"]
        team1Name = responseData[spiel]["team1"]["teamName"]
        team2Id = responseData[spiel]["team2"]["teamId"]
        team2Name = responseData[spiel]["team2"]["teamName"]

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
            responseData[spiel]["matchID"],
            team1Id,
            team2Id,
            responseData[spiel]["group"]["groupOrderID"],
            responseData[spiel]["matchDateTime"],
        ]
        cursor.execute(statement, matchData)
        goalData = responseData[spiel]["goals"]
        for goal in goalData:
            statement = (
                "INSERT OR IGNORE INTO goals (id, match_id, scorer_id, is_own_goal, is_penalty)"
                "VALUES (?, ?, ?, ?, ?)"
            )
            cursor.execute(statement,  [
                goal["goalID"],
                responseData[spiel]["matchID"],
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