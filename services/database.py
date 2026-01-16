import psycopg2
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    if not DATABASE_URL:
        raise ValueError("A variável DATABASE_URL não foi definida no .env")
    return psycopg2.connect(DATABASE_URL)

def iniciar_banco():
    """
    Cria a tabela 'assets' baseada no diagrama ValoraDB se ela não existir.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assets (
                ticker VARCHAR(20) PRIMARY KEY,
                name VARCHAR(100),
                type VARCHAR(20) NOT NULL,
                current_price DECIMAL(19,4),
                daily_variation DECIMAL(10,2),
                last_update TIMESTAMP
            )
        """)

        conn.commit()
        cursor.close()
        conn.close()
        print("✔ Tabela 'assets' verificada/criada com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao conectar ou criar tabela: {e}")

def salvar_registro(dados: dict):
    """
    Realiza um UPSERT (Update ou Insert) na tabela assets.
    Se o ticker já existir, atualiza preço e variação. Se não, cria novo.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        query = """
            INSERT INTO assets (ticker, name, type, current_price, daily_variation, last_update)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (ticker) 
            DO UPDATE SET
                current_price = EXCLUDED.current_price,
                daily_variation = EXCLUDED.daily_variation,
                last_update = EXCLUDED.last_update;
        """
        
        cursor.execute(query, (
            dados["ticker"],
            dados["name"],
            dados["type"],
            dados["current_price"],
            dados["daily_variation"],
            datetime.now()
        ))

        conn.commit()
        cursor.close()
        conn.close()
        print(f"   💾 Ativo atualizado/salvo em 'assets': {dados['ticker']}")
        
    except Exception as e:
        print(f"❌ Erro ao salvar {dados['ticker']}: {e}")