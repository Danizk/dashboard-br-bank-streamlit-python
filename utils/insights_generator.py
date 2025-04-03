# utils/insights_generator.py
# 📡 Geração dinâmica de insights automáticos para o dashboard do BR Bank

def gerar_insight_conversao(variacao: float) -> str:
    """
    Gera um insight baseado na variação percentual da taxa de conversão.
    """
    if variacao > 0:
        return f"📈 Conversão aumentou em {variacao:.2f}% em relação ao período anterior. Mantenha as estratégias de sucesso!"
    elif variacao < 0:
        return f"📉 Conversão caiu {abs(variacao):.2f}%. Reveja campanhas, abordagem comercial e tempo de resposta."
    else:
        return "🔄 A taxa de conversão manteve-se estável. Busque oportunidades de otimização nos pontos de contato."

def gerar_insight_roas(roas_atual: float) -> str:
    """
    Gera um insight com base no ROAS (Return on Ad Spend).
    """
    if roas_atual >= 500:
        return f"🚀 Excelente desempenho! ROAS atual é de {roas_atual:.2f}%. Os investimentos estão gerando ótimo retorno."
    elif roas_atual >= 300:
        return f"✅ ROAS saudável em {roas_atual:.2f}%. Há espaço para escalar campanhas com melhor performance."
    else:
        return f"⚠️ ROAS abaixo do ideal ({roas_atual:.2f}%). Considere revisar segmentações e criativos com baixo retorno."

def gerar_insight_vendedor(nome: str, crescimento: float) -> str:
    """
    Gera destaque personalizado para vendedores com base na variação de conversão.
    """
    if crescimento > 0:
        return f"🏆 {nome} teve crescimento de {crescimento:.2f}% na conversão nesta semana. Excelente performance!"
    elif crescimento < 0:
        return f"📉 {nome} teve queda de {abs(crescimento):.2f}% na conversão. Ofereça suporte para identificar gargalos."
    else:
        return f"📊 {nome} manteve sua taxa de conversão estável no período. Estabilidade pode ser oportunidade de evolução."

def gerar_insight_ticket(ticket_atual: float, ticket_anterior: float) -> str:
    """
    Gera um insight estratégico sobre a variação no ticket médio.
    """
    diff = ticket_atual - ticket_anterior
    if diff > 0:
        return f"💰 Ticket médio aumentou para R$ {ticket_atual:,.2f}. Isso indica maior potencial de receita por cliente."
    elif diff < 0:
        return f"🧐 Ticket médio caiu para R$ {ticket_atual:,.2f}. Explore estratégias de upsell e bundles."
    else:
        return "📌 Ticket médio está estável. Reforce ações de valor percebido e explore oportunidades de upgrade."
