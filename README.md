
# Gestão de Investimentos

## 🚀 Como executar o projeto

<p align="justify">Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:</p>

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=git,vscode,docker" />
</a>


### 🛠️ Como usar

Siga os passos abaixo para executar o projeto localmente:


````bash
# Clone o repositório
$ git clone https://github.com/seu-usuario/gestao_investimentos.git

# Navegue até o diretório do projeto
$ cd gestao_investimentos

# Crie um ambiente virtual

# Windows

$ python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt

# Linux

$ python -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# Execução

$ uvicorn main:app --reload --host 0.0.0.0 --port 8000
````