library(tidyverse)


fixtures_path <- "results/serie_a/general_league_match.csv"
matches <- read_csv(fixtures_path, show_col_types = FALSE)

matches_id <- matches |>
  select(c(matchId, home_id, away_id)) |>
  pivot_longer(!matchId, names_to = "local", values_to = "team_id") |>
  write_csv("results/serie_a/match_teams_id.csv")

matches_score <- matches |>
  select(c(matchId, home_score, away_score)) |>
  pivot_longer(!matchId, names_to = "local", values_to = "team_score") |>
  write_csv("results/serie_a/match_score.csv")

id_teams <- matches |>
  select(c(id = home_id, name = home_name)) |>
  unique() |>
  write_csv("results/serie_a/id_teams.csv")

match_names <- matches |>
  select(c(matchId, matchName)) |>
  write_csv("results/serie_a/match_names.csv")