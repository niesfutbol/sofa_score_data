from sofa_score_data import Row_Table


def get_matches_url(league_info: dict) -> list:
    return _get_matches_variable(league_info, variable="pageUrl")


def get_matches_id(league_info: dict) -> list:
    return _get_matches_variable(league_info, variable="id")


def _get_matches_variable(league_info: dict, variable: str) -> list:
    all_matches = _get_all_matches_info(league_info)
    return [match[variable] for match in all_matches]


def _get_all_matches_info(league_info) -> list:
    return [match for match in league_info["matches"]["allMatches"]]


def get_league_table(league_info: dict) -> "list[Row_Table]":
    table_rows: "list[dict]" = league_info["table"][0]["data"]["table"]["all"]
    return [Row_Table(**row) for row in table_rows]
