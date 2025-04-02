# settings.py
# Configurações globais do dashboard BR Bank

# Paleta de cores acessível (modo claro/escuro e contraste)
PALETTE = {
    "primary": "#005BA1",     # Azul escuro institucional (bom contraste em fundo claro)
    "secondary": "#0072CE",   # Azul médio vibrante (boa legibilidade com branco/preto)
    "success": "#2E8540",     # Verde escuro acessível (substitui o verde padrão para contraste)
    "danger": "#B91C1C",      # Vermelho escuro (alerta crítico, legível sobre claro/escuro)
    "warning": "#F59E0B",     # Amarelo queimado (melhor legibilidade que o amarelo puro)
    "info": "#1C64F2",        # Azul informativo vibrante (ótimo contraste e destaque)
    "light": "#F4F4F5",       # Cinza claro para fundo (modo claro suave, menos brilho)
    "dark": "#1F2937",        # Azul petróleo escuro (para fundo no dark mode)
    "neutral": "#6B7280"      # Texto neutro, cinza médio com bom contraste sobre ambos modos
}

# 👤 Perfis de stakeholders para navegação e visões personalizadas
USER_PROFILES = [
    "Executivo",   # Visão de metas, receita, margem, projeções
    "Growth",      # Aquisição, CAC, ROAS, campanhas
    "Vendas",      # Conversão por vendedor, follow-ups, perdas
    "Produto"      # Retenção, churn, upsell/cross-sell
]

# 🔤 Configurações tipográficas
FONT = {
    "family": "Arial",  # Fonte padrão (web-safe e acessível)
    "size": {
        "small": 12,
        "medium": 14,
        "large": 18
    }
}

# ♿ Preferências de acessibilidade
THEME = {
    "dark_mode": True,           # Modo escuro ativado por padrão
    "high_contrast": False,      # Contraste alto desativado
    "color_blind_mode": False    # Suporte a daltônicos (paleta alternativa pode ser implementada)
}
