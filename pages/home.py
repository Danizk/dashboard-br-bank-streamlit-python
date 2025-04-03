# pages/home.py
# Página inicial – Boas-vindas e guia de uso do Dashboard BR Bank

import streamlit as st
from datetime import datetime

def show():
    st.title("🏦 Dashboard Tático • BR Bank")
    st.subheader("Bem-vindo ao centro de inteligência de crescimento")

    st.markdown("""
    Este dashboard foi desenvolvido para transformar **dados em decisões**, com foco na jornada do lead:
    **Aquisição → Retenção → Monetização**.

    ---
    """)

    # --- Perfil do Usuário (Pode ser implementado com autenticação ou seleção) ---
    profile = st.session_state.get('user_profile', 'Visualizador Geral') # Valor padrão
    st.markdown("### 👤 Perfil Atual:")
    st.info(f"Você está visualizando o dashboard como: **{profile}**")
    st.caption("💡 O perfil selecionado pode influenciar os insights e as métricas em destaque.")

    st.markdown("""
    ---
    ### 🚀 O que você pode fazer aqui:

    - 📊 **Visão Geral:** Acompanhar um resumo dos principais KPIs de Aquisição, Retenção e Monetização.
    - 📈 **Aquisição:** Analisar o desempenho das campanhas de marketing, o custo por lead (CPA), o retorno sobre o investimento (ROAS) e as taxas de conversão.
    - 🤝 **Retenção:** Monitorar o tempo médio de conversão, identificar gargalos no funil de vendas e analisar os motivos de perda de leads.
    - 💰 **Monetização:** Avaliar a receita gerada por vendedor, o ticket médio e o Lifetime Value (LTV) dos clientes.
    - 🔮 **Projeções e Simulações:** Utilizar ferramentas para projetar o impacto de diferentes cenários no faturamento e nas metas.
    - 🔍 **Análise Detalhada:** Explorar os dados em profundidade, aplicando filtros personalizados para identificar tendências e oportunidades.
    - ⚙️ **Acessibilidade:** Ajustar as preferências visuais para otimizar a sua experiência de uso (modo escuro, contraste, tamanho da fonte).

    ---
    """)

    st.markdown("### 🧭 Navegação:")
    st.markdown("""
    Utilize o menu lateral para acessar as diferentes seções do dashboard e obter insights específicos sobre cada etapa da jornada do lead.
    """)

    st.info("💡 Dica: Explore cada seção para obter uma visão completa do desempenho e identificar áreas de melhoria.")

    # Última atualização simulada (idealmente puxar de metadado ou processamento real)
    st.markdown("---")
    st.caption(f"📅 Última atualização dos dados: {datetime.today().strftime('%d/%m/%Y')}")
