# pages/overview.py
# Visão Executiva – Desempenho Financeiro e de Aquisição

import streamlit as st
import pandas as pd
from utils.kpi_calculator import calcular_roas, calcular_cac  # Importando funções específicas
from utils.insights_generator import gerar_alerta_meta, gerar_insight_roas  # Importando geradores de insights

def show(profile):
    st.title("📊 Visão Executiva")
    st.markdown(f"Visão geral de desempenho financeiro e de aquisição — perfil: **{profile}**")

    try:
        # Carregar dados de cálculos consolidados (contendo KPIs gerais - conforme Etapa 10)
        df_calculos = pd.read_csv("data/calculos.csv")
        # Carregar dicionário de KPIs para acessar a meta (conforme Etapa 10)
        df_kpis = pd.read_csv("data/kpis_e_metricas_.csv")
        meta_receita = df_kpis[df_kpis['KPI'] == 'Meta de Receita']['Valor'].iloc[0] if not df_kpis.empty and ('KPI' in df_kpis.columns and 'Valor' in df_kpis.columns and any(df_kpis['KPI'] == 'Meta de Receita')) else 30000000 # Meta padrão

        # --- Recuperar KPIs do DataFrame (Assumindo nomes de colunas) ---
        receita_total = df_calculos['Receita'].sum() # Assumindo 'Receita' total em calculos.csv
        custo_total_vendas = df_calculos['Custo Total Vendas'].sum() # Assumindo coluna de custo total
        clientes_adquiridos = df_calculos['Clientes Adquiridos'].sum() # Assumindo coluna de clientes
        custo_total_ads = df_calculos['Custo Ads'].sum() # Assumindo coluna de custo de ads

        lucro_liquido = df_calculos['Lucro Líquido'].sum() if 'Lucro Líquido' in df_calculos.columns else None
        margem_liquida = df_calculos['Margem Líquida'].mean() if 'Margem Líquida' in df_calculos.columns else None
        roas = calcular_roas(receita_total, custo_total_ads) * 100
        cac = calcular_cac(custo_total_ads, custo_total_vendas, clientes_adquiridos)

        col1, col2, col3 = st.columns(3)
        col1.metric("💵 Receita Total", f"R$ {receita_total:,.2f}")
        if lucro_liquido is not None:
            col2.metric("✅ Lucro Líquido", f"R$ {lucro_liquido:,.2f}")
        else:
            col2.empty()
        if margem_liquida is not None:
            col3.metric("📊 Margem Líquida", f"{margem_liquida:.2f}%")
        else:
            col3.empty()

        col4, col5 = st.columns(2)
        col4.metric("📈 ROAS", f"{roas:.2f}%")
        col5.metric("💰 CAC", f"R$ {cac:,.2f}")

        # --- Alerta de Meta de Receita ---
        st.markdown("---")
        st.subheader("🎯 Meta de Receita")
        alerta_meta = gerar_alerta_meta(meta_receita, receita_total)
        st.info(alerta_meta)

        # --- Insight de ROAS ---
        st.markdown("---")
        st.subheader("💡 Insights de Aquisição")
        insight_roas = gerar_insight_roas(roas)
        st.info(insight_roas)

    except FileNotFoundError:
        st.error("Erro: O arquivo calculos.csv ou kpis_e_metricas_.csv não foi encontrado na pasta 'data/'.")
    except KeyError as e:
        st.error(f"Erro: A coluna '{e}' não foi encontrada no arquivo calculos.csv ou kpis_e_metricas_.csv.")
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
