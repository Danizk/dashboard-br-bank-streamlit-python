# pages/monetization.py
# Módulo de Monetização – Receita, Vendas e Ticket Médio

import streamlit as st
import pandas as pd
from config.settings import PALETTE
from utils.kpi_calculator import (
    calcular_ticket_medio,
    calcular_ltv,
    calcular_taxa_conversao,
    calcular_receita_total_por_vendedor,
    calcular_ranking_vendedores
)

# Carregamento dos dados processados
df_vendas = pd.read_csv("data/processed/kpis_monetizacao.csv")

# KPIs gerais
receita_total = df_vendas["receita"].sum()
total_clientes = df_vendas["clientes"].sum()
ticket_medio = calcular_ticket_medio(receita_total, total_clientes)
ltv = calcular_ltv(ticket_medio)

def show():
    st.title("💰 Monetização – Receita e Performance Comercial")
    st.markdown("Avalie o desempenho financeiro, ticket médio por cliente e ranking dos vendedores.")

    col1, col2, col3 = st.columns(3)
    col1.metric("💵 Receita Total", f"R$ {receita_total:,.2f}")
    col2.metric("🎟️ Ticket Médio", f"R$ {ticket_medio:,.2f}")
    col3.metric("📈 LTV Estimado", f"R$ {ltv:,.2f}")

    st.markdown("---")
    st.subheader("📊 Receita por Vendedor")

    df_receita_vendedor = calcular_receita_total_por_vendedor(df_vendas)
    st.bar_chart(df_receita_vendedor.set_index("vendedor"))

    st.markdown("---")
    st.subheader("🏆 Ranking de Vendedores")

    df_ranking = calcular_ranking_vendedores(df_vendas)
    df_ranking["taxa_conversao"] = df_ranking["taxa_conversao"].apply(lambda x: f"{x * 100:.2f}%")

    st.dataframe(df_ranking.style.format({
        "receita": "R$ {:,.2f}",
        "leads_recebidos": "{:,.0f}"
    }))

    st.caption("Fonte: dados tratados da planilha BR_BANK_DANI_KALOI.xlsv")
