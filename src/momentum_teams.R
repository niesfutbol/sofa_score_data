library(tidyverse)


momentum_path <- "/workdir/results/serie_a/momentum_home_in_match.csv"
momentum <- read_csv(momentum_path, show_col_types = FALSE)

momentum_team <- momentum |>
  select(c(matchId, momentum_home = momentum_porc)) |>
  mutate(momentum_away = 100 - momentum_home) |>
  pivot_longer(!matchId, names_to = "local", values_to = "momentum", names_prefix = "momentum_")

id_teams <- read_csv("results/serie_a/id_teams.csv", show_col_types = FALSE)
matches_id <- read_csv("results/serie_a/match_teams_id.csv", show_col_types = FALSE)
full_momentum <- matches_id |>
  left_join(momentum_team, by = c("matchId", "local")) |>
  left_join(id_teams, by = c("team_id"="id"))