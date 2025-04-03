# pages/accessibility.py
# Página de Configurações de Acessibilidade Visual

import streamlit as st
from utils.accessibility import apply_theme

def show():
    st.title("♿ Acessibilidade e Preferências Visuais")
    st.markdown("Personalize sua experiência de uso para melhor conforto visual e inclusão digital.")

    # Carregar as configurações de tema atuais (se houver)
    theme_settings = st.session_state.get('theme', {'dark_mode': False, 'high_contrast': False, 'color_blind_mode': False, 'font_size': 'Médio'})

    # Dark Mode
    dark_mode = st.checkbox("🌙 Ativar modo escuro", value=theme_settings['dark_mode'])

    # Contraste alto
    high_contrast = st.checkbox("🧱 Ativar alto contraste", value=theme_settings['high_contrast'])

    # Modo daltônico
    color_blind_mode = st.checkbox("🎨 Ativar modo daltônico", value=theme_settings['color_blind_mode'])

    # Tamanho da fonte
    font_size = st.selectbox("🔤 Tamanho da fonte", options=["Pequeno", "Médio", "Grande"], index=["Pequeno", "Médio", "Grande"].index(theme_settings['font_size']))

    # Aplicar o tema ao clicar em um botão (melhor UX)
    if st.button("✅ Aplicar Preferências"):
        theme = {
            'dark_mode': dark_mode,
            'high_contrast': high_contrast,
            'color_blind_mode': color_blind_mode,
            'font_size': font_size
        }
        st.session_state['theme'] = theme
        apply_theme(theme) # A função apply_theme estaria em utils/accessibility.py
        st.success("Preferências de acessibilidade aplicadas!")

    st.markdown("---")
    st.markdown("### ⚙️ Configurações Atuais:")
    st.json(st.session_state.get('theme', {'dark_mode': False, 'high_contrast': False, 'color_blind_mode': False, 'font_size': 'Médio'}))

    st.info("⚠️ Estas configurações são visuais e são aplicadas via CSS customizado.")
    st.caption("🔒 As preferências são mantidas durante a sessão.")
