import requests
import pandas as pd
import sofa_score_data as ssd


league_id: int = 42
header: dict = requests.get("http://46.101.91.154:6006/").json()
league_url: str = f"https://www.fotmob.com/api/leagues?id={league_id}&season=2024%2F2025"
r = requests.get(league_url, headers=header)
league_info = r.json()

league: pd.DataFrame = ssd.obtain_table_of_league(league_info)
result_path: str = ssd.RESULTS[league_id]
league.to_csv(f"/workdir/{result_path}/league_table.csv", index=False)
