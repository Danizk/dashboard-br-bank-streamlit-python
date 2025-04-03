# pages/analytics.py
# Visão Analítica – Exploração Detalhada dos Dados

import streamlit as st
import pandas as pd
import altair as alt

def show():
    st.title("🧠 Visão Analítica")
    st.markdown("Explore os dados com mais profundidade. Utilize os filtros abaixo para análises personalizadas.")

    try:
        # Carregar dados do CRM (conforme Etapa 10)
        df_crm = pd.read_csv("data/crm.csv", parse_dates=['Data do Lead', 'Data da Conversão'])

        st.sidebar.header("Filtros")

        # Filtros cruzados na barra lateral
        canal = st.sidebar.selectbox("🔍 Canal de Aquisição", options=["Todos"] + sorted(df_crm["CANAL_ORIGEM"].unique().tolist()))
        campanha = st.sidebar.selectbox("📢 Campanha", options=["Todas"] + sorted(df_crm["Nome da Campanha"].unique().tolist())) # Assumindo nome da coluna
        vendedor = st.sidebar.selectbox("👤 Vendedor", options=["Todos"] + sorted(df_crm["Vendedor que atendeu"].unique().tolist())) # Assumindo nome da coluna
        status_lead = st.sidebar.multiselect("🚦 Status do Lead", options=sorted(df_crm["STATUS DO LEAD"].unique().tolist()))

        # Filtragem condicional
        filtro_df = df_crm.copy()

        if canal != "Todos":
            filtro_df = filtro_df[filtro_df["CANAL_ORIGEM"] == canal]
        if campanha != "Todas":
            filtro_df = filtro_df[filtro_df["Nome da Campanha"] == campanha]
        if vendedor != "Todos":
            filtro_df = filtro_df[filtro_df["Vendedor que atendeu"] == vendedor]
        if status_lead:
            filtro_df = filtro_df[filtro_df["STATUS DO LEAD"].isin(status_lead)]

        st.markdown(f"### 📈 Evolução Temporal de Leads (Total de {len(filtro_df)} registros)")
        # Agrupar por mês de criação do lead (assumindo 'Data do Lead')
        filtro_df['mes_lead'] = pd.to_datetime(filtro_df['Data do Lead']).dt.to_period('M')
        leads_por_mes = filtro_df.groupby("mes_lead")["ID_Lead"].count().reset_index()
        leads_por_mes['mes_lead'] = leads_por_mes['mes_lead'].astype(str) # Converter para string para o Altair

        chart = alt.Chart(leads_por_mes).mark_line(point=True).encode(
            x=alt.X("mes_lead:T", title="Mês"),
            y=alt.Y("ID_Lead:Q", title="Número de Leads"),
            tooltip=["mes_lead", "ID_Lead"]
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

        st.caption("Fonte: dados do CRM (BR_BANK_DANI_KALOI.xlsv)")

    except FileNotFoundError:
        st.error("Erro: O arquivo crm.csv não foi encontrado na pasta 'data/'.")
    except KeyError as e:
        st.error(f"Erro: A coluna '{e}' não foi encontrada no arquivo crm.csv.")
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
