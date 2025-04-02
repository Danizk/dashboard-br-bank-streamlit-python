# pages/home.py
# Página inicial – Onboarding e seleção de perfil

import streamlit as st
from config.settings import USER_PROFILES, THEME
from datetime import datetime

def show():
    st.set_page_config(page_title="Dashboard BR Bank", layout="wide")

    st.title("🏦 Dashboard Tático – BR Bank")
    st.markdown("Bem-vindo ao painel interativo que conecta dados à estratégia. Use os menus laterais para navegar entre as áreas de **Aquisição**, **Retenção**, **Monetização** e **Análises**.")

    st.markdown("---")

    # Seletor de perfil
    st.sidebar.title("👤 Selecione seu perfil")
    perfil = st.sidebar.radio("Qual é o seu papel no BR Bank?", USER_PROFILES)

    st.success(f"Você está visualizando o dashboard como **{perfil}**.")
    st.markdown("🔄 Os dados deste painel são baseados no período: **01/09/2022 a 28/02/2023** (dados históricos tratados)")

    # Última atualização simulada (base estática)
    st.markdown(f"📅 Última atualização dos dados: `{datetime(2023, 2, 28).strftime('%d/%m/%Y')}`")

    # Instruções
    with st.expander("ℹ️ Como usar este dashboard?"):
        st.markdown("""
        - Use o menu lateral para acessar as diferentes áreas do dashboard.
        - Filtre por canal, público, campanha ou vendedor conforme necessário.
        - Simule cenários nas abas de **Projeções** e **Monetização**.
        - Ative recursos de acessibilidade no menu lateral (modo escuro, alto contraste, etc.).
        - Passe o mouse sobre os gráficos para ver detalhes com **tooltips interativos**.
        """)

    # Estilo adicional conforme tema
    if THEME["dark_mode"]:
        st.markdown("<style>body { background-color: #1F2937; color: white; }</style>", unsafe_allow_html=True)
