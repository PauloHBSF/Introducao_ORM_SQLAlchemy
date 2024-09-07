# SQLAlchemy PostgreSQL Project

*DISCLAIMER: README revisado e melhorado com Axíílio do ChatGPT*

Este projeto demonstra como utilizar o SQLAlchemy para interagir com um banco de dados PostgreSQL, criando tabelas, inserindo dados e realizando consultas, tudo através de uma abordagem ORM (Object Relational Mapper). A estrutura do projeto é gerenciada pelo Poetry para facilitar a instalação de dependências e o gerenciamento de ambientes.

## Pré-requisitos
Antes de começar, certifique-se de ter o seguinte instalado:

Python 3.8+
PostgreSQL (banco de dados)
Poetry (para gerenciar dependências)

# Instalação
1. Clone o repositório:

``` bash
git clone https://github.com/PauloHBSF/seu-repositorio.git
cd seu-repositorio
```

2. Instale as dependências com o Poetry:

``` bash
poetry install
```

3. Crie um arquivo .env na raiz do projeto com suas credenciais do PostgreSQL, utilizando como base o .env_example.

4. Ative o ambiente virtual:

``` bash
poetry shell
```

## Como Executar
1. Certifique-se de que o PostgreSQL está em execução e que as variáveis de ambiente no arquivo .env estão corretas. (Utilize o .env_example para criar seu .env)

2. Execute o script principal para criar a tabela e inserir os dados:

``` bash
python src/main.py
```

### O script irá:

- Conectar-se ao banco de dados PostgreSQL.
- Criar a tabela dim_products.
- Inserir dois registros de produtos.

## Dependências
- SQLAlchemy: ORM usado para interagir com o banco de dados.
- psycopg2: Driver PostgreSQL para Python.
- python-dotenv: Utilizado para carregar variáveis de ambiente do arquivo .env.