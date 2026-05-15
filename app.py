from db import conectar, criar_tabela
import datetime

criar_tabela()

def cadastrar():

    try:
        conn = conectar()
        cursor = conn.cursor()

        nome = str(input('Nome: '))
        categoria = str(input('Categoria: '))
        quantidade = int(input('Quantidade: '))
        data = str(input('Data YYY-MM-DD: '))

        cursor.execute('''
            INSERT INTO produtos(nome,categoria,quantidade,data)
            VALUES(?,?,?,?)
        ''',(nome,categoria,quantidade,data))

        cursor.execute('''
            SELECT * FROM produtos
             WHERE nome LIKE ?
        ''',(f'%{nome}%',))

        produto = cursor.fetchone()

        print(f'{nome} Cadatrado com sucesso, veja:')

        largura = 30

        print(f'╔{"═" * largura}╗')
        print(f'║{"PRODUTO" :^ {largura}}║')
        print(f'╠{"═" * largura}╣')
        print(f'║ {"Id: " + str(produto[0]) :<{ largura - 1 }}║')
        print(f'║ {"Nome: " + produto[1][:18 ] :<{ largura - 1 }}║')
        print(f'║ {"Categoria: " + produto[2][:20] :<{ largura -1 }}║')
        print(f'║ {"Quantidade: " + str(produto[3])[:18] :<{ largura - 1 }}║')
        print(f'║ {"Data: " + produto[4] :<{ largura -1 }}║')
        print(f'╚{"═" * largura}╝')

        conn.commit()
        
    except ValueError as e:
        print('Quantidade deve conter apenas números inteiros, por favor revise o erro e tente novamente!')
        print(e)
    
    finally:
        conn.close()


# def atualizar():

# def consultar():

# def alerta():

# Simbolos  ╔ ╗ ╚ ╝ ═ ║ ╠ ╣ →

while True:

    print('╔════════════════════╗')
    print('║        MENU        ║')
    print('╠════════════════════╣')
    print('║ 1 → Cadastrar      ║')
    print('║ 2 → Atualizar      ║')
    print('║ 3 → Consultar      ║')
    print('║ 4 → Sair           ║')
    print('╚════════════════════╝')

    try:

        opcao = int(input('Escolha: '))

        if opcao == 1:
            cadastrar()

        elif opcao == 2:

            print('╔═════════════════════════════╗')
            print('║      ATUALIZAR PRODUTO      ║')
            print('╠═════════════════════════════╣')
            print('║ 1 → Adicionar unidades      ║')
            print('║ 2 → Retirar unidades        ║')
            print('╚═════════════════════════════╝')

            # atualizar()

        elif opcao == 3:
            
            print('╔══════════════════════════╗')
            print('║    CONSULTAR PRODUTOS    ║')
            print('╠══════════════════════════╣')
            print('║ 1 → Consutar por nome    ║')
            print('║ 2 → Consultar por id     ║')   
            print('║ 2 → Consultar todos      ║')   
            print('╚══════════════════════════╝')

            # consultar()

        elif opcao == 4 :
            print('Saindo do Programa...')
            print("Sistema fechado com êxito!")
            
            break

    except ValueError:
        print('\nApenas números são permitidos!')