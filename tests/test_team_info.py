import sofa_score_data as ssd


squat: "list[dict]" = [
    {"title": "coach", "members": [{"id": 36053, "name": "Thomas Christiansen"}]},
    {
        "title": "keepers",
        "members": [{"id": 206088, "name": "Luis Mejia"}, {"id": 1330683, "name": "Cesar Samudio"}],
    },
    {
        "title": "defenders",
        "members": [
            {"id": 1421394, "name": "Eduardo Anderson"},
            {"id": 501847, "name": "Roderick Miller"},
        ],
    },
    {
        "title": "midfielders",
        "members": [
            {"id": 1087406, "name": "Freddy Gondola"},
            {"id": 727101, "name": "Christian Martinez"},
        ],
    },
    {
        "title": "attackers",
        "members": [
            {"id": 526710, "name": "Edgar Barcenas"},
            {"id": 1054132, "name": "Eduardo Guerrero"},
        ],
    },
]

expected: "list[dict]" = [
    {"id": 36053, "name": "Thomas Christiansen"},
    {"id": 206088, "name": "Luis Mejia"},
    {"id": 1330683, "name": "Cesar Samudio"},
    {"id": 1421394, "name": "Eduardo Anderson"},
    {"id": 501847, "name": "Roderick Miller"},
    {"id": 1087406, "name": "Freddy Gondola"},
    {"id": 727101, "name": "Christian Martinez"},
    {"id": 526710, "name": "Edgar Barcenas"},
    {"id": 1054132, "name": "Eduardo Guerrero"},
]


def test_obtain_players_from_squat() -> None:
    obtained: "list[dict]" = ssd.obtain_players_from_squat()
    assert expected == obtained
