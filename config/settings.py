# 📚 settings.py
# Configurações globais do dashboard BR Bank

# 🎨 Paleta de cores (acessível e compatível com modo claro/escuro)
COLOR_PALETTE = {
    "primary": "#005BBB",     # Azul institucional
    "secondary": "#FFD500",   # Amarelo BR Bank
    "success": "#3BB273",     # Verde para conversões
    "danger": "#E94F37",      # Vermelho para alertas/perdas
    "background": "#FFFFFF",  # Padrão branco (modo claro)
    "text": "#333333"         # Texto padrão
}

# 👤 Perfis de usuário disponíveis no menu inicial
USER_PROFILES = [
    "Executivo",
    "Marketing & Growth",
    "Time de Vendas",
    "Produto"
]

# 🧾 Informações do projeto
PROJECT_METADATA = {
    "name": "Dashboard Tático – BR Bank",
    "version": "1.0",
    "authors": ["Dani Kaloi / Equipe Growth Analytics"],
    "instituicao": "BR Bank",
    "descricao": "Painel interativo para monitoramento de leads e performance comercial"
}

# 🧠 Categorias de motivo de perda padronizadas
MOTIVOS_PADRONIZADOS = [
    "NÃO RETORNOU CONTATO",
    "NÃO TEM INTERESSE",
    "OUTROS",
    "PREÇO ALTO",
    "VAI DEIXAR PARA OUTRO MOMENTO",
    "VAI FECHAR COM A CONCORRÊNCIA"
]

# ♿ Configurações de acessibilidade
ACESSIBILIDADE_CONFIG = {
    "modo_daltônico": True,
    "contraste_automatico": True,
    "dark_mode_default": False
}
