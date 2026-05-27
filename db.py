import sqlite3


def conectar():
    return sqlite3.connect('estoque.db')


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL,
        data TEXT NOT NULL
            )
        '''
    )

    conn.commit()
    conn.close()

def deletar3():
    es = input("S/N:")

    conn = conectar()
    cursor = conn.cursor()
    if es == 's' or 'S':

        cursor.execute(
            '''
            DELETE from produtos
            '''
        )

        print(f'db deletado com sucesso')

    else:
        print('cancelado..')

    conn.commit()

    conn.close()
