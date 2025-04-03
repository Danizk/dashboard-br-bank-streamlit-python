# utils/insights_generator.py
# Geração de frases automáticas para o dashboard do BR Bank

def gerar_insight_conversao(variacao: float) -> str:
    """
    Gera insight com base na variação da taxa de conversão.
    """
    if variacao > 0:
        return f"📈 A taxa de conversão subiu {variacao:.2f}% em relação ao período anterior. Continue com as boas práticas!"
    elif variacao < 0:
        return f"📉 A taxa de conversão caiu {abs(variacao):.2f}%. Avalie campanhas, follow-ups e abordagem comercial."
    else:
        return "ℹ️ A taxa de conversão permaneceu estável neste período."

def gerar_insight_roas(roas: float) -> str:
    """
    Gera insight baseado no ROAS atual.
    """
    if roas >= 600:
        return f"🚀 ROAS excelente: {roas:.2f}%. Os investimentos estão retornando acima da média!"
    elif roas >= 300:
        return f"✅ ROAS saudável em {roas:.2f}%. Vale explorar oportunidades para escalar."
    else:
        return f"⚠️ ROAS baixo ({roas:.2f}%). Reavalie canais e anúncios com baixa performance."

def gerar_insight_vendedor(nome: str, variacao_conversao: float) -> str:
    """
    Gera frase de destaque sobre o desempenho do vendedor.
    """
    if variacao_conversao > 0:
        return f"🏆 O vendedor {nome} teve um aumento de {variacao_conversao:.2f}% na conversão. Parabéns pelo desempenho!"
    elif variacao_conversao < 0:
        return f"🔻 O vendedor {nome} apresentou uma queda de {abs(variacao_conversao):.2f}% na conversão. Sinal de alerta."
    else:
        return f"📊 O vendedor {nome} manteve a taxa de conversão estável no período."

def gerar_insight_ticket_medio(ticket_atual: float, ticket_anterior: float) -> str:
    """
    Gera insight sobre variação do ticket médio.
    """
    diff = ticket_atual - ticket_anterior
    if diff > 0:
        return f"💰 O ticket médio subiu para R$ {ticket_atual:.2f}. Ótima oportunidade para elevar o LTV!"
    elif diff < 0:
        return f"🧐 O ticket médio caiu para R$ {ticket_atual:.2f}. Avalie oportunidades de upsell."
    else:
        return "📍 O ticket médio permaneceu estável no período."

def gerar_insight_leads_ativos(qtd_leads: int) -> str:
    """
    Gera frase sobre o potencial de reativação dos leads ativos.
    """
    if qtd_leads > 1000:
        return f"🔁 Existem {qtd_leads} leads ativos que ainda podem ser convertidos. Ações de follow-up são recomendadas!"
    elif qtd_leads > 0:
        return f"📞 Há {qtd_leads} leads em aberto. Um bom follow-up pode gerar conversões adicionais."
    else:
        return "✅ Nenhum lead ativo pendente. Excelente trabalho de conversão!"
