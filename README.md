<a href="https://www.nies.futbol/"><img
src="https://github.com/nepito/world_cup_semis/blob/develop/img/logo.jpeg" align="right" width="256"
/></a>

# Sofascore and Fotmob scraper
[![codecov](https://codecov.io/gh/niesfutbol/sofa_score_data/graph/badge.svg?token=vRIPoR2OZA)](https://codecov.io/gh/niesfutbol/sofa_score_data)

## Step to use

### `id` of different leagues

- Champions League = 42
- Premier League = 47
- Ligue 1 = 53
- Bundesliga = 54
- Serie A = 55
- Eredivisie = 57
- Primeira Liga = 61
- Europa League = 73
- LaLiga = 87
- Liga MX = 230
- [ ] Bélgica = 40
- [ ] Escocia = 64
- [ ] Austria = 38
- Copa América = 44
- Eurocopa = 50


``` python
league = {"copa_america": 44, "eurocopa": 50, "bundesliga" = 54}
```

### Para la inclinación
1. `python src/example_fotmob.py`
1. `python src/write_general_league_match_info.py`
1. `python src/write_table_of_league.py`
1. `Rscript src/split_matches_table.R`
1. `Rscript src/split_table.R`
1. `Rscript src/momentum_teams.R`, needs `comprehenr`
1. `Rscript src/plot_momentum_distribution.R`, needs `ggridges`