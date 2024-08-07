import requests
import sofa_score_data as ssd

league_url: str = "https://www.fotmob.com/api/fixtures?id=44&season=2024"
r = requests.get(league_url)
league_info = r.json()

teams_id = list(set([match["opponent"]["id"] for match in league_info]))

teams_url: str = [f"https://www.fotmob.com/api/teams?id={team_id}" for team_id in teams_id]

squats = [requests.get(team_url).json()["squad"] for team_url in teams_url]

team_players = {id: squat for (id, squat) in zip(teams_id, squats)}

team_players_id = {k:ssd.obtain_players_from_squat(v) for k, v in team_players.items()}

url_players = [f"https://www.fotmob.com/api/playerData?id={player['id']}" for squat in team_players_id.values() for player in squat]

players = [ssd.obtain_player_info(requests.get(url_player).json()) for url_player in url_players]
