# 📊 Dashboard Tático BR Bank

## 🎯 Descrição

Este é um dashboard interativo construído com Streamlit e Python para acompanhar e otimizar a jornada do lead até a conversão, visando atingir R$ 30 milhões em receita até o final de 2023. O dashboard se baseia no framework de **Aquisição, Retenção e Monetização**, oferecendo insights e ferramentas para a tomada de decisões estratégicas.

## 📂 Estrutura do Projeto

dashboard-br-bank-streamlit-python/
├── pages/
│   ├── aquisicao.py
│   ├── monetizacao.py
│   └── retencao.py
├── utils/
│   ├── accessibility.py
│   ├── insights_generator.py
│   ├── kpi_calculator.py
│   └── simulation.py
└── main.py
└── README.md


O diretório `utils/` contém módulos com funcionalidades específicas para o dashboard:

* `accessibility.py`: Funções para melhorar a acessibilidade visual do dashboard, incluindo opções de dark mode, alto contraste e ajuste de tamanho de fonte.
* `insights_generator.py`: Contém funções para gerar insights automáticos e alertas textuais com base nos valores dos KPIs, facilitando a interpretação dos dados.
* `kpi_calculator.py`: Contém funções para calcular os principais indicadores de desempenho (KPIs) do dashboard, utilizando fórmulas específicas para cada métrica.
* `simulation.py`: Contém funções para realizar projeções de receita (usando regressão linear) e simulações de cenários (como o impacto de aumentar o time de vendas ou a taxa de conversão).
* O diretório `pages/` conterá as diferentes seções do dashboard (Aquisição, Monetização, Retenção).
* `main.py` é o ponto de entrada da aplicação Streamlit.

## ⚙️ Pré-requisitos

* Python 3.x
* Streamlit (`pip install streamlit`)
* Pandas (`pip install pandas`)
* NumPy (`pip install numpy`)
* Scikit-learn (`pip install scikit-learn`)

## 🛠️ Instalação

1.  Clone o repositório:
    ```bash
    git clone [URL_DO_SEU_REPOSITÓRIO]
    cd dashboard-br-bank-streamlit-python
    ```
2.  (Opcional) Crie um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate  # No Windows
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt # Se você tiver um arquivo requirements.txt
    # Caso contrário, instale individualmente:
    pip install streamlit pandas numpy scikit-learn
    ```

## ▶️ Como Executar

1.  Navegue até o diretório raiz do projeto (`dashboard-br-bank-streamlit-python`).
2.  Execute o seguinte comando no terminal:
    ```bash
    streamlit run main.py
    ```
3.  O dashboard será aberto automaticamente no seu navegador web.

## 📄 Arquivos Principais

* **`main.py`:** Arquivo principal que inicializa a aplicação Streamlit e define a estrutura do dashboard.
* **`pages/aquisicao.py`:** Seção do dashboard focada nas métricas e KPIs de Aquisição (Visitantes, Leads, CAC, CTR, CPC, ROAS, Taxa de Conversão de Visitantes → Leads, Taxa de Conversão de Leads → Clientes).
* **`pages/monetizacao.py`:** Seção do dashboard focada nas métricas e KPIs de Monetização (Receita por Vendedor, Ticket Médio, LTV). Inclui também simulações do impacto de novos vendedores e ferramentas para monitorar a meta de receita.
* **`pages/retencao.py`:** Seção do dashboard focada nas métricas e KPIs de Retenção (Tempo Médio de Conversão, Leads Ativos, Motivos de Perda, Conversão Média por Vendedor).
* **`utils/accessibility.py`:** Contém funções para aplicar temas de dark mode e alto contraste, além de ajustar o tamanho da fonte, visando melhorar a experiência de usuários com diferentes necessidades de acessibilidade visual.
* **`utils/insights_generator.py`:** Implementa funções para analisar os KPIs calculados e gerar automaticamente insights textuais e alertas, como a análise da taxa de conversão geral, o desempenho do ROAS, a performance individual de vendedores, o status dos leads ativos e os principais motivos de perda. Também monitora o progresso em relação à meta de receita de R$ 30 milhões.
* **`utils/kpi_calculator.py`:** Fornece funções para calcular uma variedade de KPIs essenciais, incluindo CAC, ROAS, CPA, CPC, CTR, taxas de conversão (visitantes para leads e leads para clientes), ticket médio, LTV, tempo médio de conversão, receita por vendedor e taxa de conversão por vendedor.
* **`utils/simulation.py`:** Oferece ferramentas para realizar projeções de receita semanal utilizando regressão linear, simular o impacto no faturamento ao adicionar novos vendedores e estimar o ganho de receita com o aumento da taxa de conversão. Também inclui uma função para calcular a receita restante para atingir a meta estabelecida.

## 💡 Uso

Ao executar o dashboard, utilize a barra lateral para navegar entre as seções de Aquisição, Monetização e Retenção. Cada seção apresentará visualizações de dados, KPIs calculados e insights gerados automaticamente. Interaja com os filtros e seletores para explorar os dados em detalhes. A seção de Monetização permitirá realizar simulações para entender o potencial de crescimento com diferentes estratégias. A funcionalidade de acessibilidade pode ser encontrada em um menu ou controles dedicados, permitindo personalizar a visualização conforme suas preferências.

## ⏭️ Próximos Passos

* Integrar a conexão com as fontes de dados do BR Bank para alimentar o dashboard com informações atualizadas.
* Desenvolver visualizações de dados (gráficos, tabelas) em cada uma das páginas (`aquisicao.py`, `monetizacao.py`, `retencao.py`) para apresentar os KPIs e insights de forma clara e eficaz.
* Implementar os controles de interatividade (filtros, seletores de período, etc.) para permitir a análise exploratória dos dados.
* Refinar a interface do usuário e a experiência geral do dashboard.
* Realizar testes de usabilidade com os stakeholders do BR Bank para garantir que o dashboard atenda às suas necessidades.
* Documentar detalhadamente o código e a arquitetura do dashboard.
