# Importa o scraper
from services.yahoo_scrapper import get_stock_data
# Importa as funções do banco (do arquivo database.py que criamos acima)
from services.database import iniciar_banco, salvar_registro

# 1. INICIALIZA O BANCO (Cria a tabela se não existir)
iniciar_banco()

tickers = ["PETR4", "VALE3", "ITUB4", "BBAS3"]

print("--- Iniciando Coleta ---")

for ticker in tickers:
    ticker = ticker.strip()
    print("\n=====================")
    print(f"Coletando: {ticker}")
    print("=====================")

    data = get_stock_data(ticker)

    if not data:
        print(f"❌ Não foi possível coletar {ticker}")
        continue

    print("✔ Dados extraídos:")
    # Mostra na tela para conferência
    print(f"   Preço: R$ {data['preco']}")
    print(f"   Variação: {data['variacao']}")

    # 2. SALVA NO BANCO DE DADOS
    salvar_registro(data)

print("\n--- Processo Finalizado ---")