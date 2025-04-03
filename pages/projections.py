# pages/projections.py
# Módulo de Projeções – Receita Futura e Simuladores

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.simulation import calcular_receita_faltante  # Importando função útil

def show():
    st.title("🚀 Projeções e Potencial de Receita")
    st.markdown("Visualize o caminho até a meta de R$ 30 milhões e simule diferentes cenários de crescimento.")

    try:
        # Carregar dados de cálculos consolidados (podendo conter receita mensal - conforme Etapa 10)
        df_calculos = pd.read_csv("data/calculos.csv", parse_dates=['Data']) # Assumindo coluna 'Data'
        # Carregar dicionário de KPIs para acessar a meta (conforme Etapa 10)
        df_kpis = pd.read_csv("data/kpis_e_metricas_.csv")
        meta_receita = df_kpis[df_kpis['KPI'] == 'Meta de Receita']['Valor'].iloc[0] if not df_kpis.empty and ('KPI' in df_kpis.columns and 'Valor' in df_kpis.columns and any(df_kpis['KPI'] == 'Meta de Receita')) else 30000000 # Meta padrão

        # --- Projeção de Receita Acumulada ---
        st.subheader("📈 Receita Acumulada vs. Meta")

        # Assumindo que df_calculos tem colunas 'Data' e 'Receita'
        df_receita_acumulada = df_calculos.groupby('Data')['Receita'].sum().cumsum().reset_index()
        df_receita_acumulada['Meta'] = meta_receita

        fig = px.line(df_receita_acumulada, x='Data', y=['Receita', 'Meta'],
                      labels={'Receita': 'Receita Acumulada', 'Meta': 'Meta de Receita'},
                      title='Evolução da Receita Acumulada vs. Meta')
        st.plotly_chart(fig, use_container_width=True)

        # --- Receita Faltante ---
        receita_atual = df_receita_acumulada['Receita'].iloc[-1] if not df_receita_acumulada.empty else 0
        receita_faltante = calcular_receita_faltante(meta_receita, receita_atual)
        st.info(f"💰 Faltam **R$ {receita_faltante:,.2f}** para atingir a meta de R$ {meta_receita:,.2f}.")

        st.markdown("---")
        st.subheader("🧪 Simulador: Impacto no Crescimento")
        st.markdown("Explore como diferentes fatores podem influenciar a receita futura.")

        # --- Simulador de Novos Vendedores ---
        st.subheader("➕ Novos Vendedores")
        novos_vendedores = st.slider("Número de vendedores adicionais", min_value=0, max_value=30, value=5)
        # Lógica de simulação (a implementar com base nos dados e modelo de vendas)
        st.info(f"Simulando o impacto de **{novos_vendedores}** novos vendedores na sua equipe.")
        st.warning("⚠️ A lógica de simulação para novos vendedores precisa ser implementada com base nos dados de produtividade e capacidade.")

        # --- Simulador de Melhoria na Conversão ---
        st.subheader("📈 Melhoria na Taxa de Conversão")
        delta_conversao = st.slider("Aumento percentual na taxa de conversão (%)", min_value=0, max_value=20, value=5)
        # Lógica de simulação (a implementar com base nos dados históricos de conversão)
        st.info(f"Simulando um aumento de **{delta_conversao}%** na taxa de conversão.")
        st.warning("⚠️ A lógica de simulação para melhoria na conversão precisa ser implementada com base nos dados do funil e taxas atuais.")

        st.markdown("---")
        st.caption("Fonte: dados históricos e meta definidos no planejamento (BR_BANK_DANI_KALOI.xlsv)")

    except FileNotFoundError:
        st.error("Erro: Os arquivos calculos.csv ou kpis_e_metricas_.csv não foram encontrados na pasta 'data/'.")
    except KeyError as e:
        st.error(f"Erro: A coluna '{e}' não foi encontrada nos arquivos de dados.")
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
