library(tidyverse)
library(ggplot2)
library(ggrepel)
league <- "bundesliga"
table <- read_csv(glue::glue("results/{league}/league_table.csv"), show_col_types = FALSE)
id_teams <- read_csv(glue::glue("results/{league}/id_teams.csv"), show_col_types = FALSE) |>
  distinct(id, .keep_all=TRUE)
momentum_distribution <- read_csv(glue::glue("results/{league}/momentum_distribution.csv"), show_col_types = FALSE)
spread_5 <- momentum_distribution |>
  group_by(team_id) |>
  summarize(iqr=IQR(momentum), quality = quantile(momentum, 0.05)) |>
  left_join(id_teams, by=c("team_id"="id")) |>
  left_join(table, by=c("team_id"="id")) |>
  write_csv(glue::glue("quality_{league}_2024.csv"))
spread_5 |> ggplot(aes(x = iqr, y = quality)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, col="#00AFBB") +
  ylab("Cuantil del 5%") + xlab("Rango intercuartil") +
  theme_classic() +
  geom_text_repel(aes(label = spread_5$name), size = 3.5)
ggsave(glue::glue("spread_distribution_{league}.png"))