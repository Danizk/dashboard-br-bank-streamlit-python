# pages/projections.py
# Módulo de Projeções – Receita Futura e Simuladores

import streamlit as st
import pandas as pd
from utils.simulation import (
    projetar_receita_acumulada,
    simular_novos_vendedores,
    simular_melhoria_conversao
)

# Carregamento dos dados processados
df_projecao = pd.read_csv("data/processed/kpis_mensais.csv")

# Parâmetros reais atuais
meta_receita = 30_000_000  # Meta: R$ 30M
clientes_atuais = df_projecao["clientes"].sum()
receita_gerada = df_projecao["receita"].sum()

def show():
    st.title("🚀 Projeções e Potencial de Receita")
    st.markdown("Visualize o caminho até a meta de R$ 30 milhões e simule diferentes cenários de crescimento.")

    # Gráfico de receita acumulada
    st.subheader("📈 Receita Acumulada vs. Meta")
    fig = projetar_receita_acumulada(df_projecao, meta_receita)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("🧪 Simulador: + Vendedores na Equipe")

    novos_vendedores = st.slider("Quantos vendedores adicionais?", min_value=1, max_value=20, value=5)
    receita_proj_vendedores = simular_novos_vendedores(df_projecao, novos_vendedores)

    st.success(f"💼 Com +{novos_vendedores} vendedores, a receita projetada pode chegar a **R$ {receita_proj_vendedores:,.2f}**")

    st.markdown("---")
    st.subheader("🧠 Simulador: Aumento na Taxa de Conversão")

    delta_conversao = st.slider("Melhoria esperada na taxa de conversão (%)", min_value=1, max_value=15, value=5)
    receita_proj_conversao = simular_melhoria_conversao(df_projecao, delta_conversao)

    st.info(f"📊 Com +{delta_conversao}% de conversão, a receita pode alcançar **R$ {receita_proj_conversao:,.2f}**")

    st.markdown("---")
    st.caption("Fonte: dados históricos extraídos da BR_BANK_DANI_KALOI.xlsv")
