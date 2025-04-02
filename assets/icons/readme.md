# 📁 assets/icons/

Esta pasta armazena os **ícones customizados** utilizados no dashboard tático do BR Bank. Os ícones reforçam a comunicação visual, facilitam a leitura dos KPIs e aumentam a acessibilidade da interface — especialmente nos modos escuro, daltônico e alto contraste.

---

## 🎯 Finalidade

Os ícones são usados para representar:

- Indicadores de performance (ex: ROAS, CAC, Lucro)
- Status visuais (ex: sucesso, alerta, erro)
- Perfis de usuário (Executivo, Growth, Vendas, Produto)
- Elementos de navegação (ex: filtros, setas, voltar, avançar)

---

## 🧩 Regras de Organização

| Tipo de Ícone     | Uso Sugerido                          | Formato Ideal       |
|-------------------|----------------------------------------|----------------------|
| KPIs              | ROAS, CAC, Receita, Lucro              | `.svg` com fundo transparente |
| Status            | Sucesso ✅, Erro ❌, Alerta ⚠️          | `.svg` ou `.png`, 24x24px |
| Perfis            | Executivos, Vendas, Growth, Produto    | `.svg`, 48x48px, ícone neutro |
| Navegação         | Setas, filtros, menus, ícones de ação  | `.svg`, adaptável a CSS |

---

## 🎨 Acessibilidade Visual

Todos os ícones devem:

- Ter contraste suficiente para funcionar em **modo escuro** e **modo daltônico**
- Ser vetoriais (preferencialmente `.svg`) para manter qualidade em diferentes resoluções
- Ser nomeados de forma descritiva e sem espaços (ex: `executivo.svg`, `sucesso.svg`)

---

## 📦 Estrutura de Exemplo
assets/icons/ ├── sucesso.svg ├── alerta.svg ├── erro.svg ├── executivo.svg ├── growth.svg ├── vendas.svg ├── produto.svg └── filtro.svg


---

## ✅ Boas Práticas

- Evite cores vibrantes demais — utilize a **paleta do projeto definida em `settings.py`**.
- Prefira ícones com formas claras, simples e reconhecíveis.
- Centralize os ícones nos arquivos `.svg` para evitar desalinhamentos no Streamlit.

---

## 📁 Créditos (se aplicável)

Utilize apenas ícones de fontes com licença livre, como:

- [https://heroicons.com](https://heroicons.com)
- [https://feathericons.com](https://feathericons.com)
- [https://fontawesome.com](https://fontawesome.com)

---
