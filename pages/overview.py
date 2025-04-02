# pages/overview.py
# Visão Executiva – KPIs principais e metas

import streamlit as st
import pandas as pd
from config.settings import PALETTE
from utils.kpi_calculator import (
    calcular_cac, calcular_roas, calcular_margem_liquida,
    calcular_taxa_conversao, calcular_ticket_medio
)
from utils.insights_generator import gerar_insight_receita, gerar_insight_conversao

# Simulação de dados carregados (normalmente virão do processed/)
df_kpis = pd.read_csv("data/processed/kpis_gerais.csv")

# KPIs principais
receita_total = df_kpis["receita_total"].iloc[0]
lucro_liquido = df_kpis["lucro_liquido"].iloc[0]
investimento_ads = df_kpis["investimento_ads"].iloc[0]
clientes_convertidos = df_kpis["clientes_convertidos"].iloc[0]
leads_captados = df_kpis["leads_captados"].iloc[0]
visitantes = df_kpis["visitantes"].iloc[0]

# Cálculos
cac = calcular_cac(investimento_ads, clientes_convertidos)
roas = calcular_roas(receita_total, investimento_ads)
margem = calcular_margem_liquida(lucro_liquido, receita_total)
taxa_conv_site = calcular_taxa_conversao(clientes_convertidos, visitantes)
ticket_medio = calcular_ticket_medio(receita_total, clientes_convertidos)

def show():
    st.title("📊 Visão Executiva – Painel Geral de Performance")
    st.markdown("Indicadores de alto nível da operação do BR Bank para tomada de decisões estratégicas.")

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Receita Total", f"R$ {receita_total:,.2f}")
    col2.metric("📈 ROAS", f"{roas:.2f}%")
    col3.metric("🎯 CAC", f"R$ {cac:,.2f}")

    col4, col5, col6 = st.columns(3)
    col4.metric("🏆 Lucro Líquido", f"R$ {lucro_liquido:,.2f}")
    col5.metric("📉 Margem Líquida", f"{margem:.2f}%")
    col6.metric("🧲 Conversão Visitante → Cliente", f"{taxa_conv_site:.2f}%")

    st.markdown("---")

    st.subheader("📌 Meta Estratégica: R$ 30 milhões em Receita")

    st.progress(receita_total / 30_000_000)

    st.markdown("### 📍 Ticket Médio Atual")
    st.success(f"🎟️ R$ {ticket_medio:,.2f} por cliente")

    st.markdown("---")

    # Insights automáticos
    st.subheader("🧠 Insights Automatizados")
    st.info(gerar_insight_receita(receita_total))
    st.warning(gerar_insight_conversao(taxa_conv_site))

    st.markdown("---")
    st.caption("Dados do período: 01/09/2022 a 28/02/2023 | Fonte: BR_BANK_DANI_KALOI.xlsv (tratado)")

