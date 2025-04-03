# 🚀 utils/simulation.py
# Simuladores e projeções para o dashboard tático do BR Bank

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


# 💰 PROJEÇÃO DE RECEITA – Visão Executiva e Projeções
def projetar_receita_semana(df, coluna_data, coluna_receita, n_semanas=4):
    """
    Realiza regressão linear para prever receita semanal.
    
    Args:
        df (pd.DataFrame): Base com colunas de data e receita.
        coluna_data (str): Nome da coluna de datas.
        coluna_receita (str): Nome da coluna com valores de receita.
        n_semanas (int): Número de semanas futuras a projetar.

    Returns:
        pd.DataFrame: Receita real + receita projetada com datas futuras.
    """
    df = df.copy()
    df[coluna_data] = pd.to_datetime(df[coluna_data])
    df = df.groupby(pd.Grouper(key=coluna_data, freq="W"))[coluna_receita].sum().reset_index()
    df["Semana"] = np.arange(len(df))

    # Modelo de regressão
    model = LinearRegression()
    model.fit(df[["Semana"]], df[[coluna_receita]])

    # Geração de projeções
    semanas_futuras = np.arange(len(df), len(df) + n_semanas).reshape(-1, 1)
    receita_futura = model.predict(semanas_futuras)

    df_futuro = pd.DataFrame({
        "Semana": semanas_futuras.flatten(),
        "Receita Projetada": receita_futura.flatten(),
        "Data": pd.date_range(start=df[coluna_data].max() + pd.Timedelta(days=1), periods=n_semanas, freq="W")
    })

    df_real = df.rename(columns={coluna_receita: "Receita Real"})
    return pd.concat([df_real, df_futuro], ignore_index=True)


# 👥 SIMULAÇÃO DE TIME COMERCIAL – Monetização
def simular_receita_com_mais_vendedores(conversao, ticket_medio, leads_por_vendedor, vendedores_atuais, novos_vendedores):
    """
    Simula o impacto de adicionar vendedores no faturamento futuro.

    Returns:
        float: Receita estimada adicional com novos vendedores.
    """
    novos_leads = leads_por_vendedor * novos_vendedores
    novos_clientes = novos_leads * conversao
    receita_adicional = novos_clientes * ticket_medio
    return receita_adicional


# 📈 SIMULAÇÃO DE TAXA DE CONVERSÃO – Retenção
def simular_impacto_conversao(num_leads, taxa_atual, taxa_nova, ticket_medio):
    """
    Simula o ganho de receita com aumento da taxa de conversão.

    Returns:
        dict: Clientes adicionais e receita adicional gerada.
    """
    clientes_atual = num_leads * taxa_atual
    clientes_nova = num_leads * taxa_nova
    delta_clientes = clientes_nova - clientes_atual
    delta_receita = delta_clientes * ticket_medio

    return {
        "clientes_ganhos": delta_clientes,
        "receita_adicional": delta_receita
    }


# 🎯 MONITORAMENTO DE META – Visão Executiva
def calcular_receita_faltante(meta_total, receita_atual):
    """
    Calcula quanto falta para bater a meta de faturamento.

    Returns:
        tuple: (valor restante em R$, percentual da meta atingido)
    """
    restante = meta_total - receita_atual
    percentual = (receita_atual / meta_total) * 100
    return restante, percentual
