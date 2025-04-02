# pages/retention.py
# Módulo de Retenção – Funil, Follow-up e Gargalos

import streamlit as st
import pandas as pd
from config.settings import PALETTE
from utils.kpi_calculator import calcular_taxa_conversao

# Dados simulados para exemplo
df_retencao = pd.read_csv("data/processed/kpis_retencao.csv")

# Métricas globais do funil
visitantes = df_retencao["visitantes"].sum()
leads = df_retencao["leads"].sum()
atendidos = df_retencao["atendidos"].sum()
convertidos = df_retencao["convertidos"].sum()

# Cálculos
taxa_vis_lead = calcular_taxa_conversao(leads, visitantes)
taxa_lead_cliente = calcular_taxa_conversao(convertidos, atendidos)
tempo_medio = df_retencao["tempo_conversao_dias"].mean()

def show():
    st.title("🔁 Retenção de Leads – Funil & Follow-Up")
    st.markdown("Análise da jornada do lead, tempo médio de conversão e principais motivos de perda.")

    col1, col2, col3 = st.columns(3)
    col1.metric("📥 Conversão Visitante → Lead", f"{taxa_vis_lead:.2f}%")
    col2.metric("🎯 Conversão Atendido → Cliente", f"{taxa_lead_cliente:.2f}%")
    col3.metric("⏱️ Tempo médio de conversão", f"{tempo_medio:.1f} dias")

    st.markdown("---")
    st.subheader("📌 Leads Ativos para Follow-up")
    st.write("Segmentados por motivo de perda")

    df_motivos = pd.read_csv("data/processed/motivos_perda.csv")

    st.dataframe(df_motivos.style.format({
        "quantidade": "{:,.0f}",
        "percentual": "{:.2f}%"
    }))

    st.markdown("✅ Use esses dados para reengajar leads com ações direcionadas por motivo.")
    st.caption("Fonte: dados tratados da planilha BR_BANK_DANI_KALOI.xlsv")
