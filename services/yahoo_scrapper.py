import os
import certifi
import yfinance as yf

# Descomente a linha abaixo apenas se tiver problemas de certificado SSL no Windows
# os.environ['SSL_CERT_FILE'] = r"C:\TempCert\cacert.pem"

def get_stock_data(ticker):
    symbol = f"{ticker}.SA"
    
    try:
        stock = yf.Ticker(symbol)
        info = stock.fast_info
        
        price = info.last_price
        
        if price is None:
            return None

        # Dados adicionais
        day_low = info.day_low
        day_high = info.day_high
        volume = info.last_volume 
        previous_close = info.previous_close
        
        variation_val = price - previous_close
        variation_percent = (variation_val / previous_close) * 100
        variation_str = f"{variation_percent:.2f}%"

        # RETORNANDO JÁ COM OS NOMES QUE O BANCO ESPERA
        return {
            "ticker": ticker,
            "nome": ticker,   
            "preco": round(price, 2),  
            "variacao": variation_str,
            "minimo": round(day_low, 2), 
            "maximo": round(day_high, 2), 
            "volume": volume   
        }

    except Exception as e:
        return None