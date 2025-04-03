# main.py
# 📊 Arquivo principal de roteamento do Dashboard BR Bank (Streamlit + Python)
# Controla navegação, perfil de usuário e interface global

import streamlit as st
from config.settings import USER_PROFILES
from pages import (
    home, overview, acquisition, retention,
    monetization, projections, analytics, accessibility
)
import datetime

# 🧠 Função principal
def main():
    # 🚀 Configuração inicial da aplicação
    st.set_page_config(
        page_title="Dashboard BR Bank",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # 🖼️ Logotipo (opcional)
    st.sidebar.image("assets/icons/brbank_logo.png", use_column_width=True)

    # 👤 Seletor de Perfil do Usuário
    st.sidebar.title("👤 Perfil do Usuário")
    selected_profile = st.sidebar.selectbox(
        "Selecione seu perfil de acesso:",
        USER_PROFILES,
        index=0,
        help="O conteúdo exibido será adaptado conforme o perfil selecionado."
    )

    # 💾 Armazena o perfil selecionado para uso em outras páginas
    st.session_state['profile'] = selected_profile

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
        "Escolha uma seção do dashboard:",
        list(PAGES.keys()),
        help="Use este menu para navegar entre os módulos táticos do BR Bank."
    )

    # 📌 Exibe visualização personalizada conforme o perfil
    st.caption(f"📌 Visualização personalizada para o perfil: **{selected_profile}**")

    # 🔁 Roteamento dinâmico
    if selected_page in PAGES:
        PAGES[selected_page].show(profile=selected_profile)
    else:
        st.error("Página não encontrada.")

    # ✅ Rodapé fixo
    ano = datetime.datetime.now().year
    st.markdown(
        f"""
        <hr style='margin-top: 2rem;'>
        <div style='text-align: center; color: gray; font-size: 0.85rem;'>
            Desenvolvido por Growth Analytics Team • BR Bank • {ano}
        </div>
        """,
        unsafe_allow_html=True
    )

# ▶️ Execução
if __name__ == "__main__":
    main()
