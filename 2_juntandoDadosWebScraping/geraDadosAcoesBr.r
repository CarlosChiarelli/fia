funcaoPrincipal = function(){

library(tidyverse)
library(quantmod)
library(janitor)

# limpando a memoria
rm(list = ls())

###### FUNÇÕES UTILIZADAS ######

obtemAcaoXts <- function(codigo, dataIni='2017-01-01', dataFim='2020-01-01'){
  # xts é um formato de tabela de series temporais do R
  # essa função retorna o numero de linhas da 
  # de uma ação obtida no quantmod de 2017 a 2020
  
  aux = getSymbols(
    codigo,
    from = as.Date(dataIni),
    to = as.Date(dataFim),
    auto.assign = F
  ) 
  
  return(aux)
}

numLinhas <- function(xtsAcao){
  # retorna o numero de linha de um xts
  
  return(nrow(xtsAcao))
}

calculaModa <- function(x){
  # calcula a moda
  # o intuito é pegar as ações com numero de linhas parecidas
  
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}

xtsParaDf <- function(xts){
  # pega um xts e retorna um tibble com a coluna data
  # e os nomes das colunas limpos
  
  dataXts <- index(xts)
  
  df <- xts %>% 
    as_tibble() %>% 
    mutate(
      data = dataXts
    ) %>% 
    clean_names()
  
  return(df)
}

###### FUNÇÕES UTILIZADAS ######

# carregando codigos da Ibovespa e 
codigos <- read_lines('codigosIbrx100.txt')
#codDf <- read_csv('codigosIbovespIbrx100.csv')

# filtrando as 100 acoes mais liquidas
# que já fazem parte do ibovespa
#codDf <- codDf %>% 
#  filter(indice != 'ibovespa')
  
# obtendo códigos 
#codigos <- codDf %>% 
#  select(codigo) %>% 
#  as_vector()

# loop para obter vetor com numero de linhas das acoes
quantLinhasIbrx100 = map_int(
  codigos,
  function(codigo){
    codigo %>% 
      obtemAcaoXts() %>% 
      numLinhas()
  }
)

# calcula quantidade de linhas que mais aparecem  
modaLinhas <- calculaModa(quantLinhasIbrx100)

# vetor para selecionar ações com mais linhas
logicoMaxLinhas <- quantLinhasIbrx100 == modaLinhas

# filtrando ações desejadas na tabela
# codDf <- codDf %>% 
#  filter(logicoMaxLinhas) 

# codigos alvo
codAlvos <- codigos
#  select(codigo) %>% 
#  as_vector()

# agora vamos fazer um merge de todos os dados
# para realizar essa união vamos separar 1 ação 
# e ir unindo as demais nela
acoesDf <- codAlvos[1] %>% 
  obtemAcaoXts() %>% 
  xtsParaDf()

# atualiza o vetor com os ´codigos
codAlvos <- codAlvos[-1]

# vai fazendo a união dos dados pela coluna data
for (codigo in codAlvos) {
  
  # obtem os dados da ação
  df <- codigo %>% 
    obtemAcaoXts() %>% 
    xtsParaDf()
  
  # faz o merge no DF final
  acoesDf <- acoesDf %>% 
    left_join(df)
}

# salvando dados
# ressaltando que essas fazem parte das 100
# mais liquidas na data 15/02/2020
# com algumas faltantes (devido a API para obter os dados)
acoesDf %>% 
  write_csv('dadosAcoesBrV2.csv')

# limpando a memoria
rm(list = ls())

}