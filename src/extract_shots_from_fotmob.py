import os
import json
import requests
import pandas as pd
import sofa_score_data as ssd

league_name: str = "bundesliga"
league: dict = {
    "champions_league": 42,
    "copa_america": 44,
    "eurocopa": 50,
    "bundesliga": 54,
    "serie_a": 55,
    "laliga": 87,
    "premierleague": 47,
    "FIFA_club_world_cup": 78,
    "ligue_1": 53,
    "eredivisie": 57,
}
league_id: int = league[league_name]

result_path: str = ssd.RESULTS[league_id]
league_path = f"/workdir/{result_path}"
all_downloaded_files: list = os.listdir(league_path)
id_matches: list = ssd.extract_id_from_filename(all_downloaded_files)

general_info: pd.DataFrame = pd.DataFrame()
shots_players: pd.DataFrame = pd.DataFrame()
for index, id_match in enumerate(id_matches):
    print(f"id_match: {id_match} and index: {index}")
    input_path = f"/workdir/{result_path}/match_details_data_{id_match}.json"
    with open(input_path) as f:
        d = json.load(f)
    match_general_info: ssd.Matches = ssd.get_match_general_info(d)
    b = ssd.transfor_dict_of_scalar_to_list(match_general_info.model_dump())
    general_info = pd.concat([general_info, pd.DataFrame(b)])
    shots = ssd.get_all_shots(d)
    s: "list[dict]" = [
        {"matchId": id_match, **ssd.Shots(**shot).model_dump()}
        for shot in shots
        if not shot["isOwnGoal"]
    ]
    shots_players = pd.concat([shots_players, pd.DataFrame(s)])

general_info.to_csv(f"/workdir/{result_path}/general_league_match.csv", index=False)
shots_players.to_csv(f"/workdir/{result_path}/shots_match.csv", index=False)
