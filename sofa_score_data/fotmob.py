def get_matches_url(league_info: dict) -> list:
    all_matches = _get_all_matches_info(league_info)
    return [match["pageUrl"] for match in all_matches]


def get_matches_id(league_info: dict) -> list:
    all_matches = _get_all_matches_info(league_info)
    return [match["id"] for match in all_matches]


def _get_all_matches_info(league_info) -> list:
    return [match for match in league_info["matches"]["allMatches"]]
