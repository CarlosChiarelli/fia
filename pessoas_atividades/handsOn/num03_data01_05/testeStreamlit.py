# aplicacao Streamlit
import pandas as pd
import streamlit as st

def main():
    # funcao principal
    st.image('logo.jpg', width=200)
    st.title('Aplicacao web: renda variável')
    st.markdown('Projeto de ciência de dados aplicado em finanças.')

    # adicionando dados
    st.subheader('Insira seus dados:')
    arquivo = st.file_uploader('Escolha seu arquivo CSV', type='csv')

    if arquivo is not None:
        # le arquivo
        df = pd.read_csv(arquivo)

        quantLinhas = st.slider('quantidade de linha',
                                min_value = 5,
                                max_value = 100)

        st.dataframe(df.head(quantLinhas))

        # adicionando botão
        botao = st.button('Ver analise estatística')
        if botao:
            st.dataframe(df.describe().transpose())


if __name__ == '__main__':
    main()
