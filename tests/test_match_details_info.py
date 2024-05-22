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
    expected_name: str = "Carlos Orrantia"
    assert obatined[0]["playerName"] == expected_name
    expected_xG: float = 0.3704860
    assert obatined[1]["expectedGoals"] == pytest.approx(expected_xG, 0.1)
    assert obatined[1]["expectedGoalsOnTarget"] == pytest.approx(0.709, 0.1)


def test_get_momentum() -> None:
    match_details: dict = load_data_from_match_details()
    obtained = ssd.get_momentum(match_details)
    expected = 38
    assert obtained[1]["value"] == expected


def test_get_percentage_momentun_by_team() -> None:
    minutes = [1, 2, -3, 4, 5, 6, 7, -2, 4, -8, 9]
    momentum = [_make_minute_momentum(minute) for minute in minutes]
    home_momentum = ssd.get_percentage_momentun_by_team(momentum)
    assert home_momentum == pytest.approx(74.5, 0.01)


def _make_minute_momentum(minute) -> dict:
    return {"value": minute}
