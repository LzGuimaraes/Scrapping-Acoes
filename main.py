from services.yahoo_scrapper import get_stock_data
from services.database import iniciar_banco, salvar_registro

iniciar_banco()

tickers = ["BBAS3", "BBDC3", "KLBN4", "TAEE3", "WEGE3", "MDIA3", "POMO3","PLPL3" ]

print("--- Iniciando Coleta ---")

for ticker in tickers:
    ticker = ticker.strip()
    print(f"Coletando: {ticker}")

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