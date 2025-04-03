# ⚙️ settings.py
# Configurações globais de estilo, acessibilidade e perfis de usuário do Dashboard BR Bank

# 👤 Perfis de usuário disponíveis
USER_PROFILES = [
    "Executivo",
    "Marketing & Growth",
    "Vendas",
    "Produto"
]

# 🎨 Paleta de Cores Oficial (usada em cards, gráficos, alertas)
COLOR_PALETTE = {
    "primary": "#0043A4",        # Azul BR Bank
    "secondary": "#0061F2",
    "success": "#00B050",        # Verde de performance positiva
    "danger": "#D80027",         # Vermelho de alerta/erro
    "warning": "#FFA800",        # Amarelo de atenção
    "neutral": "#F9F9F9",        # Fundo neutro
    "font": "#333333",           # Cor base para textos
    "light_gray": "#E0E0E0",
    "dark_gray": "#444444",
    "background_dark": "#121212",
    "background_light": "#FFFFFF"
}

# 🌓 Modo Visual
DEFAULT_THEME = "light"  # Opções: "light" ou "dark"

# 🔡 Tamanhos de fonte (padrão visual)
FONT_SIZES = {
    "title": "2rem",
    "subtitle": "1.4rem",
    "normal": "1rem",
    "small": "0.85rem"
}

# ♿ Acessibilidade (modo daltônico, contraste)
ACCESSIBILITY_MODES = {
    "default": {
        "contrast": 1.0,
        "colorblind_safe": False
    },
    "high_contrast": {
        "contrast": 1.4,
        "colorblind_safe": False
    },
    "colorblind": {
        "contrast": 1.2,
        "colorblind_safe": True
    }
}

# 🧱 Layout
LAYOUT = {
    "sidebar_width": 300,
    "max_content_width": 1200
}
