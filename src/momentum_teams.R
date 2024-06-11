library(tidyverse)


momentum_path <- "/workdir/results/serie_a/momentum_home_in_match.csv"
momentum <- read_csv(momentum_path, show_col_types = FALSE)

momentum_team <- momentum |>
  select(c(matchId, home_momentum = momentum_porc)) |>
  mutate(away_momentum = 100 - home_momentum) |>
  pivot_longer(!matchId, names_to = "local", values_to = "momentum")
