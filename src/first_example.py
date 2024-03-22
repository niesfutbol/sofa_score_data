import requests
import sofa_score_data as ssd


match_url = "https://www.sofascore.com/fulham-tottenham-hotspur/IsT#id:11352604"

sofa = ssd.Sofascore()

players_and_id = sofa.get_player_ids(match_url)
id_playes = list(players_and_id.values())
salidita = sofa.get_match_shotmap(match_url)
shotmap = salidita.json()["shotmap"]
