# pages/home.py
# Página inicial – Boas-vindas e guia de uso do Dashboard BR Bank

import streamlit as st
from datetime import datetime

def show(profile):
    st.title("🏦 Dashboard Tático • BR Bank")
    st.subheader("Bem-vindo ao centro de inteligência de crescimento")

    st.markdown("""
    Este dashboard foi desenvolvido para transformar **dados em decisões**, com foco na jornada do lead:  
    **Aquisição → Retenção → Monetização**.

    ---
    """)

    st.markdown("### 👤 Perfil Selecionado:")
    st.success(f"Você está visualizando o dashboard como: **{profile}**")

    st.markdown("""
    ---
    ### 🚀 O que você pode fazer aqui:
    
    - 📊 **Executivo:** Acompanhar KPIs estratégicos e resultados consolidados  
    - 📈 **Growth:** Monitorar desempenho de campanhas, CAC, ROAS e conversão  
    - 🤝 **Vendas:** Priorizar leads ativos e analisar performance de vendedores  
    - 🧪 **Produto:** Identificar gargalos, oportunidades e LTV por segmento
    
    ---
    """)

    st.markdown("### 🧭 Como Navegar:")
    st.markdown("""
    Use o menu lateral para acessar as seções:
    
    - **Visão Executiva**: KPIs consolidados e resultados gerais  
    - **Aquisição**: Funil de tráfego pago e eficiência por canal  
    - **Retenção**: Performance de atendimento, follow-up e perdas  
    - **Monetização**: Receita, ticket médio e conversão por vendedor  
    - **Projeções**: Simuladores e metas futuras  
    - **Visão Analítica**: Exploração livre dos dados  
    - **Acessibilidade**: Ajustes de contraste, fontes e modo escuro
    """)

    st.info("💡 Dica: Você pode alternar entre os perfis a qualquer momento no menu lateral.")

    # Última atualização simulada (idealmente puxar de metadado do CSV ou processamento real)
    st.markdown("---")
    st.caption(f"📅 Última atualização dos dados: {datetime.today().strftime('%d/%m/%Y')}")
