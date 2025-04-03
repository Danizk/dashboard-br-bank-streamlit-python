# 📁 assets/icons/

Esta pasta contém todos os **ícones customizados** utilizados no dashboard tático do BR Bank, com foco em uma experiência visual clara, acessível e intuitiva.

---

## 🎯 Finalidade

Os ícones aqui reunidos cumprem diferentes funções:

- **Identificação rápida** de KPIs e métricas (como receita, leads, ROI)
- **Auxílio visual** na navegação entre seções do dashboard
- **Refinamento estético** e reforço da identidade visual do BR Bank

---

## ✅ Padrões e Organização

### 📌 Nomenclatura recomendada:

| Tipo de Uso           | Prefixo sugerido      | Exemplo                |
|------------------------|------------------------|-------------------------|
| KPIs e Métricas        | `kpi_`                 | `kpi_receita.svg`       |
| Navegação e Páginas    | `nav_`                 | `nav_monetizacao.svg`   |
| Acessibilidade         | `access_`              | `access_contraste.svg`  |
| Alertas e Status       | `status_`              | `status_alerta.svg`     |
| Perfis de Usuário      | `profile_`             | `profile_growth.svg`    |

---

## 🧩 Categorias de Ícones

### 🔢 KPIs e Indicadores
- `kpi_receita.svg`
- `kpi_cac.svg`
- `kpi_roas.svg`
- `kpi_ltv.svg`
- `kpi_ticket_medio.svg`

### 🔀 Navegação
- `nav_aquisicao.svg`
- `nav_retencao.svg`
- `nav_monetizacao.svg`
- `nav_projecoes.svg`
- `nav_analytics.svg`

### 👥 Perfis de Usuário
- `profile_executivo.svg`
- `profile_growth.svg`
- `profile_vendas.svg`
- `profile_produto.svg`

### ⚠️ Alertas e Status
- `status_alerta.svg`
- `status_ok.svg`
- `status_negativo.svg`
- `status_em_progresso.svg`

### ♿ Acessibilidade
- `access_darkmode.svg`
- `access_daltonico.svg`
- `access_contraste.svg`
- `access_fonte.svg`

---

## 🎨 Requisitos Visuais

- Formato recomendado: **SVG** (vetorial, leve e escalável)
- Estilo: flat ou outline, coerente com o design geral
- Cores: seguir a paleta definida em `settings.py` (usar `fill="currentColor"` sempre que possível para herdar estilos)

---

## 🚨 Boas Práticas

- Evitar uso de ícones com textos embutidos
- Garantir legibilidade em tamanhos pequenos (24x24 ou 32x32 px)
- Preferir bibliotecas open-source (como [Lucide](https://lucide.dev), [Feather Icons](https://feathericons.com), [Heroicons](https://heroicons.com))
- Otimizar os arquivos SVG para produção (ex: https://jakearchibald.github.io/svgomg)

---

## 📝 Observações Finais

📌 Todos os ícones desta pasta são utilizados em **componentes reutilizáveis** via Streamlit, e são carregados dinamicamente conforme o tema (modo claro ou escuro).

Caso deseje contribuir com novos ícones, siga a convenção de nomes e adicione uma descrição neste `README.md`.

---
