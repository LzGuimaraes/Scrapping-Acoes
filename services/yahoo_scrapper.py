import yfinance as yf

def get_stock_data(ticker):
    symbol = f"{ticker}.SA"
    
    try:
        stock = yf.Ticker(symbol)
        info = stock.fast_info
        
        price = info.last_price
        
        if price is None:
            return None

        previous_close = info.previous_close
        
        variation_val = price - previous_close
        variation_percent = (variation_val / previous_close) * 100
        nome_ativo = ticker 

        return {
            "ticker": ticker,
            "name": nome_ativo,
            "current_price": round(price, 2),
            "daily_variation": round(variation_percent, 2),
            "type": "ACAO" 
        }

    except Exception as e:
        print(f"Erro no scrapper para {ticker}: {e}")
        return None