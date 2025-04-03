# main.py
# 📊 Arquivo principal de roteamento do Dashboard BR Bank (Streamlit + Python)

import streamlit as st
from pages import (
    home, overview, acquisition, retention,
    monetization, projections, analytics, accessibility
)
from config.settings import USER_PROFILES

# 🚀 Configuração da aplicação
st.set_page_config(
    page_title="Dashboard BR Bank",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 👤 Perfil do Usuário
st.sidebar.title("👤 Perfil de Acesso")
selected_profile = st.sidebar.selectbox(
    "Selecione seu perfil:",
    USER_PROFILES,
    index=0,
    help="O conteúdo será personalizado de acordo com o perfil selecionado."
)

# 🧭 Menu de Navegação
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
    "Escolha uma seção:",
    list(PAGES.keys()),
    help="Use este menu para navegar entre os módulos estratégicos."
)

# 🔄 Executar página selecionada
PAGES[selected_page].show(profile=selected_profile)

# ✅ Rodapé opcional
st.markdown(
    """
    <hr style='margin-top: 2rem;'>
    <div style='text-align: center; color: gray; font-size: 0.85rem;'>
        Desenvolvido por Growth Analytics Team • BR Bank • 2023
    </div>
    """,
    unsafe_allow_html=True
)
