import json
import sofa_score_data as ssd


def load_data_from_leagues() -> dict:
    f = open("/workdir/tests/data/leagues_fotmob.json")
    return json.load(f)


def test_get_matches_url() -> None:
    league_info: dict = load_data_from_leagues()
    match_urls: list = ssd.get_matches_url(league_info)
    assert len(match_urls) == 164, "List len is right"
    assert match_urls[0] == "/matches/queretaro-fc-vs-toluca/lto5f#4384303", "First url is right"
    assert (
        match_urls[1] == "/matches/atletico-de-san-luis-vs-mazatlan-fc/8tzh1yse#4384305"
    ), "Second url is right"


def test_get_matches_id() -> None:
    league_info: dict = load_data_from_leagues()
    match_ids: list = ssd.get_matches_id(league_info)
    assert match_ids[0] == "4384303", "First id is right"
    assert match_ids[5] == "4384301", "Sixth id is right"


def test_get_table() -> None:
    f = open("/workdir/tests/data/league_serie_a_2023-24.json")
    league_info: dict = json.load(f)
    table: "list[dict]" = ssd.get_league_table(league_info)