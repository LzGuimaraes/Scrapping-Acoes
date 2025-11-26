import sqlite3
from datetime import datetime
import os

# Caminho para salvar na pasta 'data' na raiz do projeto
DB_PATH = os.path.join("data", "historico_acoes.db")

def iniciar_banco():
    # Cria a pasta 'data' se não existir
    os.makedirs("data", exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT,
            nome TEXT,
            preco REAL,
            variacao TEXT,
            maximo REAL,
            minimo REAL,
            volume REAL,
            data_coleta DATETIME
        )
    """)

    conn.commit()
    conn.close()

def salvar_registro(dados: dict):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO historico
        (ticker, nome, preco, variacao, maximo, minimo, volume, data_coleta)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
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
    conn.close()
    print(f"   Salvo no DB: {dados['ticker']}")