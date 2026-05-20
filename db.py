import sqlite3


def conectar():
    return sqlite3.connect('estoque.db')


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    data DATE NOT NULL
    )''')

    conn.commit()
    conn.close()

    