# config/constants.py
# Constantes globais do projeto BR Bank – Central de parâmetros fixos

# 🎯 Metas e Objetivos Estratégicos
META_FATURAMENTO = 30_000_000  # Meta de faturamento (R$)
TAXA_CONVERSAO_META = 0.30     # Meta de conversão de leads
META_TICKET_MEDIO = 19509.79   # Valor atual (base histórica)

# 📅 Intervalo de análise dos dados
PERIODO_INICIAL = "2022-09-01"
PERIODO_FINAL = "2023-02-28"

# 🧬 Públicos-alvo
TIPOS_PUBLICO = ["HOT", "COLD"]

# 📊 Colunas padrão utilizadas em múltiplos módulos
COLUNAS_KPIS = [
    "impressões",
    "cliques",
    "leads",
    "clientes",
    "receita",
    "custo_total",
    "vendedor"
]

# 📌 Motivos de perda padronizados
MOTIVOS_PERDA = [
    "Não retornou contato",
    "Não tem interesse",
    "Outros",
    "Preço alto",
    "Vai deixar para outro momento",
    "Vai fechar com a concorrência"
]

# 🔢 Configurações para simuladores
SIMULACAO_MAX_VENDEDORES = 10
SIMULACAO_VARIACAO_CONVERSAO = [0.01, 0.02, 0.05, 0.10]
