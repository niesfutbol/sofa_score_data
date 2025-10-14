`%||%` <- function(x, y) if (is.null(x)) y else x

league_name <- "premierleague"
path_matches <- list.files(glue::glue("results/{league_name}"), pattern = "json$", full.name = TRUE)

datos <- path_matches |> 
  purrr::map(jsonlite::read_json) |> 
  purrr::map_dfr(function(match) {
    match_id <- match$content$matchFacts$matchId
	round <- match$general$matchRound
    tarjetas <- match$content$matchFacts$events$events |> 
      purrr::keep(~ .x$type == "Card")
    
    purrr::map_dfr(tarjetas, ~ tibble::tibble(
      match_id = match_id,
	  round = round,
      minute = .x$time %||% NA,  # Maneja valores NULL
      card = .x$card %||% NA,
      player = .x$player$name %||% NA,
      home = .x$isHome %||% NA
    ))
  })

matches_info <- readr::read_csv(glue::glue("results/{league_name}/general_league_match.csv"), show_col_types = FALSE) |>
  tidyr::separate(matchName, c("match_name", "date"), "_") |>
  dplyr::mutate(date = lubridate::parse_date_time(date, "amdYHM")) |>
  dplyr::select(match_id = matchId, home_team = home_id, away_team = away_id, date)

completed_data <- datos |>
  dplyr::left_join(matches_info, by = "match_id") |>
  dplyr::mutate(team = ifelse(home, home_team, away_team)) |>
  dplyr::select(-home, -home_team, -away_team) |> 
  dplyr::filter(card != "Yellow") |>
  dplyr::group_by(match_id, team) |>
  dplyr::summarize(red_cards = dplyr::n())

cards_by_team <- matches_info |>
  dplyr::select(match_id, date) |>
  dplyr::distinct() |>
  dplyr::right_join(completed_data, by = "match_id") |>
  dplyr::arrange(team, date) |>
  dplyr::group_by(team) |>
  dplyr::mutate(
    tarjetas_ultimas_6_semanas = purrr::map_dbl(
      date, 
      ~ sum(red_cards[dplyr::between(date, .x - lubridate::weeks(5), .x)], na.rm = TRUE)
    )
  ) |>
  dplyr::arrange(-tarjetas_ultimas_6_semanas) |>
  readr::write_csv(glue::glue("results/{league_name}/red_cards_last_6_weeks.csv"))