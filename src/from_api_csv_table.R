data <- jsonlite::fromJSON("league_table_140_2024.json")
tabla <- data$response$league$standings[[1]][[1]] |>
  dplyr::select(1:9) |>
  tidyr::unnest_wider(c(all, team)) |>
  tidyr::unnest_wider(goals) |>
  readr::write_csv("tabla_la_liga_2024.csv")