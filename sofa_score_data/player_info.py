from sofa_score_data import Player


def obtain_player_info(player_info: dict) -> dict:
    player: Player = Player(**player_info)
    birthDate: str = _extract_birthDate(player.birthDate)
    return {"id": player.id, "name": player.name, "birthDate": birthDate}


def _extract_birthDate(birthDate: dict) -> str:
    return birthDate["utcTime"].split("T")[0]
