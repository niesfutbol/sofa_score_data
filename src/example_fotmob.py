import json
import requests
import sofa_score_data as ssd

league_name: str = "champions_league"
league: dict = {
    "champions_league": 42,
    "copa_america": 44,
    "eurocopa": 50,
    "bundesliga": 54,
    "laliga": 87,
    "premierleague": 47,
}
header: dict = requests.get("http://46.101.91.154:6006/").json()
league_id: int = league[league_name]
league_url: str = f"https://www.fotmob.com/api/leagues?id={league_id}&season=2024%2F2025"
r = requests.get(league_url, headers=header)
league_info = r.json()
match_id: list = ssd.get_matches_id(league_info)
last_five_matches = [
    requests.get(f"https://www.fotmob.com/api/matchDetails?matchId={id_m}", headers=header).json()
    for id_m in match_id[:72]
]
xG = [shot["expectedGoals"] for shot in ssd.get_all_shots(last_five_matches[3])]
result_path: str = ssd.RESULTS[league_id]
for match in last_five_matches:
    match_general_info: ssd.Matches = ssd.get_match_general_info(match)
    output_path = f"/workdir/{result_path}/match_details_data_{match_general_info.matchId}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(match, f, ensure_ascii=False, indent=4)
