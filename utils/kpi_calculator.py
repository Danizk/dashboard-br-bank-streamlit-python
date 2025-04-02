# utils/kpi_calculator.py
# Cálculo dos principais KPIs do dashboard tático do BR Bank

import pandas as pd

def calcular_ctr(impressões: int, cliques: int) -> float:
    """
    Calcula o Click-through Rate (CTR).
    Fórmula: (Cliques / Impressões) * 100
    """
    return round((cliques / impressões) * 100, 2) if impressões else 0.0

def calcular_cpa(custo_total: float, total_leads: int) -> float:
    """
    Calcula o Custo por Aquisição de Lead (CPA).
    Fórmula: Custo Total / Total de Leads
    """
    return round(custo_total / total_leads, 2) if total_leads else 0.0

def calcular_cac(custo_total: float, clientes_convertidos: int) -> float:
    """
    Calcula o Custo de Aquisição de Cliente (CAC).
    Fórmula: Custo Total / Total de Clientes Convertidos
    """
    return round(custo_total / clientes_convertidos, 2) if clientes_convertidos else 0.0

def calcular_roas(receita: float, investimento: float) -> float:
    """
    Calcula o Retorno sobre Investimento em Anúncios (ROAS).
    Fórmula: Receita / Investimento * 100
    """
    return round((receita / investimento) * 100, 2) if investimento else 0.0

def calcular_taxa_conversao(parcial: int, total: int) -> float:
    """
    Calcula uma taxa de conversão genérica.
    Fórmula: (Parcial / Total) * 100
    """
    return round((parcial / total) * 100, 2) if total else 0.0

def calcular_ticket_medio(receita_total: float, total_clientes: int) -> float:
    """
    Calcula o Ticket Médio por cliente.
    Fórmula: Receita Total / Número de Clientes
    """
    return round(receita_total / total_clientes, 2) if total_clientes else 0.0

def calcular_ltv(ticket_medio: float, tempo_medio_meses: int = 1) -> float:
    """
    Calcula o Lifetime Value (LTV).
    Fórmula: Ticket Médio * Tempo Médio de Relacionamento (meses)
    """
    return round(ticket_medio * tempo_medio_meses, 2)

def calcular_margem_liquida(lucro_liquido: float, receita: float) -> float:
    """
    Calcula a Margem Líquida.
    Fórmula: Lucro Líquido / Receita * 100
    """
    return round((lucro_liquido / receita) * 100, 2) if receita else 0.0

def calcular_receita_total_por_vendedor(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa e soma a receita por vendedor.
    """
    return df.groupby("vendedor")["receita"].sum().reset_index()

def calcular_taxa_perda_por_motivo(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula a distribuição percentual de motivos de perda de leads.
    """
    motivos = df['motivo_perda'].value_counts(normalize=True) * 100
    return motivos.round(2).reset_index().rename(columns={'index': 'motivo', 'motivo_perda': 'percentual'})

def calcular_ranking_vendedores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Gera ranking de vendedores com base em:
    - Receita total
    - Total de leads recebidos
    - Taxa de conversão
    """
    return df.groupby('vendedor').agg({
        'receita': 'sum',
        'lead_id': 'count',
        'conversao': 'mean'
    }).reset_index().rename(columns={
        'lead_id': 'leads_recebidos',
        'conversao': 'taxa_conversao'
    }).sort_values(by='receita', ascending=False)
