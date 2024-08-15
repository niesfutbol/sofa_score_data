library(tidyverse)
library(ggplot2)
library(ggridges)

league_name = "bundesliga"
table <- read_csv(glue::glue("results/{league_name}/league_table.csv"), show_col_types = FALSE)
id_teams <- read_csv(glue::glue("results/{league_name}/id_teams.csv"), show_col_types = FALSE) |>
  distinct(id, .keep_all=TRUE)
momentum_distribution_file <- glue::glue("results/{league_name}/momentum_distribution.csv")
momentum_distribution <- read_csv(momentum_distribution_file, show_col_types = FALSE)
momentum_distribution |>
  left_join(id_teams, by=c("team_id"="id")) |>
  left_join(table, by=c("team_id"="id")) |>
  ggplot(aes(x = momentum, y = reorder(name, pts), group = name)) +
  geom_density_ridges(fill = "#00AFBB") +
  theme_classic() +
  xlab("Inclinación del momento") + ylab("")
ggsave("momentum_distribution.png")