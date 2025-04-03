# pages/overview.py
# 📊 Visão Executiva - Dashboard BR Bank

import streamlit as st
import pandas as pd
from utils.kpi_calculator import (
    calcular_cac, calcular_roas, calcular_margem_liquida,
    calcular_ticket_medio, calcular_ltv
)
from utils.insights_generator import (
    gerar_insight_conversao, gerar_insight_roas
)
from data.loader import load_kpis_gerais

def show(profile=None):
    st.title("📊 Visão Executiva")
    st.markdown("Resumo estratégico com os principais KPIs financeiros, operacionais e insights de performance.")

    # 🔄 Carregar dados
    df_kpis = load_kpis_gerais()

    # ✅ KPIs principais
    receita_total = df_kpis.at[0, "Receita Total"]
    lucro_liquido = df_kpis.at[0, "Lucro Líquido"]
    custo_total = df_kpis.at[0, "Custo Total de Tráfego Pago"]
    clientes = df_kpis.at[0, "Leads Convertidos"]
    leads = df_kpis.at[0, "Leads Cadastrados no CRM"]
    visitantes = df_kpis.at[0, "Visitantes no site"]
    cliques = df_kpis.at[0, "Cliques nos Anúncios"]
    impressoes = df_kpis.at[0, "Impressões dos Anúncios"]

    # 🧮 KPIs calculados
    cac = calcular_cac(custo_total, clientes)
    roas = calcular_roas(receita_total, custo_total)
    margem = calcular_margem_liquida(lucro_liquido, receita_total)
    ticket = calcular_ticket_medio(receita_total, clientes)
    ltv = calcular_ltv(ticket)
    conversao_leads = round((clientes / leads) * 100, 2)
    conversao_visitantes = round((clientes / visitantes) * 100, 2)

    # 💡 KPIs em colunas
    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Receita Total", f"R$ {receita_total:,.2f}")
    col2.metric("📈 ROAS (%)", f"{roas:.2f}%")
    col3.metric("🏷️ Ticket Médio", f"R$ {ticket:,.2f}")

    col4, col5, col6 = st.columns(3)
    col4.metric("🧮 CAC", f"R$ {cac:,.2f}")
    col5.metric("💹 Margem Líquida", f"{margem:.2f}%")
    col6.metric("🔁 Conversão Leads → Clientes", f"{conversao_leads:.2f}%")

    # 🔍 Insights estratégicos
    st.subheader("📌 Insights Estratégicos")
    st.success(gerar_insight_roas(roas))
    st.info(gerar_insight_conversao(conversao_leads))

    # 📊 Tabela-resumo
    with st.expander("📄 Ver Tabela Resumo de KPIs"):
        st.dataframe(df_kpis.style.format({
            "Receita Total": "R$ {:,.2f}",
            "Lucro Líquido": "R$ {:,.2f}",
            "Custo Total de Tráfego Pago": "R$ {:,.2f}",
            "Ticket Médio": "R$ {:,.2f}",
            "LTV": "R$ {:,.2f}"
        }))

    st.caption("Fonte: BR_BANK_DANI_KALOI.xlsx → Aba: CALCULOS / KPIs")

