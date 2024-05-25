from sofa_score_data import Matches


def get_attendance(match_details) -> int:
    return _get_match_facts_from_details(match_details)["infoBox"]["Attendance"]


def get_top_players(match_details) -> dict:
    return _get_match_facts_from_details(match_details)["topPlayers"]["homeTopPlayers"][0]


def get_all_shots(match_details) -> dict:
    return match_details["content"]["shotmap"]["shots"]


def get_momentum(match_details) -> list:
    return _get_match_facts_from_details(match_details)["momentum"]["main"]["data"]


def _get_match_facts_from_details(match_details) -> dict:
    return match_details["content"]["matchFacts"]


def get_match_percentage_momentun():
    pass


def get_percentage_momentun_by_team(momentum):
    home = sum([minute["value"] for minute in momentum if minute["value"] > 0])
    away = sum([minute["value"] for minute in momentum if minute["value"] < 0])
    return 100 * home / (home + abs(away))


def get_match_general_info(match_details) -> Matches:
    return Matches(**match_details["general"])
