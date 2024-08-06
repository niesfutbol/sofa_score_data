from sofa_score_data import Member


def obtain_players_from_squat(squat: "list[dict]") -> "list[dict]":
    s = [
        obtain_player_info_from_member(member)
        for squat_position in squat
        for member in squat_position["members"]
    ]
    return s


def obtain_player_info_from_member(member: dict) -> dict:
    m = Member(**member)
    return m.dict()
