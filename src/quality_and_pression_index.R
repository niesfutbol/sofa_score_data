library(tidyverse)

data <- read_csv("tests/data/quality_and_pression_index.csv", show_col_types = FALSE)

full_model <- data |>
  select(-team) |>
  lm(formula = pts ~ .)
forward_model <- step(full_model, direction = "forward", scope = formula(~ .))
backward_model <- step(full_model, direction = "backward")

pca <- data |>
  select(-c(team, team)) |>
  prcomp(center = T, scale.=T)

summary(pca)