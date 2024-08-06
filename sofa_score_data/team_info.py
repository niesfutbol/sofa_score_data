from sofa_score_data import Member


def obtain_players_from_squat(squat: "list[dict]") -> "list[dict]":
    s = [
        [obtain_player_info_from_member(member) for member in squat_position["members"]]
        for squat_position in squat
    ]
    return [x for xs in s for x in xs]


def obtain_player_info_from_member(member: dict) -> dict:
    m = Member(**member)
    return m.dict()
