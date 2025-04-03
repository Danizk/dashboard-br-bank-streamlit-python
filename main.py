# main.py
# 📊 Arquivo principal de roteamento do Dashboard BR Bank (Streamlit + Python)

import streamlit as st
from pages import (
    home,
    overview,
    acquisition,
    retention,
    monetization,
    projections,
    analytics,
    accessibility
)
from config.settings import USER_PROFILES

# 🚀 Configuração geral da aplicação
st.set_page_config(
    page_title="Dashboard BR Bank",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 👤 Seletor de Perfil do Usuário
st.sidebar.title("👤 Perfil de Acesso")
selected_profile = st.sidebar.selectbox(
    label="Selecione seu perfil:",
    options=USER_PROFILES,
    index=0,
    help="O conteúdo será adaptado conforme o tipo de usuário (Executivo, Growth, Vendas, Produto)."
)

# 🧭 Menu de Navegação (Modular por objetivo estratégico)
st.sidebar.title("📌 Navegação")
PAGES = {
    "🏠 Home": home,
    "📊 Visão Executiva": overview,
    "📈 Aquisição de Leads": acquisition,
    "🔁 Retenção de Leads": retention,
    "💰 Monetização": monetization,
    "🚀 Projeções e Receita": projections,
    "🧠 Visão Analítica": analytics,
    "♿ Acessibilidade": accessibility
}

selected_page = st.sidebar.radio(
    label="Escolha uma seção:",
    options=list(PAGES.keys()),
    help="Navegue pelos módulos do dashboard conforme seu objetivo."
)

# 🔄 Renderização da Página Selecionada
PAGES[selected_page].show(profile=selected_profile)

# ✅ Rodapé institucional
st.markdown(
    """
    <hr style='margin-top: 2rem;'>
    <div style='text-align: center; color: gray; font-size: 0.85rem;'>
        Desenvolvido por <b>Growth Analytics Team</b> • BR Bank • ©2023-2025
    </div>
    """,
    unsafe_allow_html=True
)
