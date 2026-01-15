# Scrapping Ações 📈

Um projeto de web scraping para coletar dados de ações brasileiras em tempo real da B3 (Bolsa de Valores Brasileira) usando a API do Yahoo Finance.

## 📋 Descrição

Este projeto automatiza a coleta de dados de ações brasileiras selecionadas, extraindo informações como preço atual, variação percentual, mínimo, máximo e volume de negociação. Os dados coletados são armazenados em um banco de dados PostgreSQL para análise e histórico.

## 🎯 Funcionalidades

- ✅ Coleta de dados em tempo real via Yahoo Finance
- ✅ Extração de múltiplas ações simultaneamente
- ✅ Cálculo de variação percentual do dia
- ✅ Armazenamento de dados em banco PostgreSQL
- ✅ Suporte para múltiplos tickers de ações

## 🚀 Tecnologias Utilizadas

- **Python 3.13** - Linguagem principal
- **YFinance** - API para coleta de dados de ações
- **Pandas** - Manipulação e análise de dados
- **PostgreSQL** - Banco de dados (via psycopg2)
- **Requests** - Cliente HTTP
- **Python-dotenv** - Gerenciamento de variáveis de ambiente

## 📦 Dependências

```
certifi>=2024.2.2
yfinance>=0.2.36
pandas>=1.3.0
requests>=2.31.0
psycopg2-binary
python-dotenv
```

## 🛠️ Instalação

### 1. Clone ou baixe o projeto

```bash
cd Scrapping-Acoes
```

### 2. Crie um ambiente virtual

```bash
python3 -m venv meu_venv
source meu_venv/bin/activate  # Linux/Mac
# ou
meu_venv\Scripts\activate  # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Configure as variáveis de ambiente no arquivo `.env`:

```j
# Exemplo de estrutura: 
postgresql://usuario:senha@host:porta/nome_banco
```

## 📂 Estrutura do Projeto

```
Scrapping-Acoes/
├── main.py                    # Script principal de execução
├── requirements.txt           # Dependências do projeto
├── README.md                  # Este arquivo
├── services/
│   ├── yahoo_scrapper.py     # Módulo de coleta de dados
│   └── database.py           # Módulo de banco de dados
└── meu_venv/                 # Ambiente virtual
```

## 🔧 Como Usar

Execute o script principal:

```bash
python main.py
```

O script irá:
1. Inicializar o banco de dados
2. Coletar dados para cada ticker listado
3. Exibir os dados coletados
4. Salvar os registros no banco de dados

### Tickers Disponíveis

O projeto coleta dados dos seguintes tickers por padrão:
- BBAS3 (Banco do Brasil)
- BBDC3 (Bradesco)
- KLBN4 (Klabin)
- TAEE3 (Taesa)
- WEGE3 (WEG)
- MDIA3 (Méliuz)
- POMO3 (Marcopolo)
- PLPL3 (Plásticos)

## 📊 Dados Coletados

Para cada ação, o projeto coleta:

- **ticker** - Código da ação
- **nome** - Nome/código da ação
- **preco** - Preço atual (em reais)
- **variacao** - Variação percentual do dia
- **minimo** - Preço mínimo do dia
- **maximo** - Preço máximo do dia
- **volume** - Volume de negociação

## 🔗 Módulos

### `services/yahoo_scrapper.py`
Responsável por coletar dados da API do Yahoo Finance usando a biblioteca `yfinance`. Formata os dados conforme esperado pelo banco de dados.

### `services/database.py`
Gerencia a conexão com o banco PostgreSQL e realiza operações de inserção e consulta de registros.

## ⚙️ Configuração do Banco de Dados

O projeto utiliza PostgreSQL. Certifique-se de:
1. Ter o PostgreSQL instalado e rodando
2. Criar um banco de dados para o projeto
3. Configurar as credenciais no arquivo `.env`

## 📝 Exemplo de Execução

```
--- Iniciando Coleta ---
Coletando: BBAS3
✔ Dados extraídos:
   Preço: R$ 35.45
   Variação: 2.15%
Coletando: BBDC3
✔ Dados extraídos:
   Preço: R$ 26.80
   Variação: -1.05%
--- Processo Finalizado ---
```

## 🐛 Troubleshooting

- **Erro de conexão com banco de dados**: Verifique as variáveis de ambiente e se o PostgreSQL está rodando
- **Falha na coleta de dados**: Verifique sua conexão com a internet e se o Yahoo Finance está acessível
- **Importação de módulos falha**: Certifique-se de ter ativado o ambiente virtual e instalado as dependências

## 📄 Licença

Projeto de uso pessoal

