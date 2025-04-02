# utils/simulation.py
# Funções para simulações e projeções no dashboard do BR Bank

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 📈 Projeção de Receita com base em Regressão Linear
def projetar_receita(data: pd.DataFrame, dias_proj: int = 30) -> pd.DataFrame:
    """
    Projeta a receita futura com base em dados históricos usando regressão linear.
    Parâmetros:
        data: DataFrame com colunas ['data', 'receita']
        dias_proj: número de dias a projetar no futuro
    Retorno:
        DataFrame com datas futuras e receita projetada
    """
    df = data.copy()
    df["dias"] = (pd.to_datetime(df["data"]) - pd.to_datetime(df["data"].min())).dt.days
    X = df[["dias"]]
    y = df["receita"]

    model = LinearRegression()
    model.fit(X, y)

    dias_futuros = np.arange(df["dias"].max() + 1, df["dias"].max() + dias_proj + 1)
    datas_futuras = pd.date_range(start=df["data"].max(), periods=dias_proj + 1, freq="D")[1:]
    receita_proj = model.predict(dias_futuros.reshape(-1, 1))

    return pd.DataFrame({
        "data": datas_futuras,
        "receita_projetada": receita_proj
    })


# 👥 Simulador: Adição de Vendedores
def simular_novos_vendedores(leads_por_vendedor: int, taxa_conversao: float, ticket_medio: float, n_vendedores: int = 1) -> float:
    """
    Simula o impacto financeiro da adição de vendedores.
    Retorno:
        Receita potencial gerada com os novos vendedores
    """
    leads_total = leads_por_vendedor * n_vendedores
    novos_clientes = leads_total * (taxa_conversao / 100)
    receita_simulada = novos_clientes * ticket_medio
    return round(receita_simulada, 2)


# 🚀 Simulador: Aumento da Taxa de Conversão
def simular_aumento_conversao(leads_totais: int, taxa_atual: float, taxa_nova: float, ticket_medio: float) -> float:
    """
    Compara receita entre a taxa atual e uma taxa de conversão aumentada.
    """
    clientes_atuais = leads_totais * (taxa_atual / 100)
    clientes_projetados = leads_totais * (taxa_nova / 100)
    receita_diff = (clientes_projetados - clientes_atuais) * ticket_medio
    return round(receita_diff, 2)
