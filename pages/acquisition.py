# pages/acquisition.py
# Módulo de Aquisição – Performance de Campanhas e Captação de Leads

import streamlit as st
import pandas as pd
from config.settings import PALETTE
from utils.kpi_calculator import calcular_ctr, calcular_cpa, calcular_roas, calcular_taxa_conversao

# Dados simulados (você pode substituir pelos dados reais da pasta processed/)
df_aquisicao = pd.read_csv("data/processed/kpis_aquisicao.csv")

# KPIs por canal
cliques_total = df_aquisicao["cliques"].sum()
impressoes_total = df_aquisicao["impressoes"].sum()
leads_total = df_aquisicao["leads"].sum()
investimento_total = df_aquisicao["investimento"].sum()
receita_total = df_aquisicao["receita"].sum()

# Cálculos
ctr = calcular_ctr(impressoes_total, cliques_total)
cpa = calcular_cpa(investimento_total, leads_total)
roas = calcular_roas(receita_total, investimento_total)
taxa_conv_lead = calcular_taxa_conversao(leads_total, cliques_total)

def show():
    st.title("📈 Aquisição de Leads – Performance de Campanhas")
    st.markdown("Métricas e desempenho por canal de mídia (Google Ads, Meta Ads).")

    col1, col2, col3 = st.columns(3)
    col1.metric("🖱️ CTR (Click-through Rate)", f"{ctr:.2f}%")
    col2.metric("💰 CPA (Custo por Lead)", f"R$ {cpa:,.2f}")
    col3.metric("📈 ROAS (Retorno sobre Ads)", f"{roas:.2f}%")

    col4, col5 = st.columns(2)
    col4.metric("🧲 Conversão Clique → Lead", f"{taxa_conv_lead:.2f}%")
    col5.metric("🎯 Investimento Total", f"R$ {investimento_total:,.2f}")

    st.markdown("---")

    st.subheader("📊 Desempenho por Canal")
    st.dataframe(df_aquisicao.style.format({
        "impressoes": "{:,.0f}",
        "cliques": "{:,.0f}",
        "leads": "{:,.0f}",
        "investimento": "R$ {:,.2f}",
        "receita": "R$ {:,.2f}"
    }))

    st.markdown("---")

    st.caption("Fonte: Dados tratados da planilha BR_BANK_DANI_KALOI.xlsv")

