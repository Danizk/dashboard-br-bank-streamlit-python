# pages/home.py
import streamlit as st

def show(profile):
    st.title("🏠 Bem-vindo ao Dashboard BR Bank")
    
    st.markdown(f"""
    Olá, **{profile}**! Este dashboard foi desenvolvido para apoiar decisões baseadas em dados nas áreas de **Aquisição**, **Retenção** e **Monetização**.

    Utilize o menu lateral para navegar entre os módulos. Os dados são atualizados automaticamente a partir de arquivos processados.

    ---
    **Perfis disponíveis:**
    - Executivo: visão geral e indicadores estratégicos
    - Growth: foco em tráfego pago, CAC, ROAS e leads
    - Vendas: conversão, follow-up, desempenho por vendedor
    - Produto: oportunidades de upsell e motivos de perda

    ---
    """)
