import streamlit as st
import xml.etree.ElementTree as ET


@st.cache_data
def carregar_moedas_iso(caminho_xml: str) -> dict:
    tree = ET.parse(caminho_xml)
    root = tree.getroot()

    moedas = {}
    codigos_excluidos = {"XTS", "XXX", "XAU", "XAG", "XPD", "XPT"}

    for entrada in root.findall("./CcyTbl/CcyNtry"):
        codigo = entrada.findtext("Ccy")
        nome = entrada.findtext("CcyNm")

        if not codigo or not nome:
            continue

        if codigo in codigos_excluidos:
            continue

        if codigo not in moedas:
            moedas[codigo] = nome

    return dict(sorted(moedas.items()))

def converter(valor, cotacao):
    if valor <= 0:
        st.error("Valor Inválido! Digite um valor possível de converter.")
        return 0
    else:
        return valor * cotacao