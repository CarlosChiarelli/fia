library(tidyverse)
library(lubridate)

# lendo dados
acoesDf <- read_csv('../2_juntandoDadosWebScraping/dadosAcoesBr.csv')

# deixando apenas vale
acoesDf <- acoesDf %>% 
  select(data, starts_with('vale'))

# removendo 2 linhas de nulos
acoesDf <- acoesDf %>% 
  filter(
    !is.na(vale3_sa_open)
  ) %>% 
  rename_at(
    vars(-data),
    funs(str_sub(., str_sub(10)))
  )

# vetor com numero dos dias da semana
semana <- c(
  "dom",
  "seg",
  "terc",
  "quart",
  "quint",
  "sext",
  "sab"
)

# adicionando dummies dias da semana
acoesDf <- acoesDf %>% 
  mutate(
    diasSeman = wday(data),
    diasSemanNome = semana[diasSeman]
  ) %>% 
  spread(
    diasSemanNome, diasSeman
  ) %>% 
  mutate_at(
    vars(quart:terc),
    funs(
      if_else(is.na(.), 0, 1)
    )
  ) 

# salvando dados
acoesDf %>% 
  write_csv('vale.csv')











