library(tidyverse)


momentum_path <- "/workdir/results/serie_a/momentum_home_in_match.csv"
momentum <- read_csv(momentum_path, show_col_types = FALSE)

momentum_team <- momentum |>
  select(c(matchId, momentum_home = momentum_porc)) |>
  mutate(momentum_away = 100 - momentum_home) |>
  pivot_longer(!matchId, names_to = "local", values_to = "momentum", names_prefix = "momentum_")
