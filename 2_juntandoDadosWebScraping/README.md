# 2. Juntando informações (webscraping)

A obtenção dos dados será feita via Internet, ou seja, uma raspagem de dados é necessária para obter os preços das ações com seus respectivos códigos da bolsa de valores de São Paulo.
Toda empresa/ativo/ação/papel possui um código para ser representado na Bovespa, é como se fosse um cpf para uma pessoa.

Para montar o banco de dados do problema basta conseguir esses códigos e depois usar alguma API para obter os preços das ações.

Terá um arquivo codigos.txt aqui com boa parte dos códigos das empresas cadastradas algum dia na bolsa de São Paulo, contudo está desatualizado, podendo haver empresas falidas até faltar empresas cadastradas recentemente.

Por isso será feita uma raspagem desses dados usando Selenium (web-driver) diretamente do site da B3 (bolsa de SP), pois ele está em javascript.

Nesta pasta temos alguns arquivos auxiliares:

* codigos.txt - códigos de quase todas ações cadastradas um dia na Bolsa de SP, pode haver códigos de empresas que não existem mais.

* codigosIbrx100.txt - contém o código das 100 empresas mais líquidas no momento (16/03/20) na Bolsa de SP.

* dadosAcoesBr.csv - dados diários de mercado de algumas empresas, muito parecido com a versão 02.

* dadosAcoesBrV2.csv - dados diários de mercado das empresas do Ibrx100, como abertura, fechamento, máximo, mínimo e volume. 
Trata-se de uma segunda versão (V2) pelo fato de perca de um arquivo. Os scripts das demais pastas devem rodar com .csv e 
não a versão 01.

* geraDadosAcoesBr.ipynb - jupyter notebook que gera o arquivo dadosAcoesBr.csv

* geraDadosAcoesBr.r - jupyter notebook que gera o arquivo dadosAcoesBr.csv