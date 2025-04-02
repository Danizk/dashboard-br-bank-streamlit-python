# utils/accessibility.py
# Funções utilitárias para suporte à acessibilidade visual no dashboard BR Bank

import streamlit as st
from config.settings import THEME

def aplicar_estilo_global():
    """
    Aplica configurações visuais globais com base no tema (modo escuro, alto contraste, daltônico).
    Essa função deve ser chamada no início de cada página Streamlit.
    """
    dark_mode = THEME["dark_mode"]
    high_contrast = THEME["high_contrast"]
    color_blind = THEME["color_blind_mode"]

    custom_css = ""

    if dark_mode:
        custom_css += """
            <style>
            body {
                background-color: #1F2937;
                color: #F8F9FA;
            }
            .stButton>button {
                background-color: #005BA1;
                color: white;
            }
            </style>
        """

    if high_contrast:
        custom_css += """
            <style>
            * {
                outline: none !important;
            }
            h1, h2, h3, h4, h5, h6, p {
                color: #FFFFFF !important;
                background-color: #000000 !important;
            }
            </style>
        """

    if color_blind:
        custom_css += """
            <style>
            .color-coded-bar {
                background: repeating-linear-gradient(
                    45deg,
                    #005BA1,
                    #005BA1 10px,
                    #F59E0B 10px,
                    #F59E0B 20px
                );
            }
            </style>
        """

    st.markdown(custom_css, unsafe_allow_html=True)

def render_configuracoes_acessibilidade():
    """
    Exibe opções para o usuário ativar/desativar recursos de acessibilidade.
    """
    st.sidebar.markdown("♿ **Acessibilidade Visual**")

    dark_mode = st.sidebar.checkbox("🌙 Modo Escuro", value=THEME["dark_mode"])
    high_contrast = st.sidebar.checkbox("⚫ Alto Contraste", value=THEME["high_contrast"])
    color_blind = st.sidebar.checkbox("🎨 Compatível com Daltônicos", value=THEME["color_blind_mode"])

    # Atualiza o dicionário global
    THEME["dark_mode"] = dark_mode
    THEME["high_contrast"] = high_contrast
    THEME["color_blind_mode"] = color_blind
