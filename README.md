# 📊 Dashboard Tático – BR Bank (Streamlit + Python)

Este projeto entrega um **dashboard tático interativo** desenvolvido com **Streamlit + Python**, projetado para **monitorar e otimizar toda a jornada de leads até a conversão no BR Bank**, com foco em aquisição, retenção e monetização.

---

## 🎯 Objetivo do Projeto

Transformar dados de múltiplas fontes em uma **plataforma visual e estratégica** de apoio à decisão.  
O dashboard oferece visões específicas para cada área do BR Bank:

- 📈 Executivos: Visão consolidada de faturamento, ROI e metas
- 📣 Marketing & Growth: Análise de canais, CAC, ROAS e funil de aquisição
- 📞 Vendas: Performance de vendedores, follow-ups e gargalos
- 🧠 Produto: Retenção, jornada do cliente e oportunidades de LTV

---

## ✅ Metas Estratégicas do Projeto

- Atingir **R$ 30 milhões de faturamento**
- Reduzir o **CAC** e aumentar o **ROAS**
- Aumentar a taxa de conversão geral e por vendedor
- Rastrear e priorizar **leads ativos para follow-up**
- Apoiar a tomada de decisões baseadas em dados (data-driven)

---

## 📌 Etapas do Projeto (10 fases concluídas)

1. **Briefing Estratégico**  
2. **Diagnóstico dos Dados**  
3. **Definição de KPIs e Métricas**  
4. **Modelagem de Dados (ETL local)**  
5. **Design UX/UI do Dashboard**  
6. **Desenvolvimento Técnico com Streamlit**  
7. **Deploy na Nuvem e Publicação no GitHub**  
8. **Validação com Stakeholders**  
9. **Manutenção e Evolução Contínua**  
10. **Estrutura Final da Base em CSV**

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
├── main.py                       # Navegação principal (roteador Streamlit)
├── config/
│   └── settings.py               # Paleta de cores, perfis, temas visuais
├── data/
│   ├── raw/                      # Arquivos .csv brutos
│   ├── processed/                # Bases limpas e prontas para ingestão
│   └── loader.py                 # Funções para carregamento com cache
├── utils/
│   ├── kpi_calculator.py         # Fórmulas de KPIs (CAC, ROAS, etc.)
│   ├── simulation.py             # Projeções e simuladores de crescimento
│   ├── insights_generator.py     # Frases automáticas com base em tendências
│   └── accessibility.py          # Modo escuro, contraste, fonte adaptável
├── pages/
│   ├── home.py                   # Onboarding e seletor de perfil
│   ├── overview.py               # Visão Executiva de Alto Nível
│   ├── acquisition.py            # Performance de campanhas e CAC
│   ├── retention.py              # Gargalos, perdas e leads ativos
│   ├── monetization.py           # Receita, LTV, ticket médio
│   ├── projections.py            # Caminho até os R$30M
│   ├── analytics.py              # Visão analítica detalhada
│   └── accessibility.py          # Configurações de acessibilidade
├── assets/
│   ├── icons/                    # Ícones personalizados
│   └── styles.css                # Tema visual customizado
└── README.md                     # Documentação do projeto
📈 Bases de Dados (.CSV)
Baseadas no arquivo original BR_BANK_DANI_KALOI.xlsx, convertido e limpo:

calculos.csv → Indicadores derivados, KPIs e somatórios

crm.csv → Funil de leads, conversão e perdas

dados_consolidados.csv → Campanhas de Ads (Google & Meta)

google_analytics.csv → Visitantes no site por data

relatorio_analitico_consolidado.csv → Input para insights automáticos

leads_convertidos_trafego_pago_.csv → Detalhes de conversões por Ads

kpis_e_metricas_.csv → Dicionário oficial de KPIs do projeto

▶️ Como Executar Localmente
Clone o repositório:
git clone https://github.com/SEU_USUARIO/dashboard-br-bank-streamlit-python.git
cd dashboard-br-bank-streamlit-python
Instale as dependências:
pip install -r requirements.txt
Rode o Streamlit:
streamlit run main.py
☁️ Deploy na Nuvem (Streamlit Cloud)
📍 Acesse:
https://dashboard-br-bank-final.streamlit.app/

✨ Diferenciais do Projeto
🔄 Simuladores interativos de crescimento e impacto tático

💡 Insights automáticos com linguagem natural

📊 Drill-down analítico por campanha, público e vendedor

♿ Acessibilidade total: contraste, dark mode, responsividade

📥 Exportação de dados por página (CSV/Excel)

📈 Projeção visual da meta de R$ 30 milhões

👩‍💻 Autoria e Contato
Projeto por: Dani Kaloi
💼 linkedin.com/in/danikaloi
