import streamlit as st
from Utils import request,utils

st.title("💵 Conversão de Moedas")

moedas = utils.carregar_moedas_iso("list-one-moedas-ptbr.xml")
opcoes_moedas = list(moedas.keys())

col1, col2 = st.columns(2)

with col1:
    moeda_inicial = st.selectbox(
        "Moeda Base:",
        opcoes_moedas,
        index=opcoes_moedas.index("BRL") if "BRL" in opcoes_moedas else 0,
        placeholder="Escolha uma opção",
        format_func=lambda codigo: f"{codigo} - {moedas[codigo]}"
    )

with col2:
    moeda_final = st.selectbox(
        "Moeda Destino:",
        opcoes_moedas,
        index=None,
        placeholder="Escolha uma opção",
        format_func=lambda codigo: f"{codigo} - {moedas[codigo]}"
    )

col3,col4 = st.columns(2)

with col3:
    valor = st.number_input("Valor: ")
    buscar = st.button("Converter", type="primary", )

with col4:
    if buscar:
        cotacao = request.requisitar_cotacao(moeda_inicial,moeda_final)
        if type(cotacao) != type(1):
            valor_final = utils.converter(valor, float(cotacao["bid"]))
            if valor_final != 0:
                st.title(f"{cotacao["code"]} {valor} vale: {cotacao["codein"]} {valor_final:.2f}")
                # st.write(cotacao)
        else:
            st.title("Cotação Inexistente!")
                



