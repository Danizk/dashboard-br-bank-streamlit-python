# 📦 constants.py
# Constantes reutilizáveis no projeto Dashboard BR Bank

# 📁 Caminhos de dados processados
PATHS = {
    "CRM": "data/processed/crm.csv",
    "ADS": "data/processed/dados_consolidados.csv",
    "ANALYTICS": "data/processed/google_analytics.csv",
    "CALCULOS": "data/processed/calculos.csv",
    "CONVERTIDOS": "data/processed/leads_convertidos_trafego_pago_.csv",
    "RELATORIO_ANALITICO": "data/processed/relatorio_analitico_consolidado.csv",
    "KPIS": "data/processed/kpis_e_metricas_.csv"
}

# 📅 Campos de data padrão por base
DATA_FIELDS = {
    "CRM": ["Data do Lead", "Data da Conversão"],
    "ADS": ["Dia"],
    "ANALYTICS": ["Data de Acesso"]
}

# 🧩 Nomes de colunas padronizadas
COLUMNS = {
    "STATUS": "STATUS DO LEAD",
    "VENDEDOR": "Vendedor que atendeu",
    "CANAL": "CANAL_ORIGEM",
    "RECEITA": "Receita Gerada",
    "TEMPO_CONVERSAO": "Tempo até Conversão (Dias)",
    "MOTIVO_PERDA": "Motivo da Perda"
}

# 🎯 Blocos estratégicos do dashboard
BLOCOS_DASHBOARD = [
    "🏠 Home",
    "📊 Visão Executiva",
    "📈 Aquisição de Leads",
    "🔁 Retenção de Leads",
    "💰 Monetização",
    "🚀 Projeções e Receita",
    "🧠 Visão Analítica",
    "♿ Acessibilidade"
]

# 📊 Nomes de KPIs usados em cards e métricas
KPIS_PRINCIPAIS = [
    "Receita Total",
    "Lucro Líquido",
    "ROAS",
    "CAC",
    "Ticket Médio",
    "LTV",
    "Taxa de Conversão",
    "Tempo Médio de Conversão",
    "Leads Ativos para Follow-up"
]

# 🎨 Emojis utilizados como ícones substitutos
ICONS_EMOJIS = {
    "Receita": "💵",
    "Conversão": "✅",
    "Perda": "❌",
    "ROAS": "📢",
    "Ticket Médio": "🎟️",
    "Lead Ativo": "📬",
    "Simulador": "🔮"
}

# ℹ️ Versão e metadados
VERSAO_ATUAL = "1.0"
DESENVOLVIDO_POR = "Growth Analytics Team – BR Bank"
ULTIMA_ATUALIZACAO = "2025-04-03"
