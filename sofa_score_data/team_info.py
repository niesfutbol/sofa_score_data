from sofa_score_data import Member


def obtain_players_from_squat(squat: "list[dict]") -> "list[dict]":
    s_0 = [obtain_player_info_from_member(member) for member in squat[0]["members"]]
    s_1 = [obtain_player_info_from_member(member) for member in squat[1]["members"]]
    s_2 = [obtain_player_info_from_member(member) for member in squat[2]["members"]]
    s_3 = [obtain_player_info_from_member(member) for member in squat[3]["members"]]
    s_4 = [obtain_player_info_from_member(member) for member in squat[4]["members"]]
    _ = [
        [obtain_player_info_from_member(member) for member in squat_position["members"]]
        for squat_position in squat
    ]
    return [*s_0, *s_1, *s_2, *s_3, *s_4]


def obtain_player_info_from_member(member: dict) -> dict:
    m = Member(**member)
    return m.dict()
