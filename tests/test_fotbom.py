import json
import sofa_score_data as ssd

# Opening JSON fil
def load_data_from_leagues() -> dict:
    f = open("/workdir/tests/data/leagues_fotmob.json")
    return json.load(f)

def test_get_matches_url() -> None:
    league_info: dict = load_data_from_leagues()
    match_urls: list = ssd.get_matches_url()