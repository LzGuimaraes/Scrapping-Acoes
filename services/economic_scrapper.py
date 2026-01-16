import requests
from datetime import datetime

def get_economic_indicators():
    """
    Coleta indicadores econômicos do Banco Central do Brasil (API SGS)
    Retorna uma lista de dicionários compatível com a função salvar_registro.
    """
    indicators = []

    series_map = {
        "SELIC": {"code": 432, "name": "Taxa Selic Meta"},
        "IPCA":  {"code": 13522, "name": "IPCA (12m)"}
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    for ticker, info in series_map.items():
        try:
            url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{info['code']}/dados/ultimos/1?formato=json"
            
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()[0] 
                valor = float(data['valor']) 
                
                indicator_data = {
                    "ticker": ticker,          
                    "name": info["name"],      
                    "type": "TAXA",           
                    "current_price": valor,    
                    "daily_variation": 0.00    
                }
                indicators.append(indicator_data)
            else:
                print(f"⚠️ Erro HTTP {response.status_code} ao buscar {ticker}")

        except Exception as e:
            print(f"❌ Erro ao coletar indicador {ticker}: {e}")

    return indicators