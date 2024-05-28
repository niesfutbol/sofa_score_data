from sofa_score_data import Matches, Match_Momentum, Teams


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


def get_match_percentage_momentun(match_details):
    match_info: Matches = get_match_general_info(match_details)
    momentum = get_momentum(match_details)
    mom_per = get_percentage_momentun_by_team(momentum)
    return Match_Momentum(**{**match_info.model_dump(), "momentum_porc": mom_per})


def get_percentage_momentun_by_team(momentum):
    home = sum([minute["value"] for minute in momentum if minute["value"] > 0])
    away = sum([minute["value"] for minute in momentum if minute["value"] < 0])
    return 100 * home / (home + abs(away))


def get_match_general_info(match_details) -> Matches:
    home: Teams = get_match_team_info(match_details, 0)
    away: Teams = get_match_team_info(match_details, 1)
    general_info: dict = {
        **match_details["general"],
        **{f"home_{item}": value for (item, value) in home.model_dump().items()},
        **{f"away_{item}": value for (item, value) in away.model_dump().items()},
    }
    return Matches(**general_info)


def get_match_team_info(match_details, i_team) -> Teams:
    return Teams(**match_details["header"]["teams"][i_team])
