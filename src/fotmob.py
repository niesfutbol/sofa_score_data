import requests
import pandas as pd
import json
from bs4 import BeautifulSoup

match_url = "https://www.fotmob.com/matches/liverpool-vs-crystal-palace/2tmp8g#4193856"
r = requests.get(match_url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
json_fotmob = json.loads(soup.find("script", attrs={"id": "__NEXT_DATA__"}).contents[0])
shotmap = json_fotmob["props"]["pageProps"]["content"]["shotmap"]
xG = pd.DataFrame(shotmap["shots"])
home_team = json_fotmob["props"]["pageProps"]["general"]["homeTeam"]
away_team = json_fotmob["props"]["pageProps"]["general"]["awayTeam"]
home_team_name = home_team["name"].lower().replace(" ", "-")
away_team_name = away_team["name"].lower().replace(" ", "-")
output_path = f"xg_{home_team_name}_vs_{away_team_name}.csv"


def write_team_name(teamId):
    if teamId == home_team["id"]:
        return home_team["name"]
    return away_team["name"]


team_name = [write_team_name(value) for value in list(xG.teamId)]
xG["team_name"] = team_name
xG.to_csv(output_path, index=False)

statistics = json_fotmob["props"]["pageProps"]["content"]["stats"]["Periods"]["All"]["stats"][0][
    "stats"
]
pd.DataFrame(statistics).to_csv("statistics.csv", index=False)
