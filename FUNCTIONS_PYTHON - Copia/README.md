# ⚡ Azure Function App - Python (func-python-sgr)

Este projeto contém uma aplicação **Azure Function App** em **Python 3.11**, composta por funções HTTP independentes para processamento de arquivos.

---

## 📁 Estrutura do Projeto

```
Sgr-Function/
│
├── function_app.py          # Registro das funções
├── host.json                # Configurações do host
├── local.settings.json      # Configurações locais
├── requirements.txt         # Dependências Python
├── README.md                # Documentação
└── src/
    ├── common/
    │   ├── logger.py        # Sistema de logs
    │   └── logs/            # Arquivos de log
    └── services/            # funções
```

---

## ⚙️ Tecnologias Utilizadas

| Tipo | Tecnologia |
|------|------------|
| Runtime | Python 3.11 |
| Framework | Azure Functions (v4) |
| Deploy | Azure Functions Core Tools |
| Versionamento | Git |
| Integração | HTTP REST API |

---

## 🚀 Instalação e Execução Local

### 1️⃣ Pré-requisitos

- **Python 3.11+**
  - [Download Python](https://www.python.org/downloads/)
  - ⚠️ Marque "Add Python to PATH" durante a instalação
- **Git**
  - [Download Git](https://git-scm.com/downloads)
- **Azure Functions Core Tools v4**
  - [Instalação](https://learn.microsoft.com/azure/azure-functions/functions-run-local)

---

### 2️⃣ Clonar o Projeto

```bash
# Clone o repositório
git clone https://CFInovacao@dev.azure.com/CFInovacao/FUNCTIONS_PYTHON/_git/FUNCTIONS_PYTHON
cd FUNCTIONS_PYTHON
---

### 3️⃣ Configurar Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
# Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Se der erro de política:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Windows (CMD):
.venv\Scripts\activate

# Mac/Linux:
source .venv/bin/activate
```

✅ **Atenção:** Você verá `(.venv)` no início da linha do terminal quando estiver ativo.

---

### 4️⃣ Instalar Dependências

```bash
# Com o ambiente virtual ativado (.venv)
pip install -r requirements.txt
```

---

### 5️⃣ Executar Localmente

```bash
# Iniciar o Function App
func start

# Resultado esperado:
# Functions:
#   [NOME_FUNCTION]: [MÉTODO] http://localhost:7071/api/[ROTA]
```

---

## 🧪 Testando as Functions

Após iniciar o servidor, as funções estarão disponíveis em:

```
http://localhost:7071/api/[rota-da-funcao]
```

### 📡 Rotas Disponíveis

#### 1. Health Check
Verifica se a API está funcionando.

**Endpoint:** `GET /api/health`

```bash
# Teste com cURL
curl http://localhost:7071/api/health

# Ou no navegador
# http://localhost:7071/api/health
```

**Resposta esperada:**
```json
{
  "status": "OK",
  "message": "API está funcionando normalmente"
}
```

---

## 📦 Dependências

As dependências do projeto estão listadas em `requirements.txt`:

- `azure-functions` - SDK do Azure Functions
- `azure-functions-worker` - Worker do Azure Functions
- Bibliotecas específicas para cada serviço

---

## 🆕 Adicionando Novas Functions

### Estrutura de uma Function

Abra `function_app.py` e adicione:

```python
@app.function_name(name="MinhaFunction")
@app.route(route="minha-rota", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def minha_funcao(req: func.HttpRequest) -> func.HttpResponse:
    """
    Descrição da função.
    """
    try:
        # Lógica da função
        return func.HttpResponse(
            json.dumps({"sucesso": True}),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"erro": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
```

**Após adicionar:** Reinicie o servidor com `func start`.

---

## 🔧 Comandos Úteis

### Gerenciamento do Ambiente Virtual

```bash
# Ativar
.venv\Scripts\activate        # Windows
source .venv/bin/activate    # Mac/Linux

# Desativar
deactivate

# Ver pacotes instalados
pip list
```

### Desenvolvimento

```bash
# Executar projeto
func start

# Executar com mais detalhes
func start --verbose

# Ver configurações
type host.json  # Windows
cat host.json   # Mac/Linux
```

### Git

```bash
# Ver status
git status

# Adicionar arquivos
git add .
git add nome-do-arquivo.py

# Commit
git commit -m "Descrição das alterações"

# Push
git push origin main

# Criar branch
git checkout -b feature/nova-feature
```

---

## 🚀 Deploy para Azure

```bash
# 1. Login no Azure
az login

# 2. Publicar
func azure functionapp publish nome-da-funcao

# 3. Acessar
# https://nome-da-funcao.azurewebsites.net/api/[rota]
```

---

## 🐛 Solução de Problemas

### Python não encontrado
```bash
# Reinstale Python marcando "Add to PATH"
```

### Erro ao ativar virtual environment (PowerShell)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### ModuleNotFoundError
```bash
# Certifique-se que o venv está ativado (deve ver (.venv))
pip install -r requirements.txt
```

### Porta já em uso
```bash
# Use outra porta
func start --port 7072
```

---

## 📝 Estrutura de Arquivos Importantes

### `function_app.py`
- Registro e definição das functions
- Rotas e autenticação
- Lógica de cada endpoint

### `host.json`
- Configurações globais do Function App
- Timeout, retry policies
- Logging

### `local.settings.json`
- **⚠️ NÃO VERSIONAR** (adição manual de chaves)
- Configurações locais
- Variáveis de ambiente

### `requirements.txt`
- Todas as dependências Python
- Versões específicas

---

## 🔐 Segurança

- ⚠️ **NÃO commitar** `local.settings.json` com chaves sensíveis
- Use `.gitignore` para arquivos sensíveis
- Configure `auth_level` apropriado para cada function
- Valide todos os inputs

---

## 📖 Recursos

- [Azure Functions Docs](https://learn.microsoft.com/azure/azure-functions/)
- [Python Azure SDK](https://learn.microsoft.com/python/api/overview/azure/)
- [Azure CLI](https://learn.microsoft.com/cli/azure/)
