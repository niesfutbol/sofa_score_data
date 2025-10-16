# PREPARACIÓN DE DATOS
library(tidyverse)
library(cluster)
# library(factoextra)
league_name <- "premier"
# 1. Cargar y preparar datos (ejemplo con datos de fútbol)
# Asumiendo que tienes un dataframe con las variables mencionadas
tu_data <- readr::read_csv(glue::glue("tabla_{league_name}_2024.csv"), show_col_types = FALSE) |>
  dplyr::mutate(porc_won_lost = win / lose)

# 2. ESCALAR los datos (CRUCIAL para clúster)
# Normalizar las variables para que tengan igual peso
data_escalado <- tu_data |>
  dplyr::select(points, win, lose, `for`, against, porc_won_lost) |>
  scale() |>
  tibble::as_tibble()

# 3. ANÁLISIS DE CLÚSTER EN DOS PASOS (Two-Step)
# Este es el método más similar al que describiste

# 4. APLICAR CLÚSTER JERÁRQUICO (como en tu estudio)
distancia <- dist(data_escalado, method = "euclidean")
hc <- hclust(distancia, method = "ward.D2")

# 5. OBTENER LOS 3 CLÚSTERES (como en el estudio)
clusters_final <- cutree(hc, k = 3)

# 6. AÑADIR CLÚSTERES AL DATASET ORIGINAL
resultado_final <- tu_data |>
  dplyr::mutate(cluster = clusters_final,
         nivel = dplyr::case_when(
           cluster == 1 ~ "Top teams",
           cluster == 2 ~ "Intermediate teams", 
           cluster == 3 ~ "Bottom teams"
         )) |>
  readr::write_csv(glue::glue("tabla_{league_name}_2024_con_clusters.csv"))

# 7. ANALIZAR RESULTADOS
# Características de cada clúster
resultado_final %>%
  group_by(nivel) %>%
  summarise(across(everything(), mean, na.rm = TRUE))