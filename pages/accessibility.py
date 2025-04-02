# pages/accessibility.py
# Página de Configurações de Acessibilidade Visual

import streamlit as st
from config.settings import THEME

def show():
    st.title("♿ Acessibilidade e Preferências Visuais")
    st.markdown("Personalize sua experiência de uso para melhor conforto visual e inclusão digital.")

    # Dark Mode
    dark_mode = st.checkbox("🌙 Ativar modo escuro", value=THEME["dark_mode"])

    # Contraste alto
    high_contrast = st.checkbox("🧱 Ativar alto contraste", value=THEME["high_contrast"])

    # Modo daltônico
    color_blind_mode = st.checkbox("🎨 Ativar modo daltônico", value=THEME["color_blind_mode"])

    # Tamanho da fonte
    font_size = st.selectbox("🔤 Tamanho da fonte", options=["Pequeno", "Médio", "Grande"], index=1)

    # Mostrar as configurações aplicadas
    st.markdown("### 🎯 Preferências aplicadas:")
    st.json({
        "Modo Escuro": dark_mode,
        "Alto Contraste": high_contrast,
        "Modo Daltônico": color_blind_mode,
        "Tamanho da Fonte": font_size
    })

    st.info("⚠️ Estas configurações são visuais e não afetam os dados. "
            "Elas podem ser aplicadas via CSS customizado no frontend do Streamlit.")

    st.caption("🔒 Todas as preferências são locais e não são armazenadas permanentemente.")

