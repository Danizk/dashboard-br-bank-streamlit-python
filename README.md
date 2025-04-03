# 📊 Dashboard Tático – BR Bank (Streamlit + Python)

Este projeto entrega um **dashboard tático interativo** desenvolvido com **Streamlit** e **Python**, voltado para **monitorar e otimizar a jornada dos leads até a conversão**. Baseia-se nos dados do arquivo `BR_BANK_DANI_KALOI.xlsx`, previamente tratado e convertido em `.csv`.

---

## 🎯 Objetivo do Projeto

Transformar dados de **aquisição, retenção e monetização** em uma ferramenta digital, estratégica e acessível.  
Focado em apoiar decisões rápidas e de alto impacto pelos times de:

- Growth & Marketing
- Vendas
- Produto
- Executivos do BR Bank

---

## ✅ Metas Estratégicas

- Atingir **R$ 30 milhões de faturamento**
- Melhorar taxa de conversão, CAC, ROAS e LTV
- Priorizar leads ativos e otimizar follow-up
- Identificar gargalos por vendedor ou campanha

---

## 🛠️ Tecnologias Utilizadas

| Componente           | Tecnologia         | Observações                                  |
|----------------------|---------------------|-----------------------------------------------|
| Linguagem            | Python 3.11+         | Backend e manipulação de dados                |
| Interface            | Streamlit            | Frontend web interativo e rápido              |
| Gráficos             | Plotly / Altair      | Visualizações responsivas e interativas       |
| Modelagem de Dados   | Pandas               | Cálculo de métricas, filtragem e projeções    |
| Machine Learning     | scikit-learn         | Simuladores com regressão linear              |
| Acessibilidade       | CSS Customizado      | Dark mode, contraste e modo daltônico         |

---

## 📂 Estrutura de Diretórios

```bash
dashboard_br_bank/
├── main.py                       # Navegação principal
├── config/
│   └── settings.py               # Paleta de cores, perfis, temas
├── data/
│   ├── raw/                      # Dados brutos (.csv extraídos do .xlsx)
│   ├── processed/                # Dados tratados para uso
│   └── loader.py                 # Carregamento e cache
├── utils/
│   ├── kpi_calculator.py         # Fórmulas e indicadores
│   ├── simulation.py             # Projeções e simuladores
│   ├── insights_generator.py     # Frases automáticas
│   └── accessibility.py          # Modo escuro, contraste e legibilidade
├── pages/
│   ├── home.py                   # Página inicial
│   ├── overview.py               # Visão executiva geral
│   ├── acquisition.py            # Campanhas e leads captados
│   ├── retention.py              # Retenção e follow-up
│   ├── monetization.py           # Receita, ticket médio e LTV
│   ├── projections.py            # Simulações e metas
│   ├── analytics.py              # Visão exploratória analítica
│   └── accessibility.py          # Configurações visuais
├── assets/
│   ├── icons/                    # Ícones customizados
│   └── styles.css                # Estilo visual do dashboard
└── README.md                     # Documentação geral

▶️ Como Executar Localmente
1. Clone o repositório:

git clone https://github.com/SEU_USUARIO/dashboard-br-bank-streamlit-python.git
cd dashboard-br-bank-streamlit-python

2. Instale as dependências:
pip install -r requirements.txt

3. Rode o Streamlit:
streamlit run main.py


☁️ Deploy no Streamlit Cloud
Acesse em:
https://dashboard-br-bank-final.streamlit.app/

✨ Créditos e Manutenção
Projeto por:
Dani Kaloi 
Contato: linkedin.com/danikaloi

