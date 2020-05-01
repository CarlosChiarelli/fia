import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def nomesTodasAcoes(df, retLista = False):
    # recebe o df completo e retorna df com nomes das ações
    nomesAcoes = df.columns.str.replace('_sa_','',regex=False)
    nomesAcoes = nomesAcoes.str.replace('open|high|low|close|volume|adjusted','',regex=True).unique()
    nomesAcoes = list(nomesAcoes)
    nomesAcoes.remove('data')
    nomesAcoes.sort()
    # organiza em matriz 10x10
    x = np.array(nomesAcoes)
    nomesDf = pd.DataFrame(data = x.reshape(10,10))
    nomesDf.columns = ['','','','','','','','','','']

    if not retLista:
        return nomesDf
    else:
        return nomesAcoes

def datasIniFim(df):
    # recebe o df completa e retorna 2 strings (datas)
    ini = df.data.sort_values()[0]
    fim = df.data.sort_values(ascending=False).reset_index().iloc[0,1]

    return ini, fim

def selecionaColsAtivo(ativo, df):
    # recebe o nome do ativo e o df completo, seleciona suas colunas
    colsAlvo = (df.columns.str.startswith(ativo)) | (df.columns.str.startswith('data'))
    colsAlvo = df.columns[pd.Series(colsAlvo)]
    aux = df[colsAlvo]
    # corrigindo o nome
    aux.columns = aux.columns.str.replace(ativo+'_sa_','')
    return aux

def plotaCandlestick(df):
    # recebe o df do ativo e plota Candlestick dinamico

    # fonte dos dados
    source = df

    # configura as cores
    open_close_color = alt.condition("datum.open <= datum.close",
                                     alt.value("#06982d"),
                                     alt.value("#ae1325"))

    # labels no eixo x
    base = alt.Chart(source).encode(
        alt.X('data:T',
              axis=alt.Axis(
                  format='%d - %m - %Y',
                  labelAngle=-45,
                  title='Data: ano - mês - dia'
              )
        ),
        color=open_close_color
    )

    # plotas os traços
    rule = base.mark_rule().encode(
        alt.Y(
            'low:Q',
            title='Preço (R$)',
            scale=alt.Scale(zero=False),
        ),
        alt.Y2('high:Q')
    ).interactive()

    # plotas as barras
    bar = base.mark_bar().encode(
        alt.Y('open:Q'),
        alt.Y2('close:Q')
    ).interactive()

    # une traços + barras, ajusta tamanho
    return (rule + bar).properties(width = 600, height = 600)

def main():
    # barra lateral
    #pagina = st.sidebar.selectbox("ESCOLHA A PÁGINA", ["Início", "Visualização","Teste indicador"])
    pagina = st.sidebar.radio("PÁGINAS", ["Início", "Visualização","Teste indicador","Inteligência Artificial"])
    # lendo os dados do github
    df = pd.read_csv('https://raw.githubusercontent.com/CarlosChiarelli/FIA/master/2_juntandoDadosWebScraping/dadosAcoesBrV2.csv')

    if pagina == 'Início':
        # início
        st.image('logo.jpg', width=200)
        st.title('Finanças Inteligentes Automatizadas')
        st.subheader('Ciência de dados aplicada em finanças')
        st.image('https://media.giphy.com/media/xTiTnqUxyWbsAXq7Ju/giphy.gif', width=200)

        st.subheader('APRESENTAÇÃO DOS DADOS')

        st.subheader('Preços diários das ações da Bovespa ("mercado à vista"):')
        st.markdown('''

        **Colunas**:

        * *data* = dia dos dados

        * *open* = abertura

        * *high* = máximo

        * *low* = mínimo

        * *close* = fechamento

        * *volume* = volume

        * *adjusted* = preço ajustado
        ''')

        # nomes ações disponiveis
        st.subheader('Empresas disponíveis para análise:')
        nomesDf = nomesTodasAcoes(df)
        st.table(nomesDf.head(10))

        # intervalo de datas
        st.subheader('Intervalo temporal dos dados:')
        ini, fim = datasIniFim(df)
        st.markdown('**Data inicial**: '+ini)
        st.markdown('**Data final**: '+fim)

    elif pagina == 'Visualização':
        # titulo
        st.title('Visualização dos dados')
        st.image('https://media.giphy.com/media/PKl9JTqnoiKtO/giphy.gif', width=200)

        # pergunta qual ação analisar
        nomesAcoes = nomesTodasAcoes(df, retLista=True)
        selecao = st.selectbox('EMPRESA PARA VISUALIZAR:', tuple(nomesAcoes))
        for ativo in nomesAcoes:
            if selecao == ativo:
                break

        # empresa escolhida
        st.markdown('# '+ativo)

        # gera df do ativo selecionado
        dfAtivo = selecionaColsAtivo(ativo, df)
        # visualiza a tabela
        st.dataframe(dfAtivo.head())

        st.subheader('Candlestick (gráfico de vela)')
        st.write(plotaCandlestick(dfAtivo))




    elif pagina == 'Teste indicador':
        st.title('Em desenvolvimento...')
        st.image('https://media.giphy.com/media/tTJpYjdERI2lO/giphy.gif', width=200)

    elif pagina == 'Inteligência Artificial':
        st.title('Em desenvolvimento...')
        st.image('https://media.giphy.com/media/tTJpYjdERI2lO/giphy.gif', width=200)


if __name__ == '__main__':
    main()
