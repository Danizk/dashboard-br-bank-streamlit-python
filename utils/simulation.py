# utils/simulation.py
# Funções para projeção de resultados e simulações táticas

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def simular_receita_adicional(novos_clientes: int, ticket_medio: float) -> float:
    """Calcula receita potencial ao adicionar novos clientes"""
    return round(novos_clientes * ticket_medio, 2)

def simular_novos_clientes_por_vendedor(leads_por_vendedor: int, taxa_conversao: float) -> int:
    """Estima número de clientes com base em novos leads atribuídos por vendedor"""
    return int((leads_por_vendedor * taxa_conversao) / 100)

def estimar_impacto_novo_vendedor(media_leads_atual: int, n_vendedores: int, total_leads: int, taxa_conversao: float, ticket_medio: float):
    """
    Simula o impacto de contratar mais 1 vendedor:
    - Redução da carga média
    - Aumento estimado de clientes e receita
    """
    novo_total_vendedores = n_vendedores + 1
    nova_media_leads = total_leads / novo_total_vendedores
    novos_clientes = simular_novos_clientes_por_vendedor(nova_media_leads, taxa_conversao)
    receita_estimativa = simular_receita_adicional(novos_clientes, ticket_medio)
    return {
        "nova_media_leads": round(nova_media_leads, 2),
        "clientes_estimados": novos_clientes,
        "receita_projetada": receita_estimativa
    }

def prever_crescimento_linear(dados: pd.DataFrame, coluna_data: str, coluna_valor: str, passos: int = 4) -> pd.DataFrame:
    """
    Projeta crescimento com base em regressão linear simples.
    - `coluna_data` deve estar em formato datetime ou contínuo
    - `coluna_valor` é a métrica a ser projetada
    """
    df = dados.copy()
    df = df.dropna(subset=[coluna_data, coluna_valor])
    df[coluna_data] = pd.to_datetime(df[coluna_data])
    df.sort_values(by=coluna_data, inplace=True)
    df["dias"] = (df[coluna_data] - df[coluna_data].min()).dt.days
    X = df[["dias"]]
    y = df[coluna_valor]
    
    modelo = LinearRegression()
    modelo.fit(X, y)
    
    futuros_dias = np.arange(X["dias"].max() + 1, X["dias"].max() + passos + 1).reshape(-1, 1)
    previsoes = modelo.predict(futuros_dias)

    datas_futuras = [df[coluna_data].max() + pd.Timedelta(days=i) for i in range(1, passos + 1)]
    df_resultado = pd.DataFrame({
        coluna_data: datas_futuras,
        "previsao_" + coluna_valor: previsoes.round(2)
    })
    return df_resultado
