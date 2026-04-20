#!/usr/bin/env python3

import requests

url = "https://api.openligadb.de/getmatchdata/bl1/2011/1"

response = requests.get(url)

print(response.json()[0]["team1"]["teamId"])
print(response.json()[0]["team1"]["teamName"])
print(response.json()[0]["team2"]["teamId"])
print(response.json()[0]["team2"]["teamName"])