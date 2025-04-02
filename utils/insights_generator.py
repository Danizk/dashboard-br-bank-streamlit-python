# utils/insights_generator.py
# Geração automática de insights e frases dinâmicas no dashboard do BR Bank

def gerar_insight_conversao(variacao: float) -> str:
    """
    Gera insight com base na variação percentual da taxa de conversão.
    """
    if variacao > 0:
        return f"📈 Conversão aumentou em {variacao:.2f}% em relação ao período anterior. Mantenha as ações que estão dando certo!"
    elif variacao < 0:
        return f"📉 Conversão caiu {abs(variacao):.2f}%. Revise campanhas, argumentos de venda ou tempo de resposta."
    else:
        return "ℹ️ A taxa de conversão permaneceu estável neste período."

def gerar_insight_roas(roas_atual: float) -> str:
    """
    Gera insight com base no ROAS (Retorno sobre Ads).
    """
    if roas_atual >= 500:
        return f"🚀 Excelente! O ROAS atual é {roas_atual:.2f}%. Os investimentos estão performando bem."
    elif roas_atual >= 300:
        return f"✅ ROAS saudável em {roas_atual:.2f}%. Há espaço para otimização e escala."
    else:
        return f"⚠️ Atenção: ROAS abaixo do ideal ({roas_atual:.2f}%). Avalie campanhas com baixo retorno."

def gerar_insight_vendedor(nome: str, crescimento: float) -> str:
    """
    Gera frase de destaque por vendedor com crescimento de performance.
    """
    if crescimento > 0:
        return f"🏆 O vendedor {nome} teve um crescimento de {crescimento:.2f}% na conversão esta semana!"
    elif crescimento < 0:
        return f"🔻 O vendedor {nome} teve uma queda de {abs(crescimento):.2f}% na taxa de conversão. Pode ser hora de oferecer suporte."
    else:
        return f"📊 O vendedor {nome} manteve sua taxa de conversão estável no período."

def gerar_insight_ticket(ticket_atual: float, ticket_anterior: float) -> str:
    """
    Gera insight sobre variação de ticket médio.
    """
    diff = ticket_atual - ticket_anterior
    if diff > 0:
        return f"💰 Ticket médio subiu para R$ {ticket_atual:.2f}. Excelente para aumentar o LTV!"
    elif diff < 0:
        return f"🧐 Ticket médio caiu para R$ {ticket_atual:.2f}. Avalie se há oportunidade de upsell."
    else:
        return "📍 Ticket médio estável no período. Mantenha o foco nos clientes de maior potencial."
