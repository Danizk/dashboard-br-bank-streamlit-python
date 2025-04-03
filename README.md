# 📊 Dashboard Tático – BR Bank (Streamlit + Python)

Este projeto entrega um **dashboard tático interativo** desenvolvido com **Streamlit + Python**, voltado à **monitoria e otimização da jornada de leads até a conversão**. Alimentado por dados reais da planilha `BR_BANK_DANI_KALOI.xlsx`, o dashboard atende times de **Growth, Vendas, Produto e Executivos**, com indicadores de Aquisição, Retenção e Monetização.

---

## 🎯 Objetivo Estratégico

Transformar dados brutos em insights acionáveis que:
- Identificam gargalos na jornada do cliente
- Ajudam a simular impactos de ações táticas
- Apoiam decisões rápidas com base em dados
- Aceleram o atingimento da meta de **R$ 30 milhões em faturamento**

---

## 🛠️ Tecnologias Utilizadas

| Componente           | Tecnologia              |
|----------------------|--------------------------|
| Backend              | Python 3.11+             |
| Frontend             | Streamlit                |
| Visualizações        | Plotly + Altair          |
| Modelagem de Dados   | Pandas                   |
| Projeções            | scikit-learn             |
| Acessibilidade       | CSS customizado          |

---

## 🧱 Estrutura do Projeto

```bash
dashboard_br_bank/
├── main.py                       # Arquivo principal com roteamento
├── config/
│   └── settings.py              # Configurações globais
├── data/
│   ├── raw/                     # Arquivo original (.xlsx)
│   ├── processed/               # Arquivos .csv prontos
│   └── loader.py                # Funções de ingestão de dados
├── utils/
│   ├── kpi_calculator.py        # KPIs como CAC, ROAS, Ticket Médio etc.
│   ├── simulation.py            # Simuladores de receita e vendedores
│   ├── insights_generator.py   # Geração automática de frases
│   └── accessibility.py        # Dark mode, contraste, daltônico
├── pages/
│   ├── home.py                  # Onboarding e seleção de perfil
│   ├── overview.py              # Visão executiva (ROAS, Receita, CAC)
│   ├── acquisition.py          # Módulo de aquisição
│   ├── retention.py            # Módulo de retenção
│   ├── monetization.py         # Módulo de monetização
│   ├── projections.py          # Simuladores e projeções
│   ├── analytics.py            # Visão exploratória por canal e vendedor
│   └── accessibility.py        # Configurações visuais inclusivas
├── assets/
│   ├── icons/                   # Ícones personalizados
│   └── styles.css               # Tema visual do dashboard
└── README.md
