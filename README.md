# 📊 Dashboard Tático – BR Bank (Streamlit + Python)

Este projeto entrega um **dashboard tático interativo** desenvolvido em **Streamlit com Python**, voltado para o **monitoramento e otimização da jornada do lead até a conversão**, com base em dados históricos extraídos da planilha `BR_BANK_DANI_KALOI.xlsv`.

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

| Componente           | Tecnologia              | Observações                                         |
|----------------------|--------------------------|-----------------------------------------------------|
| Linguagem Principal  | Python 3.11+             | Manipulação, análise e visualização de dados        |
| Frontend             | Streamlit                | Interface web interativa                            |
| Visualizações        | Plotly, Altair           | Gráficos dinâmicos e responsivos                    |
| Modelagem de dados   | Pandas                   | Agregações, KPIs e cálculos                         |
| Simulações           | scikit-learn             | Projeções e análises de impacto                     |
| Acessibilidade       | CSS Customizado          | Dark Mode, Contraste, Modo Daltônico                |

---

## 📂 Estrutura de Pastas

```bash
dashboard_br_bank/
├── main.py                       # Arquivo principal com navegação
├── config/
│   └── settings.py              # Configurações globais
├── data/
│   ├── raw/                     # Dados brutos extraídos da planilha
│   ├── processed/               # Dados tratados
│   └── loader.py                # Funções de ingestão
├── utils/
│   ├── kpi_calculator.py        # Cálculos dos KPIs
│   ├── simulation.py            # Projeções e simuladores
│   ├── insights_generator.py   # Frases automáticas
│   └── accessibility.py        # Funções de acessibilidade
├── pages/
│   ├── home.py                  # Página inicial
│   ├── overview.py              # Visão Executiva
│   ├── acquisition.py          # Módulo de Aquisição
│   ├── retention.py            # Módulo de Retenção
│   ├── monetization.py         # Módulo de Monetização
│   ├── projections.py          # Projeções e Simuladores
│   ├── analytics.py            # Visão Analítica
│   └── accessibility.py        # Configurações de acessibilidade
├── assets/
│   ├── icons/                   # Ícones customizados
│   └── styles.css               # Estilo visual do dashboard
└── README.md                    # Este arquivo 🙂

📦 Instalação Local
# Clone o repositório
git clone https://github.com/danikaloi/dashboard-br-bank-streamlit-python.git
cd dashboard-br-bank-streamlit-python

# (Opcional) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o dashboard
streamlit run main.py

🚀 Funcionalidades Principais
📈 Visão Executiva com KPIs estratégicos (Receita, ROAS, CAC, Lucro)

📊 Aquisição de Leads com análise de campanhas (CTR, CPA, ROAS)

🔁 Retenção com funil completo e motivos de perda por vendedor

💰 Monetização com desempenho comercial por vendedor

🚀 Projeções e Simulações de metas e ações táticas

🧠 Insights automáticos com base em variações de KPIs

♿ Acessibilidade Total: modo daltônico, dark mode e alto contraste

🔐 Deploy
Este dashboard está publicado via Streamlit Cloud:

https://share.streamlit.io

O link de acesso (exemplo):

https://br-bank-growth-dashboard.streamlit.app

📄 Licença
(A definir)
Este projeto ainda não possui uma licença pública definida. Sugestões: MIT, Apache 2.0, GPLv3.

🤝 Contribuições
Contribuições são bem-vindas!
Se desejar colaborar com novas funcionalidades ou correções, abra uma issue ou envie um pull request.

👤 Responsável Técnico
Dani Kaloi
Growth & Analytics Lead – BR Bank
🔗 https://www.linkedin.com/in/danikaloi/

Este projeto faz parte de uma estratégia de crescimento orientada por dados. Ele transforma dados dispersos em inteligência prática para times de performance, vendas e produto.
