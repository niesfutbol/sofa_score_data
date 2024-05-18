def get_attendance(match_details) -> int:
    return match_details["content"]["matchFacts"]["infoBox"]["Attendance"]


def get_top_players(match_details) -> dict:
    return match_details["content"]["matchFacts"]["topPlayers"]["homeTopPlayers"][0]


def get_all_shots(match_details) -> dict:
    return match_details["content"]["shotmap"]["shots"]


def get_momentum(match_details) -> list:
    return match_details["content"]["matchFacts"]["momentum"]["main"]["data"]
