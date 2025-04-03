# 🧠 utils/insights_generator.py
# Geração de insights automáticos e frases analíticas com base nos KPIs do BR Bank

import pandas as pd


def gerar_insight_conversao_atual(taxa_conversao_atual):
    """
    Retorna um comentário com base na taxa de conversão geral de leads para clientes.
    """
    if taxa_conversao_atual > 0.25:
        return f"🚀 Excelente! A taxa de conversão está em {taxa_conversao_atual:.2%}, superando o esperado."
    elif taxa_conversao_atual > 0.20:
        return f"📈 Conversão razoável ({taxa_conversao_atual:.2%}), mas com espaço para otimização."
    else:
        return f"⚠️ Alerta: Conversão baixa ({taxa_conversao_atual:.2%}). Reveja abordagem comercial e jornada."


def gerar_insight_roas(roas):
    """
    Retorna análise do ROAS (Retorno sobre Investimento em Ads).
    """
    if roas > 6:
        return f"💰 ROAS excelente ({roas:.2f}). Campanhas estão com alto retorno sobre investimento!"
    elif roas > 3:
        return f"📊 ROAS positivo ({roas:.2f}). Com potencial para escalar."
    else:
        return f"🔻 ROAS baixo ({roas:.2f}). Avalie segmentações, criativos e canais."


def gerar_insight_vendedor(dados_vendedor: dict):
    """
    Retorna frases personalizadas sobre a performance de um vendedor.
    Exige: nome, conversao, ticket, tempo
    """
    nome = dados_vendedor["nome"]
    conv = dados_vendedor["conversao"]
    ticket = dados_vendedor["ticket"]
    tempo = dados_vendedor["tempo"]

    insights = []

    if conv > 0.25:
        insights.append(f"✅ {nome} tem ótima taxa de conversão ({conv:.2%}).")
    elif conv < 0.22:
        insights.append(f"⚠️ {nome} está abaixo da média ({conv:.2%}).")

    if ticket > 19500:
        insights.append(f"💸 Ticket médio elevado (R$ {ticket:,.2f}).")

    if tempo <= 7:
        insights.append(f"⏱️ Conversão rápida ({tempo} dias).")
    elif tempo > 10:
        insights.append(f"🐢 Conversão lenta ({tempo} dias). Avaliar follow-up.")

    return " ".join(insights)


def gerar_alerta_leads_ativos(leads_ativos):
    """
    Gera alerta com base na quantidade de leads ativos ainda não convertidos ou perdidos.
    """
    if leads_ativos > 1500:
        return f"📌 Existem {leads_ativos} leads ativos. Follow-up precisa de reforço imediato."
    elif leads_ativos > 800:
        return f"🔍 {leads_ativos} leads em aberto. Priorizar por probabilidade de conversão."
    else:
        return f"✅ Leads ativos sob controle ({leads_ativos} leads)."


def gerar_alerta_motivos_perda(df_motivos: pd.DataFrame):
    """
    Identifica o motivo de perda mais frequente a partir de um DataFrame com colunas:
    'Motivo', 'Quantidade'
    """
    motivo_top = df_motivos.sort_values("Quantidade", ascending=False).iloc[0]
    return f"📉 Motivo de perda mais comum: **{motivo_top['Motivo']}** – {motivo_top['Quantidade']} leads."


def gerar_alerta_meta(meta, atual):
    """
    Compara a receita atual com a meta e retorna alerta com avanço e valor restante.
    """
    restante = meta - atual
    percentual = (atual / meta) * 100
    if percentual >= 90:
        return f"🏁 Estamos com {percentual:.1f}% da meta atingida! Faltam apenas R$ {restante:,.2f}."
    elif percentual >= 70:
        return f"🚀 Progresso de {percentual:.1f}%. Restam R$ {restante:,.2f} para a meta de R$ 30M."
    else:
        return f"📊 Avanço atual: {percentual:.1f}%. Ainda faltam R$ {restante:,.2f} para atingir a meta."
