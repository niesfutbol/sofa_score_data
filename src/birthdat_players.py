import requests

league_url: str = f"https://www.fotmob.com/api/fixtures?id=44&season=2024"
r = requests.get(league_url)
league_info = r.json()

teams_id = list(set([match["opponent"]["id"] for match in league_info]))

teams_url: str = [f"https://www.fotmob.com/api/teams?id={team_id}" for team_id in teams_id]

squats = [requests.get(team_url).json()["squad"] for team_url in teams_url]

player_url = "https://www.fotmob.com/api/playerData?id=141762"

player_info = requests.get(player_url).json()
