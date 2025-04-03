# 📁 assets/

A pasta `assets/` centraliza todos os **recursos visuais** utilizados no dashboard tático do BR Bank, com foco em acessibilidade, responsividade e identidade visual consistente com a marca.

---

## 🎨 Estrutura

assets/ ├── icons/ # Ícones customizados usados nos KPIs e navegação └── styles.css # Estilo visual do dashboard (cores, fontes, dark mode)

---

## 📌 Descrição dos Arquivos

### 📁 icons/
Contém os ícones utilizados ao longo do dashboard, como:

- Indicadores de performance (💰 Receita, 📉 CAC, 📈 ROAS)
- Status visuais (✅ Sucesso, ⚠️ Alerta, ❌ Erro)
- Perfis de usuário (Executivo, Growth, Vendas, Produto)
- Navegação e filtros

🔗 Veja detalhes específicos em: `assets/icons/README.md`

---

### 🎨 styles.css
Este arquivo contém o estilo global do dashboard:

- Paleta de cores (modo claro e escuro)
- Tamanhos de fonte e espaçamento
- Regras para responsividade
- Ícones visuais com classes reutilizáveis
- Estilos adicionais de acessibilidade (alto contraste, foco visível)

---

## ♿ Acessibilidade Visual
Todos os recursos visuais seguem boas práticas de acessibilidade:

- Contraste suficiente entre fundo/texto
- Ícones com significados visuais claros
- Compatibilidade com dark mode e modo daltônico
- Suporte ao ajuste de fontes e contraste via `settings.py`

---

## ✨ Boas Práticas

- Mantenha o padrão de nomenclatura: `kpi_<nome>.svg`, `icon_<função>.svg`
- Utilize formatos vetoriais (`.svg`) para máxima compatibilidade
- Mantenha os arquivos organizados e reutilizáveis

---
