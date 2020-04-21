# FIA: finan�as inteligentes e automatizadas

## Objetivo

Prever o comportamento de a��es do mercado financeiro e encontrar a carteira (conjunto de a��es) com maior retorno poss�vel.

Todas tomadas de decis�o ser�o "data-driven" a partir de aprendizado de m�quina, ferramentas e fluxos de ci�ncia de dados.

Ser� utilizado R e Python neste projeto, pois s�o recursos gratuitos.

Todos os dados aqui ser�o do **mercado � vista de a��es**.

## Estrutura do projeto

1. Defini��o do problema

2. Juntando informa��es (webscraping)

3. An�lise explorat�ria (visualiza��o de dados)

4. Prepara��o do dados

5. Avaliar modelos preditivos

6. Melhorar precis�o dos modelos

7. Finalizar modelo e testar no mercado di�rio

## 1. Defini��o do problema

Trata-se de um estudo de mercado financeiro com intuito de ganhar dinheiro ao negociar (comprar/vender) a��es do mercado financeiro. Isso ser� feito coletando dados e modelando as s�ries temporais que s�o os pre�os das a��es.

A modelagem preditiva realizada visa prever os pre�os das a��es, sendo implementada com aprendizado de m�quina e intelig�ncia artifical, ou seja, ferramentas de ci�ncia de dados.

## 2. Juntando informa��es (webscraping)

A obten��o dos dados ser� feita via Internet, ou seja, uma raspagem de dados � necess�ria para obter os pre�os das a��es com seus respectivos c�digos da bolsa de valores de S�o Paulo.
Toda empresa/ativo/a��o/papel possui um c�digo para ser representado na Bovespa, � como se fosse um cpf para uma pessoa.

Para montar o banco de dados do problema basta conseguir esses c�digos e depois usar alguma API para obter os pre�os das a��es.

Ter� um arquivo .txt aqui com boa parte dos c�digos das empresas cadastradas algum dia na bolsa de S�o Paulo, contudo est� desatualizado, podendo haver empresas falidas at� faltar empresas cadastradas recentemente.

Por isso ser� feita uma raspagem desses dados usando Selenium (web-driver) diretamente do site da B3 (bolsa de SP), pois ele est� em javascript.

## 3. An�lise explorat�ria (visualiza��o de dados)

Visualiza��o dos dados para conhecer o dom�nio do problema.

Gerar estat�sticas descritivas do tipo e distribui��es das vari�veis (colunas) explicativas, cruzando elas atrav�s de diferentes gr�ficos que possibilitem enxergar o comportamento da s�rie hist�rica ao longo do tempo.

## 4. Modelagem preditiva

* Limpeza dos dados
* Sele��o de vari�veis/"features"
* Transforma��o de dados e testar suposi��es

## 5. Avaliar modelos preditivos

* Divis�o do conjunto de dados e valida��o
* Treinar e avaliar diferentes modelos preditivos
* Comparar modelos

## 6. Melhorar precis�o dos modelos

* Ajuste de hiperpar�metros do modelos 
* Uni�o do modelos treinados (ensembles)
* Salvar o modelo final

## 7. Finalizar modelo e testar no mercado di�rio

* Montagem uma metologia de trading 
* Elabora��o de carteira (conjunto de a��es)
* An�lise de risco e retorno





