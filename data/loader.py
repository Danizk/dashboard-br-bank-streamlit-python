# data/loader.py
# 📦 Carregamento de dados tratados para o Dashboard BR Bank

import pandas as pd
import streamlit as st
import os

# Diretório base
DATA_DIR = "data/processed"

@st.cache_data
def load_csv(filename: str) -> pd.DataFrame:
    """Carrega um arquivo CSV da pasta de dados processados"""
    path = os.path.join(DATA_DIR, filename)
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        st.error(f"❌ Arquivo não encontrado: {filename}")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"⚠️ Erro ao carregar {filename}: {e}")
        return pd.DataFrame()

# Carregamento de arquivos específicos

def load_kpis_gerais():
    return load_csv("kpis_gerais.csv")

def load_tabela_kpis():
    return load_csv("tabela_kpis_gerais.csv")

def load_google_analytics():
    return load_csv("google_analytics.csv")

def load_relatorio_analitico():
    return load_csv("relatório_analítico_consolidado.csv")

def load_kpis():
    return load_csv("kpis.csv")

def load_leads_convertidos():
    return load_csv("leads_convertidos_trafego_pago_.csv")

def load_calculos():
    return load_csv("calculos.csv")

def load_crm():
    return load_csv("crm.csv")

def load_dados_consolidados():
    return load_csv("dados_consolidados.csv")

def load_kpis_metricas():
    return load_csv("kpis_e_metricas_.csv")
