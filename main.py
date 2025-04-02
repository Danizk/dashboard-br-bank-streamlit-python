
import streamlit as st
from pages import (
    home,
    overview,
    acquisition,
    retention,
    monetization,
    projections,
    analytics,
    accessibility,
)

# Configurações iniciais do Streamlit
st.set_page_config(
    page_title="Dashboard BR Bank",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Mapeamento das páginas do menu
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

# Título da barra lateral e seletor de página
st.sidebar.title("📌 Navegação")
selected_page = st.sidebar.radio("Escolha uma página:", list(PAGES.keys()))

# Executa a função .show() da página selecionada
PAGES[selected_page].show()
