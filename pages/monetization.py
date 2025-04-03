# pages/monetization.py
# Módulo de Monetização – Receita, Vendas e Ticket Médio

import streamlit as st
import pandas as pd
from utils.kpi_calculator import calcular_ticket_medio, calcular_ltv
from utils.insights_generator import gerar_alerta_meta  # Importando gerador de alerta de meta

def show():
    st.title("💰 Monetização – Receita e Performance Comercial")
    st.markdown("Avalie o desempenho financeiro, ticket médio por cliente e ranking dos vendedores.")

    try:
        # Carregar dados do CRM (contendo informações de vendas e vendedores - conforme Etapa 10)
        df_crm = pd.read_csv("data/crm.csv", parse_dates=['Data da Conversão'])
        # Carregar dados de cálculos consolidados (podendo conter receita total - conforme Etapa 10)
        df_calculos = pd.read_csv("data/calculos.csv")
        # Carregar dicionário de KPIs para acessar a meta (conforme Etapa 10)
        df_kpis = pd.read_csv("data/kpis_e_metricas_.csv")
        meta_receita = df_kpis[df_kpis['KPI'] == 'Meta de Receita']['Valor'].iloc[0] if not df_kpis.empty and ('KPI' in df_kpis.columns and 'Valor' in df_kpis.columns and any(df_kpis['KPI'] == 'Meta de Receita')) else 30000000 # Meta padrão

        # --- KPIs Gerais ---
        receita_total = df_crm['Receita Gerada'].sum() # Assumindo coluna 'Receita Gerada' no CRM
        total_clientes = df_crm['ID_Cliente'].nunique() # Assumindo coluna 'ID_Cliente' no CRM
        ticket_medio = calcular_ticket_medio(receita_total, total_clientes)
        ltv = calcular_ltv(ticket_medio)

        col1, col2, col3 = st.columns(3)
        col1.metric("💵 Receita Total", f"R$ {receita_total:,.2f}")
        col2.metric("🎟️ Ticket Médio", f"R$ {ticket_medio:,.2f}")
        col3.metric("📈 LTV Estimado", f"R$ {ltv:,.2f}")

        # --- Alerta de Meta ---
        st.markdown("---")
        st.subheader("🎯 Meta de Receita")
        alerta_meta = gerar_alerta_meta(meta_receita, receita_total)
        st.info(alerta_meta)

        # --- Receita por Vendedor ---
        st.markdown("---")
        st.subheader("📊 Receita por Vendedor")

        # Agrupar receita por vendedor (assumindo 'Vendedor que atendeu' e 'Receita Gerada' no CRM)
        receita_por_vendedor = df_crm.groupby('Vendedor que atendeu')['Receita Gerada'].sum().sort_values(ascending=False)
        st.bar_chart(receita_por_vendedor)

        # --- Ranking de Vendedores ---
        st.markdown("---")
        st.subheader("🏆 Ranking de Vendedores (Receita)")

        # Calcular número de leads convertidos por vendedor
        leads_convertidos_por_vendedor = df_crm[df_crm['STATUS DO LEAD'] == 'CONVERTIDO']['Vendedor que atendeu'].value_counts().rename('Leads Convertidos')

        # Calcular receita por vendedor (já calculado acima)

        # Criar DataFrame para o ranking
        df_ranking = pd.DataFrame({'Receita': receita_por_vendedor, 'Leads Convertidos': leads_convertidos_por_vendedor}).fillna(0).sort_values(by='Receita', ascending=False)

        st.dataframe(df_ranking.style.format({
            "Receita": "R$ {:,.2f}",
            "Leads Convertidos": "{:,.0f}"
        }))

        st.caption("Fonte: dados do CRM e dicionário de KPIs (BR_BANK_DANI_KALOI.xlsv)")

    except FileNotFoundError:
        st.error("Erro: Um ou mais arquivos de dados necessários não foram encontrados na pasta 'data/'.")
    except KeyError as e:
        st.error(f"Erro: A coluna '{e}' não foi encontrada nos arquivos de dados.")
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
