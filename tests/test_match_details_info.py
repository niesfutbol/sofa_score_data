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
    shot: ssd.Shots = ssd.Shots(**obatined[0])
    assert shot.playerName == expected_name
    expected_xG: float = 0.0358349
    assert shot.expectedGoals == pytest.approx(expected_xG, 0.1)
    shot_1: ssd.Shots = ssd.Shots(**obatined[1])
    assert shot_1.expectedGoalsOnTarget == pytest.approx(0.709, 0.1)
    assert shot.eventType == "AttemptSaved"
    assert shot.teamId == 6618
    assert shot.playerId == 201110
    assert shot.x == pytest.approx(87.96323529, 0.1)
    assert shot.y == pytest.approx(18.043821658, 0.1)
    assert shot.min == 5


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


def test_get_match_general_info() -> None:
    match_details: dict = load_data_from_match_details()
    _: ssd.Matches = ssd.get_match_general_info(match_details)
