# data/loader.py
# Funções para carregar os dados do BR Bank (pré-processados)

import pandas as pd
import os
from pathlib import Path

# Caminho base para os arquivos CSV processados
DATA_DIR = Path("data/processed")

@st.cache_data
def load_csv(filename: str) -> pd.DataFrame:
    """
    Carrega um arquivo CSV da pasta data/processed/ com cache.
    """
    filepath = DATA_DIR / filename
    if not filepath.exists():
        st.error(f"Arquivo não encontrado: {filepath}")
        return pd.DataFrame()
    
    df = pd.read_csv(filepath)
    return df


def load_all_data():
    """
    Carrega todos os datasets essenciais do projeto.
    """
    return {
        "kpis": load_csv("kpis.csv"),
        "crm": load_csv("crm.csv"),
        "calculos": load_csv("calculos.csv"),
        "consolidados": load_csv("dados_consolidados.csv"),
        "leads_convertidos": load_csv("leads_convertidos_trafego_pago.csv"),
        "analytics": load_csv("google_analytics.csv"),
        "relatorio": load_csv("relatório_analítico_consolidado.csv"),
        "kpis_e_metricas": load_csv("kpis_e_metricas_.csv")
    }
