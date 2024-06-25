import json
import requests
import pandas as pd
import sofa_score_data as ssd


league_id: int = 55
league_url: str = f"https://www.fotmob.com/api/leagues?id={league_id}&ccode3=MEX&season=2023%2F2024"
r = requests.get(league_url)
league_info = r.json()

league: pd.DataFrame = ssd.obtain_table_of_league(league_info)
result_path: str = ssd.RESULTS[league_id]
league.to_csv(f"/workdir/{result_path}/league_table.csv", index=False)
