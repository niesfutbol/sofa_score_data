library(tidyverse)
library(comprehenr)


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

calculate_mean_momentum <- function(momentum, team) {
  momentum |>
    filter(team_id == team) %>%
    .$momentum |>
    sample(replace = TRUE) |>
    mean()
}

momentum_distribution <- tibble::tibble()
just_id_teams <- id_teams$id |> unique()
for (id_t in just_id_teams) {
  boots_mean_momentum <- comprehenr::to_vec(for(i in 1:2000) calculate_mean_momentum(full_momentum, id_t))
  momentum_distribution <- rbind(
    momentum_distribution,
    tibble::tibble("team_id"=id_t, "momentum" = boots_mean_momentum)
    )
  print(id_t)
}
momentum_distribution |>
  write_csv("results/serie_a/momentum_distribution.csv")