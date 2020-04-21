# 2. Juntando informa��es (webscraping)

A obten��o dos dados ser� feita via Internet, ou seja, uma raspagem de dados � necess�ria para obter os pre�os das a��es com seus respectivos c�digos da bolsa de valores de S�o Paulo.
Toda empresa/ativo/a��o/papel possui um c�digo para ser representado na Bovespa, � como se fosse um cpf para uma pessoa.

Para montar o banco de dados do problema basta conseguir esses c�digos e depois usar alguma API para obter os pre�os das a��es.

Ter� um arquivo codigos.txt aqui com boa parte dos c�digos das empresas cadastradas algum dia na bolsa de S�o Paulo, contudo est� desatualizado, podendo haver empresas falidas at� faltar empresas cadastradas recentemente.

Por isso ser� feita uma raspagem desses dados usando Selenium (web-driver) diretamente do site da B3 (bolsa de SP), pois ele est� em javascript.

Nesta pasta temos alguns arquivos auxiliares:

* codigos.txt - c�digos de quase todas a��es cadastradas um dia na Bolsa de SP, pode haver c�digos de empresas que n�o existem mais.

* codigosIbrx100.txt - cont�m o c�digo das 100 empresas mais l�quidas no momento (16/03/20) na Bolsa de SP.

* dadosAcoesBr.csv - dados di�rios de mercado de algumas empresas, muito parecido com a vers�o 02.

* dadosAcoesBrV2.csv - dados di�rios de mercado das empresas do Ibrx100, como abertura, fechamento, m�ximo, m�nimo e volume. 
Trata-se de uma segunda vers�o (V2) pelo fato de perca de um arquivo. Os scripts das demais pastas devem rodar com .csv e 
n�o a vers�o 01.

* geraDadosAcoesBr.ipynb - jupyter notebook que gera o arquivo dadosAcoesBr.csv

* geraDadosAcoesBr.r - jupyter notebook que gera o arquivo dadosAcoesBr.csv