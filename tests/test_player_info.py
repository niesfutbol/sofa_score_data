import sofa_score_data as ssd


def test_obtain_player_info() -> None:
    expected: dict = {"id": 6461434917, "name": "Nepo Rojas", "birthDate": "1985-01-31"}
    data_raw: dict = {
        "id": 6461434917,
        "name": "Nepo Rojas",
        "birthDate": {"utcTime": "1985-01-31T00:00:00.000Z"},
    }
    obtained: dict = ssd.obtain_player_info(data_raw)
    assert obtained == expected
