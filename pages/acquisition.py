# pages/acquisition.py
# Módulo de Aquisição – Performance de Campanhas e Captação de Leads

import streamlit as st
import pandas as pd
from utils.kpi_calculator import calcular_ctr, calcular_cpa, calcular_roas, calcular_taxa_conversao
from utils.insights_generator import gerar_insight_roas  # Importando gerador de insight

def show():
    st.title("📈 Aquisição de Leads – Performance de Campanhas")
    st.markdown("Métricas e desempenho por canal de mídia (Google Ads, Meta Ads).")

    try:
        # Carregar dados consolidados das campanhas de Ads (conforme Etapa 10)
        df_ads = pd.read_csv("data/dados_consolidados.csv", parse_dates=['DIA'])
        # Carregar dados de cálculos consolidados (conforme Etapa 10)
        df_calculos = pd.read_csv("data/calculos.csv")

        # --- KPIs Gerais ---
        cliques_total = df_ads["Cliques"].sum()
        impressoes_total = df_ads["Impressões"].sum()
        leads_total = df_calculos["Leads"].sum()  # Assumindo coluna 'Leads' em calculos.csv
        investimento_total = df_ads["Custo"].sum()
        receita_total = df_calculos["Receita"].sum()  # Assumindo coluna 'Receita' em calculos.csv

        ctr = calcular_ctr(cliques_total, impressoes_total)
        cpa = calcular_cpa(investimento_total, leads_total)
        roas = calcular_roas(receita_total, investimento_total)
        taxa_conv_lead = calcular_taxa_conversao(leads_total, cliques_total)

        col1, col2, col3 = st.columns(3)
        col1.metric("🖱️ CTR (Click-through Rate)", f"{ctr:.2f}%")
        col2.metric("💰 CPA (Custo por Lead)", f"R$ {cpa:,.2f}")
        col3.metric("📈 ROAS (Retorno sobre Ads)", f"{roas:.2f}%")

        col4, col5 = st.columns(2)
        col4.metric("🧲 Conversão Clique → Lead", f"{taxa_conv_lead:.2f}%")
        col5.metric("🎯 Investimento Total", f"R$ {investimento_total:,.2f}")

        # --- Insight de ROAS ---
        st.markdown("---")
        st.subheader("💡 Insights")
        insight_roas = gerar_insight_roas(roas * 100) # ROAS é geralmente interpretado como %, multiplicamos por 100
        st.info(insight_roas)

        # --- Desempenho por Canal ---
        st.markdown("---")
        st.subheader("📊 Desempenho por Canal")

        # Agrupar dados de Ads por canal (assumindo coluna 'Canal' em dados_consolidados.csv)
        df_canal = df_ads.groupby("CANAL_ORIGEM").agg(
            Impressões=('Impressões', 'sum'),
            Cliques=('Cliques', 'sum'),
            Custo=('Custo', 'sum')
        ).reset_index()

        # Tentar fazer um merge com dados de Leads e Receita por canal (pode exigir ajustes dependendo das colunas)
        df_merged = pd.merge(df_canal, df_calculos, left_on='CANAL_ORIGEM', right_on='CANAL', how='left').fillna(0)

        df_merged['CTR'] = df_merged.apply(lambda row: calcular_ctr(row['Cliques'], row['Impressões']), axis=1)
        df_merged['CPA'] = df_merged.apply(lambda row: calcular_cpa(row['Custo'], row['Leads']), axis=1)
        df_merged['ROAS'] = df_merged.apply(lambda row: calcular_roas(row['Receita'], row['Custo']), axis=1)
        df_merged['Taxa Conv. Lead'] = df_merged.apply(lambda row: calcular_taxa_conversao(row['Leads'], row['Cliques']), axis=1)

        st.dataframe(df_merged[[
            "CANAL_ORIGEM", "Impressões", "Cliques", "Custo", "Leads", "Receita", "CTR", "CPA", "ROAS", "Taxa Conv. Lead"
        ]].style.format({
            "Impressões": "{:,.0f}",
            "Cliques": "{:,.0f}",
            "Leads": "{:,.0f}",
            "Custo": "R$ {:,.2f}",
            "Receita": "R$ {:,.2f}",
            "CTR": "{:.2f}%",
            "CPA": "R$ {:,.2f}",
            "ROAS": "{:.2f}%",
            "Taxa Conv. Lead": "{:.2f}%"
        }))

        st.markdown("---")
        st.caption("Fonte: Dados consolidados das campanhas de Ads e cálculos (BR_BANK_DANI_KALOI.xlsv)")

    except FileNotFoundError:
        st.error("Erro: Os arquivos de dados necessários não foram encontrados na pasta 'data/'.")
    except KeyError as e:
        st.error(f"Erro: A coluna '{e}' não foi encontrada nos arquivos de dados.")
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
