def get_matches_url(league_info: dict) -> list:
    return [match["pageUrl"] for match in league_info["matches"]["allMatches"]]
