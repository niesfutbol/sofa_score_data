import requests
import sofa_score_data as ssd


match_url = "https://www.sofascore.com/club-america-deportivo-toluca-fc/GNsON#id:11911066"

sofa = ssd.Sofascore()

players_and_id = sofa.get_player_ids(match_url)
id_playes = list(players_and_id.values())
salidita = sofa.get_match_shotmap(match_url)
shotmap = salidita.json()["shotmap"]
momento = sofa.match_momentum(match_url)
team_names = sofa.get_team_names(match_url)


def write_team_name(value):
    if value > 0:
        return team_names[0]
    return team_names[1]


team_name = [write_team_name(value) for value in list(momento.value)]
momento["team_name"] = team_name
output_name = f"momentum_{team_names[0].lower().replace(' ','-')}_vs_{team_names[1].lower().replace(' ','-')}.csv"
momento.to_csv(output_name, index=False)
