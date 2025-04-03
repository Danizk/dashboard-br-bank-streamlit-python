# pages/retention.py
# Módulo de Retenção – Funil, Follow-up e Gargalos

import streamlit as st
import pandas as pd
from utils.kpi_calculator import calcular_taxa_conversao
from utils.insights_generator import gerar_insight_tempo_conversao, gerar_tabela_motivos_perda # Importando geradores de insights

def show():
    st.title("🔁 Retenção de Leads – Funil & Follow-Up")
    st.markdown("Análise da jornada do lead, tempo médio de conversão e principais motivos de perda.")

    try:
        # Carregar dados do CRM (contendo informações do funil e tempo de conversão - conforme Etapa 10)
        df_crm = pd.read_csv("data/crm.csv", parse_dates=['Data do Lead', 'Data da Conversão'])
        # Carregar dados de cálculos consolidados (podendo conter informações agregadas do funil - conforme Etapa 10)
        df_calculos = pd.read_csv("data/calculos.csv")

        # --- Métricas Globais do Funil ---
        visitantes = df_calculos['Visitantes'].sum() if 'Visitantes' in df_calculos.columns else 0 # Assumindo coluna em calculos.csv
        leads = df_calculos['Leads'].sum() if 'Leads' in df_calculos.columns else 0 # Assumindo coluna em calculos.csv
        atendidos = df_crm[df_crm['STATUS DO LEAD'] != 'Não Contatado']['ID_Lead'].nunique() if 'STATUS DO LEAD' in df_crm.columns else 0 # Assumindo status
        convertidos = df_crm[df_crm['STATUS DO LEAD'] == 'CONVERTIDO']['ID_Lead'].nunique() if 'STATUS DO LEAD' in df_crm.columns else 0 # Assumindo status

        # --- Cálculos ---
        taxa_vis_lead = calcular_taxa_conversao(leads, visitantes)
        taxa_lead_cliente = calcular_taxa_conversao(convertidos, atendidos)
        tempo_medio = (df_crm['Data da Conversão'] - df_crm['Data do Lead']).dt.days.mean() if ('Data da Conversão' in df_crm.columns and 'Data do Lead' in df_crm.columns) else 0

        col1, col2, col3 = st.columns(3)
        col1.metric("📥 Conversão Visitante → Lead", f"{taxa_vis_lead:.2f}%")
        col2.metric("🎯 Conversão Atendido → Cliente", f"{taxa_lead_cliente:.2f}%")
        col3.metric("⏱️ Tempo médio de conversão", f"{tempo_medio:.1f} dias")

        # --- Insight de Tempo Médio de Conversão ---
        st.markdown("---")
        st.subheader("💡 Insights")
        insight_tempo = gerar_insight_tempo_conversao(tempo_medio)
        st.info(insight_tempo)

        # --- Leads Ativos para Follow-up e Motivos de Perda ---
        st.markdown("---")
        st.subheader("💔 Motivos de Perda")
        st.write("Análise dos principais motivos pelos quais leads não foram convertidos.")

        # Gerar tabela de motivos de perda usando função do utils
        df_motivos_perda = gerar_tabela_motivos_perda(df_crm)
        st.dataframe(df_motivos_perda.style.format({"Percentual": "{:.2f}%"}))

        st.markdown("✅ Use esses dados para refinar abordagens e identificar oportunidades de melhoria.")
        st.caption("Fonte: dados do CRM e cálculos (BR_BANK_DANI_KALOI.xlsv)")

    except FileNotFoundError:
        st.error("Erro: Os arquivos crm.csv ou calculos.csv não foram encontrados na pasta 'data/'.")
    except KeyError as e:
        st.error(f"Erro: A coluna '{e}' não foi encontrada nos arquivos de dados.")
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
