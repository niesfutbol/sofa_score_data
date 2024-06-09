library(tidyverse)

shots <- read_csv("/workdir/results/serie_a/shots_match.csv", show_col_types = FALSE)

combination_key <- c("playerName", "teamId", "playerId")
all_players <- shots |>
  select(c(2, 6, 7)) |>
  unique()

players_teams <- tibble::rowid_to_column(all_players, "index") |>
  write_csv("/workdir/results/player_team.csv")

cleaned_shots <- players_teams |>
  left_join(shots, combination_key) |>
  select(-combination_key) |>
  write_csv("/workdir/results/cleaned_shots.csv")