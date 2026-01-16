from services.yahoo_scrapper import get_stock_data
from services.economic_scrapper import get_economic_indicators 
from services.database import iniciar_banco, salvar_registro

iniciar_banco()

tickers_acoes = ["BBAS3", "BBDC3", "KLBN4", "TAEE3", "WEGE3", "MDIA3", "POMO3", "PLPL3"]

print("--- 1. Atualizando Ações (B3) ---")
for ticker in tickers_acoes:
    ticker = ticker.strip()
    print(f"Coletando: {ticker}")
    data = get_stock_data(ticker)
    
    if data:
        salvar_registro(data)
    else:
        print(f"❌ Falha em {ticker}")

print("\n--- 2. Atualizando Taxas (Banco Central) ---")
indicadores = get_economic_indicators() 

for ind in indicadores:
    print(f"Coletando: {ind['ticker']}")
    print(f"   Taxa Atual: {ind['current_price']}%")
    salvar_registro(ind) 

print("\n--- Processo Finalizado ---")