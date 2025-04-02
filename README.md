# 📊 Dashboard Tático – BR Bank (Streamlit + Python)

Este projeto entrega um **dashboard tático interativo** desenvolvido em **Streamlit com Python**, voltado para **monitoramento e otimização da jornada do lead até a conversão**, com base em dados históricos extraídos da planilha `BR_BANK_DANI_KALOI.xlsv`.

---

## 🎯 Objetivo do Projeto

Transformar dados de **aquisição, retenção e monetização de leads** em uma **ferramenta digital acessível, estratégica e orientada à ação**, com foco em apoiar decisões rápidas e de alto impacto pelos times de:

- Growth & Marketing
- Vendas
- Produto
- Executivos do BR Bank

O dashboard permite **visualizar gargalos, simular cenários e priorizar ações**, contribuindo diretamente para o atingimento da meta de **R$ 30 milhões de faturamento**.

---

## 🛠️ Tecnologias Utilizadas

| Componente           | Tecnologia              | Observações |
|----------------------|--------------------------|-------------|
| Linguagem Principal  | `Python 3.11+`           | Manipulação, análise e visualização de dados |
| Frontend             | `Streamlit`              | Interface web interativa |
| Visualizações        | `Plotly`, `Altair`       | Gráficos dinâmicos e responsivos |
| Modelagem de dados   | `Pandas`                 | Agregações, KPIs e cálculos |
| Simulações           | `scikit-learn` (Linear Regression) | Projeções e análises de impacto |
| Acessibilidade       | `Custom CSS + Streamlit` | Dark Mode, Contraste, Modo Daltônico |

---

## 🧩 Estrutura de Pastas

```bash
dashboard_br_bank/
│
├── main.py                         # Arquivo principal com navegação
├── config/
│   └── settings.py                # Cores, perfis, temas e configurações globais
├── data/
│   ├── raw/                       # Dados brutos extraídos da planilha
│   ├── processed/                 # Dados tratados para visualização
│   └── loader.py                  # Funções para carregar e preparar dados
├── utils/
│   ├── kpi_calculator.py          # Fórmulas de CAC, ROAS, LTV, etc.
│   ├── simulation.py              # Simuladores e projeções
│   ├── insights_generator.py     # Frases automáticas e alertas
│   └── accessibility.py          # Dark mode, contraste, tamanhos de fonte
├── pages/
│   ├── home.py                    # Guia interativo e seletor de perfil
│   ├── overview.py                # Visão executiva
│   ├── acquisition.py            # Módulo de Aquisição de Leads
│   ├── retention.py              # Módulo de Retenção
│   ├── monetization.py           # Módulo de Monetização
│   ├── projections.py            # Projeções e simuladores
│   ├── analytics.py              # Exploração analítica
│   └── accessibility.py          # Configurações visuais inclusivas
├── assets/
│   ├── icons/                     # Ícones personalizados
│   └── styles.css                 # Estilo customizado e temas visuais
└── README.md                      # Você está aqui 😉
