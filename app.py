import streamlit as st
import Utils.request as rqt

cotacao = rqt.requisitar_cotacao("EUR","BRL")

print(cotacao)