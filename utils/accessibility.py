# utils/accessibility.py
# Configurações e utilitários para acessibilidade no dashboard BR Bank

import streamlit as st

def aplicar_tema_acessibilidade(theme_config: dict):
    """
    Aplica configurações de acessibilidade conforme o dicionário de preferências.
    """
    dark_mode = theme_config.get("dark_mode", False)
    high_contrast = theme_config.get("high_contrast", False)
    color_blind_mode = theme_config.get("color_blind_mode", False)

    st.session_state["dark_mode"] = dark_mode
    st.session_state["high_contrast"] = high_contrast
    st.session_state["color_blind_mode"] = color_blind_mode

def exibir_config_acessibilidade():
    """
    Adiciona controles interativos no sidebar para o usuário configurar preferências visuais.
    """
    st.sidebar.markdown("### ♿ Acessibilidade")

    st.session_state["dark_mode"] = st.sidebar.checkbox("🌙 Modo Escuro", value=st.session_state.get("dark_mode", True))
    st.session_state["high_contrast"] = st.sidebar.checkbox("🌈 Alto Contraste", value=st.session_state.get("high_contrast", False))
    st.session_state["color_blind_mode"] = st.sidebar.checkbox("🧠 Modo Daltônico", value=st.session_state.get("color_blind_mode", False))

def aplicar_estilo_personalizado():
    """
    Insere CSS customizado para temas escuros e contraste elevado.
    """
    estilo_base = """
        <style>
        body { font-family: 'Arial', sans-serif; }
        </style>
    """

    dark_style = """
        <style>
        .stApp { background-color: #1F2937; color: #F4F4F5; }
        .css-1aumxhk, .css-qrbaxs { background-color: #1F2937 !important; }
        </style>
    """

    contraste_alto = """
        <style>
        * { outline: 1px solid #FFD700 !important; }
        </style>
    """

    daltônico = """
        <style>
        .stApp { filter: grayscale(50%); }
        </style>
    """

    st.markdown(estilo_base, unsafe_allow_html=True)

    if st.session_state.get("dark_mode"):
        st.markdown(dark_style, unsafe_allow_html=True)
    if st.session_state.get("high_contrast"):
        st.markdown(contraste_alto, unsafe_allow_html=True)
    if st.session_state.get("color_blind_mode"):
        st.markdown(daltônico, unsafe_allow_html=True)
