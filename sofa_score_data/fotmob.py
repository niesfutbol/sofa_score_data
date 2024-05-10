def get_matches_url(league_info: dict) -> list:
    return [match["pageUrl"] for match in league_info["matches"]["allMatches"]]


def get_matches_id(league_info: dict) -> list:
    return [match["id"] for match in league_info["matches"]["allMatches"]]
