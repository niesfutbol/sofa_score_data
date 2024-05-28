import json
import requests
import pandas as pd
import sofa_score_data as ssd


league_id: int = 55
league_url: str = f"https://www.fotmob.com/api/leagues?id={league_id}&ccode3=MEX&season=2023%2F2024"
r = requests.get(league_url)
league_info = r.json()
match_id: list = ssd.get_matches_id(league_info)
last_five_matches = [
    requests.get(f"https://www.fotmob.com/api/matchDetails?matchId={id_m}").json()
    for id_m in match_id[0:30]
]

result_path: str = ssd.RESULTS[league_id]
general_info: pd.DataFrame = pd.DataFrame()
for match in last_five_matches:
    match_general_info: ssd.Matches = ssd.get_match_general_info(match)
    input_path = f"/workdir/{result_path}/match_details_data_{match_general_info.matchId}.json"
    with open(input_path) as f:
        d = json.load(f)
    match_general_info: ssd.Matches = ssd.get_match_general_info(d)
    b = {k: [v] for (k,v) in match_general_info.model_dump().items()}
    general_info = pd.concat([general_info, pd.DataFrame(b)])
general_info.to_csv(f"/workdir/{result_path}/general_league_match.csv", index = False)
