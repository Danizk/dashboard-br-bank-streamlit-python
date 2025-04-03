# pages/overview.py
import streamlit as st
from data.loader import load_kpis_gerais

def show(profile):
    st.title("📊 Visão Executiva")
    st.markdown(f"Visão geral de desempenho financeiro e de aquisição — perfil: **{profile}**")

    df = load_kpis_gerais()

    col1, col2, col3 = st.columns(3)
    col1.metric("Receita Total", f"R$ {df['receita_total'].iloc[0]:,.2f}")
    col2.metric("Lucro Líquido", f"R$ {df['lucro_liquido'].iloc[0]:,.2f}")
    col3.metric("Margem Líquida", f"{df['margem_liquida'].iloc[0]:.2f}%")

    col4, col5 = st.columns(2)
    col4.metric("ROAS", f"{df['roas'].iloc[0]:.2f}%")
    col5.metric("CAC", f"R$ {df['cac'].iloc[0]:,.2f}")
