# settings.py
# Configurações globais do dashboard BR Bank

# Paleta de cores acessíveis (modo claro e escuro)
PALETTE = {
    "primary": "#005BA1",
    "secondary": "#00B0F0",
    "success": "#28a745",
    "danger": "#dc3545",
    "warning": "#ffc107",
    "info": "#17a2b8",
    "light": "#f8f9fa",
    "dark": "#343a40"
}

# Perfis de usuário
USER_PROFILES = [
    "Executivo",
    "Growth",
    "Vendas",
    "Produto"
]

# Configurações de fonte
FONT = {
    "family": "Arial",
    "size": {
        "small": 12,
        "medium": 14,
        "large": 18
    }
}

# Modo escuro e contraste
THEME = {
    "dark_mode": True,
    "high_contrast": False,
    "color_blind_mode": False
}
