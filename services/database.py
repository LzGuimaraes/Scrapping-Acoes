import psycopg2
import os
from datetime import datetime
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

#Carrega URL do banco 
DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    """Conecta usando a URL direta (Connection String)"""
    if not DATABASE_URL:
        raise ValueError("A variável DATABASE_URL não foi definida no .env")
    
    return psycopg2.connect(DATABASE_URL)

def iniciar_banco():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS historico (
                id SERIAL PRIMARY KEY,
                ticker TEXT,
                nome TEXT,
                preco REAL,
                variacao TEXT,
                maximo REAL,
                minimo REAL,
                volume REAL,
                data_coleta TIMESTAMP
            )
        """)

        conn.commit()
        cursor.close()
        conn.close()
        print("✔ Tabela verificada/criada com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao conectar ou criar tabela: {e}")

def salvar_registro(dados: dict):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO historico
            (ticker, nome, preco, variacao, maximo, minimo, volume, data_coleta)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            dados["ticker"],
            dados["nome"],
            dados["preco"],
            dados["variacao"],
            dados["maximo"],
            dados["minimo"],
            dados["volume"],
            datetime.now()
        ))

        conn.commit()
        cursor.close()
        conn.close()
        print(f"   Salvo no PostgreSQL: {dados['ticker']}")
        
    except Exception as e:
        print(f"❌ Erro ao salvar {dados['ticker']}: {e}")