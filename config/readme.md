# ⚙️ Pasta: config/

Este diretório centraliza as **configurações globais** do dashboard tático BR Bank.

Ele contém variáveis reutilizáveis, parâmetros de estilo, perfis de usuário e caminhos dos dados. Toda a lógica de design e navegação do projeto depende desses arquivos.

---

## 📄 Arquivos Presentes

### 1. `settings.py`
Arquivo responsável por armazenar:

- 🎨 Paleta de cores do dashboard
- 👤 Perfis de usuários disponíveis
- 📱 Parâmetros de visualização responsiva
- 📌 Tema visual padrão (modo claro ou escuro)

Exemplo:
```python
USER_PROFILES = ["Executivo", "Marketing & Growth", "Vendas", "Produto"]

COLOR_PALETTE = {
    "primary": "#0043A4",
    "success": "#00B050",
    "danger": "#D80027",
    "background": "#F9F9F9",
    "font": "#333333"
}
