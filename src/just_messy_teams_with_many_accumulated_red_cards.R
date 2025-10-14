paths_red <- list.files("results", full.name = T, recursive = T, pattern = "^red_cards")
paths_match <- list.files("results", full.name = T, recursive = T, pattern = "^general_league_match")

red_cards <- readr::read_csv(paths_red, show_col_types = FALSE) |>
  dplyr::filter(tarjetas_ultimas_6_semanas > 3) |>
  dplyr::arrange(-tarjetas_ultimas_6_semanas)

matches <- readr::read_csv(paths_match, show_col_types = FALSE) |>
  dplyr::select(home_id, home_name) |>
  dplyr::distinct()

red_cards_with_name <- red_cards |>
  dplyr::left_join(matches, by = c("team" = "home_id")) |>
  dplyr::rename(team_name = home_name) |>
  dplyr::select(team_name, date, tarjetas_ultimas_6_semanas) |>
  readr::write_csv("results/just_messy_teams_with_many_accumulated_red_cards.csv")