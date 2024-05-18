import json
import pytest
import sofa_score_data as ssd


def load_data_from_match_details() -> dict:
    f = open("/workdir/tests/data/match_details_fotmob.json")
    return json.load(f)


def test_get_attendance() -> None:
    match_details: dict = load_data_from_match_details()
    obtained = ssd.get_attendance(match_details)
    expected = 65644
    assert obtained == expected, "Obtain the right attendance"


def test_get_top_players() -> None:
    match_details: dict = load_data_from_match_details()
    obatined = ssd.get_top_players(match_details)
    expected = "Diego Valdés"
    assert obatined["name"]["fullName"] == expected


def test_get_all_shots() -> None:
    match_details: dict = load_data_from_match_details()
    obatined = ssd.get_all_shots(match_details)
    expected = "Carlos Orrantia"
    assert obatined[0]["playerName"] == expected
    expected = 0.3704860
    assert obatined[1]["expectedGoals"] == pytest.approx(expected, 0.1)
    assert obatined[1]["expectedGoalsOnTarget"] == pytest.approx(0.709, 0.1)
