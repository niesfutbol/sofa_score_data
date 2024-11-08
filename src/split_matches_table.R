library(tidyverse)

LEAGUE_FROM_ID <- list(
  "42"="champions_league",
  "54"="bundesliga",
  "87"="laliga",
  "47"="premierleague"
)
league_name = LEAGUE_FROM_ID[["42"]]
fixtures_path <- glue::glue("/workdir/results/{league_name}/general_league_match.csv")
matches <- read_csv(fixtures_path, show_col_types = FALSE)

matches_id <- matches |>
  select(c(matchId, id_home = home_id, id_away = away_id)) |>
  pivot_longer(!matchId, names_to = "local", values_to = "team_id", names_prefix = "id_") |>
  write_csv(glue::glue("/workdir/results/{league_name}/match_teams_id.csv"))

matches_score <- matches |>
  select(c(matchId, score_home = home_score, score_away = away_score)) |>
  pivot_longer(!matchId, names_to = "local", values_to = "team_score", names_prefix = "score_") |>
  write_csv(glue::glue("/workdir/results/{league_name}/match_score.csv"))

id_teams <- matches |>
  select(c(id = home_id, name = home_name)) |>
  unique() |>
  write_csv(glue::glue("/workdir/results/{league_name}/id_teams.csv"))

match_names <- matches |>
  select(c(matchId, matchName)) |>
  write_csv(glue::glue("/workdir/results/{league_name}/match_names.csv"))