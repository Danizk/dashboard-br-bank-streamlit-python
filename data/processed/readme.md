# 📁 Pasta: data/processed

Esta pasta contém os dados **tratados e prontos para uso** no dashboard do BR Bank.

## ✅ Objetivo
Armazenar datasets limpos, estruturados e já modelados com base nos arquivos brutos da pasta `data/raw`, prontos para alimentar os módulos do dashboard em Streamlit.

## 🛠️ Tipos de tratamento aplicados
- Padronização de nomes de colunas
- Conversão de tipos (datas, números, categorias)
- Cálculo prévio de métricas auxiliares
- Junções e cruzamentos entre abas relevantes (ex: CRM + Campanhas)
- Enriquecimento com KPIs calculados previamente

## 📌 Exemplos de arquivos esperados
- `dados_consolidados.csv`
- `kpis_por_vendedor.csv`
- `funil_conversao_diario.csv`
- `base_simulacoes.pkl`

## 🔄 Regras de atualização
- Os arquivos desta pasta são gerados a partir dos scripts em `utils/loader.py` e `utils/kpi_calculator.py`.
- Sempre que houver alteração nos dados brutos, os processados devem ser atualizados e validados.

## ⚠️ Importante
Esta é a **fonte de verdade para o dashboard**. Toda a interface e visualização em Streamlit consome os arquivos desta pasta, nunca diretamente os dados brutos.

---

👨‍💻 Responsável técnico: Dani Kaloi  
📊 Projeto: Dashboard Tático BR Bank (Etapa 6 – Desenvolvimento Técnico)
