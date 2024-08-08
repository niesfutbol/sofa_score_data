import requests
import json
import pandas as pd
import sofa_score_data as ssd

league = {"copa_america": 44, "eurocopa": 50}
league_name: str = "eurocopa"
league_id = league[league_name]
league_url: str = f"https://www.fotmob.com/api/fixtures?id={league_id}&season=2024"
r = requests.get(league_url)
league_info = r.json()

teams_id = list(set([match["opponent"]["id"] for match in league_info]))

teams_url: str = [f"https://www.fotmob.com/api/teams?id={team_id}" for team_id in teams_id]

squats = [requests.get(team_url).json() for team_url in teams_url]

team_players = {id: squat for (id, squat) in zip(teams_id, squats)}

for k, v in team_players.items():
    output_file: str = f"/workdir/results/{league_name}/team_{k}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(v, f, ensure_ascii=False, indent=4)

team_players_id = {k: ssd.obtain_players_from_squat(v["squad"]) for k, v in team_players.items()}


url_players = [
    f"https://www.fotmob.com/api/playerData?id={player['id']}"
    for squat in team_players_id.values()
    for player in squat
]

players: list = []
for url_player in url_players:
    player: dict = requests.get(url_player).json()
    players.append(ssd.obtain_player_info(player))
    output_file: str = f"/workdir/results/{league_name}/player_{player['id']}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(player, f, ensure_ascii=False, indent=4)

pd.DataFrame(players).to_csv(f"{league_name}_birthdate_players.csv")
