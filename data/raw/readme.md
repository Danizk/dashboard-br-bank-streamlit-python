# 📁 Pasta: data/raw

Esta pasta armazena os dados **originais** extraídos da fonte base do projeto: `BR_BANK_DANI_KALOI.xlsv`.

## ✅ Objetivo
Manter uma cópia dos arquivos **sem modificações**, como foram recebidos originalmente. Essa abordagem garante reprodutibilidade, rastreabilidade e integridade dos dados de entrada.

## 📌 Observações
- Nenhuma transformação ou tratamento deve ser aplicada diretamente aos arquivos desta pasta.
- Toda limpeza e modelagem deve ocorrer a partir dos arquivos copiados para `data/processed`.
- O conteúdo desta pasta não será versionado no Git (`.gitignore` já inclui essa proteção por padrão).

## 📝 Exemplo de conteúdo esperado
- `BR_BANK_DANI_KALOI.xlsv`
- Outros arquivos de entrada recebidos (caso novos dados históricos sejam integrados ao futuro).

## 🔒 Importante
Esta pasta pode conter dados sensíveis ou estratégicos. Evite compartilhar publicamente.

---

👨‍💻 Responsável técnico: Dani Kaloi  
📅 Projeto: Dashboard Tático BR Bank (Streamlit + Python)
