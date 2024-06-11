import json
import requests
import pandas as pd
import sofa_score_data as ssd


league_id: int = 55
league_url: str = f"https://www.fotmob.com/api/leagues?id={league_id}&ccode3=MEX&season=2023%2F2024"
r = requests.get(league_url)
league_info = r.json()
id_matches: list = ssd.get_matches_id(league_info)

result_path: str = ssd.RESULTS[league_id]
general_info: pd.DataFrame = pd.DataFrame()
shots_players: pd.DataFrame = pd.DataFrame()
momentum_matches: pd.DataFrame = pd.DataFrame()
for id_match in id_matches:
    print(id_match)
    input_path = f"/workdir/{result_path}/match_details_data_{id_match}.json"
    with open(input_path) as f:
        d = json.load(f)
    momentum_tilt_home: ssd.Match_Momentum = ssd.get_match_percentage_momentun(d)
    m = {k: [v] for (k, v) in momentum_tilt_home.model_dump().items()}
    momentum_matches = pd.concat([momentum_matches, pd.DataFrame(m)])
    match_general_info: ssd.Matches = ssd.get_match_general_info(d)
    b = {k: [v] for (k, v) in match_general_info.model_dump().items()}
    general_info = pd.concat([general_info, pd.DataFrame(b)])
    shots = ssd.get_all_shots(d)
    s: "list[dict]" = [{"matchId": id_match, **ssd.Shots(**shot).model_dump()} for shot in shots if not shot["isOwnGoal"]]
    shots_players = pd.concat([shots_players, pd.DataFrame(s)])
    
general_info.to_csv(f"/workdir/{result_path}/general_league_match.csv", index=False)
shots_players.to_csv(f"/workdir/{result_path}/shots_match.csv", index=False)
momentum_matches.to_csv(f"/workdir/{result_path}/momentum_home_in_match.csv", index=False)
