# pages/analytics.py
# Visão Analítica – Exploração Detalhada dos Dados

import streamlit as st
import pandas as pd
import altair as alt

# Dados tratados
df = pd.read_csv("data/processed/leads_tratados.csv")

def show():
    st.title("🧠 Visão Analítica")
    st.markdown("Explore os dados com mais profundidade. Utilize os filtros abaixo para análises personalizadas.")

    # Filtros cruzados
    canal = st.selectbox("🔍 Canal de Aquisição", options=["Todos"] + sorted(df["canal"].unique().tolist()))
    campanha = st.selectbox("📢 Campanha", options=["Todas"] + sorted(df["campanha"].unique().tolist()))
    vendedor = st.selectbox("👤 Vendedor", options=["Todos"] + sorted(df["vendedor"].unique().tolist()))

    # Filtragem condicional
    filtro_df = df.copy()

    if canal != "Todos":
        filtro_df = filtro_df[filtro_df["canal"] == canal]
    if campanha != "Todas":
        filtro_df = filtro_df[filtro_df["campanha"] == campanha]
    if vendedor != "Todos":
        filtro_df = filtro_df[filtro_df["vendedor"] == vendedor]

    st.markdown("### 📈 Evolução Temporal de Leads")
    leads_por_mes = filtro_df.groupby("data_conversao")["lead_id"].count().reset_index()

    chart = alt.Chart(leads_por_mes).mark_line(point=True).encode(
        x="data_conversao:T",
        y="lead_id:Q",
        tooltip=["data_conversao", "lead_id"]
    ).properties(
        width="container",
        height=400
    ).interactive()

    st.altair_chart(chart, use_container_width=True)

    st.markdown("### 📁 Dados Detalhados")
    st.dataframe(filtro_df)

    st.download_button(
        label="⬇️ Exportar para CSV",
        data=filtro_df.to_csv(index=False).encode("utf-8"),
        file_name="leads_analise_personalizada.csv",
        mime="text/csv"
    )

    st.caption("Fonte: dados tratados do BR_BANK_DANI_KALOI.xlsv")
