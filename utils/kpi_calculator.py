# 📈 utils/kpi_calculator.py
# Funções para cálculo dos KPIs essenciais do dashboard do BR Bank

import pandas as pd
import numpy as np

# CAC – Custo de Aquisição de Cliente
# Fórmula: (Custo Ads + Custo Time de Vendas) / Clientes Adquiridos
def calcular_cac(custo_ads, custo_vendas, num_clientes):
    if num_clientes == 0:
        return 0
    return (custo_ads + custo_vendas) / num_clientes

# ROAS – Return on Ad Spend
# Fórmula: Receita / Custo com Ads
def calcular_roas(receita, custo_ads):
    if custo_ads == 0:
        return 0
    return receita / custo_ads

# CPA – Custo por Aquisição de Lead
# Fórmula: Custo Total / Nº de Leads Convertidos
def calcular_cpa(custo_total, num_leads_convertidos):
    if num_leads_convertidos == 0:
        return 0
    return custo_total / num_leads_convertidos

# CPC – Custo por Clique
# Fórmula: Custo / Cliques
def calcular_cpc(custo_total, num_cliques):
    if num_cliques == 0:
        return 0
    return custo_total / num_cliques

# CTR – Click Through Rate
# Fórmula: Cliques / Impressões
def calcular_ctr(cliques, impressoes):
    if impressoes == 0:
        return 0
    return cliques / impressoes

# Taxa de Conversão de Leads → Clientes
# Fórmula: Nº de Clientes / Nº de Leads
def calcular_taxa_conversao(clientes, leads):
    if leads == 0:
        return 0
    return clientes / leads

# Taxa de Conversão de Visitantes → Leads
# Fórmula: Leads / Visitantes
def calcular_conversao_visitantes_para_leads(leads, visitantes):
    if visitantes == 0:
        return 0
    return leads / visitantes

# Ticket Médio
# Fórmula: Receita Total / Nº de Clientes
def calcular_ticket_medio(receita_total, num_clientes):
    if num_clientes == 0:
        return 0
    return receita_total / num_clientes

# LTV – Lifetime Value
# Fórmula: Receita média estimada por cliente no período de 12 meses
def calcular_ltv(ticket_medio, meses=12):
    return ticket_medio * (meses / 12)

# Tempo Médio de Conversão
# Fórmula: Média de dias entre entrada e conversão
def calcular_tempo_medio_conversao(df):
    if df.empty or "Tempo até Conversão (Dias)" not in df.columns:
        return 0
    return df["Tempo até Conversão (Dias)"].mean()

# Receita por Vendedor
# Retorna um DataFrame com somatório por responsável
def calcular_receita_por_vendedor(df):
    if "Vendedor que atendeu" not in df.columns or "Receita Gerada" not in df.columns:
        return pd.DataFrame()
    return df.groupby("Vendedor que atendeu")["Receita Gerada"].sum().reset_index()

# Conversão por Vendedor
# Retorna a taxa de conversão individual
def calcular_conversao_por_vendedor(df):
    if "Vendedor que atendeu" not in df.columns or "STATUS DO LEAD" not in df.columns:
        return pd.DataFrame()
    total = df.groupby("Vendedor que atendeu")["ID_Lead"].count()
    convertidos = df[df["STATUS DO LEAD"] == "CONVERTIDO"].groupby("Vendedor que atendeu")["ID_Lead"].count()
    return (convertidos / total).fillna(0).reset_index(name="Taxa de Conversão")
