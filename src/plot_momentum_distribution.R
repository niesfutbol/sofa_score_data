library(tidyverse)
library(ggplot2)
library(ggridges)

id_teams <- read_csv("results/serie_a/id_teams.csv", show_col_types = FALSE)
momentum_distribution <- read_csv("results/serie_a/momentum_distribution.csv", show_col_types = FALSE)
momentum_distribution |>
  left_join(id_teams, by=c("team_id"="id")) |>
  ggplot(aes(x = momentum, y = name, group = name)) +
  geom_density_ridges(fill = "#00AFBB")
ggsave("momentum_distribution.png")