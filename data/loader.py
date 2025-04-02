# loader.py
# Funções de ingestão de dados tratados para o dashboard BR Bank

import pandas as pd
import streamlit as st
import os

# Caminho base dos dados processados
DATA_DIR = os.path.join("data", "processed")

@st.cache_data(ttl=3600)  # Cache para otimizar carregamento (1 hora)
def load_csv(filename):
    """
    Carrega um arquivo .csv da pasta de dados processados.
    """
    file_path = os.path.join(DATA_DIR, filename)
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"Arquivo {filename} não encontrado em {DATA_DIR}")
        return pd.DataFrame()

@st.cache_data(ttl=3600)
def load_pickle(filename):
    """
    Carrega um arquivo .pkl (Pickle) da pasta de dados processados.
    """
    file_path = os.path.join(DATA_DIR, filename)
    try:
        df = pd.read_pickle(file_path)
        return df
    except FileNotFoundError:
        st.error(f"Arquivo {filename} não encontrado em {DATA_DIR}")
        return pd.DataFrame()

# Exemplo de uso
if __name__ == "__main__":
    df_kpis = load_csv("kpis_por_vendedor.csv")
    st.write(df_kpis.head())
