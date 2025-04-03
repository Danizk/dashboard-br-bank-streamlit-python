# config/settings.py
# Configurações globais do Dashboard BR Bank

# Paleta de cores acessível para modo claro e escuro
PALETTE = {
    "primary": "#005BA1",       # Azul institucional
    "secondary": "#0072CE",     # Azul claro vibrante
    "success": "#2E8540",       # Verde escuro (contraste elevado)
    "danger": "#B91C1C",        # Vermelho escuro (alerta)
    "warning": "#F59E0B",       # Amarelo queimado (atenção)
    "info": "#1C64F2",          # Azul para informações
    "light": "#F4F4F5",         # Fundo claro suave
    "dark": "#1F2937",          # Fundo escuro
    "neutral": "#6B7280"        # Cinza neutro para textos e gráficos
}

# Perfis de stakeholders para visualização personalizada
USER_PROFILES = [
    "Executivo",   # Visão estratégica de faturamento e metas
    "Growth",      # KPIs de aquisição, mídia e performance
    "Vendas",      # Conversão, vendedores e motivos de perda
    "Produto"      # Retenção, comportamento e oportunidades de upsell
]

# Tipografia padrão
FONT = {
    "family": "Arial",
    "size": {
        "small": 12,
        "medium": 14,
        "large": 18
    }
}

# Preferências visuais de acessibilidade
THEME = {
    "dark_mode": True,         # Inicia com modo escuro
    "high_contrast": False,    # Contraste alto desabilitado por padrão
    "color_blind_mode": False  # Compatível com visão daltônica
}
