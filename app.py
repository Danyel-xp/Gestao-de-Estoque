from db import conectar, criar_tabela
from datetime import datetime

criar_tabela()

def cadastrar():

    try:
        conn = conectar()
        cursor = conn.cursor()

        nome = str(input('Nome: ')).strip().lower()
        categoria = str(input('Categoria: ')).strip().lower()
        quantidade = int(input('Quantidade: '))
        data = str(datetime.today().strftime('%Y/%m/%d às %Hh:%Mm:%Ss'))

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

        largura = 45

        print(f'╔{"═" * largura}╗')
        print(f'║{"PRODUTO" :^{largura}}║')
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


def atualizar():

    try:
        conn = conectar()
        cursor = conn.cursor()

        op = int(input('Escolha: '))
        
        if op == 1:
            nome_produto = str(input('Digite o nome do produto: ')).strip().lower()

            cursor.execute(
                "SELECT * FROM produtos WHERE nome LIKE ?",(f'%{nome_produto}%',)
            )

            mostra_produto = cursor.fetchone()

            print(f'Nome: {mostra_produto[1]}')
            print(f'Categoria: {mostra_produto[2]}')
            print(f'Quantidade atual: {mostra_produto[3]}')
            print(f'Ultima data de atualização: {mostra_produto[4]}')

            quantidade_adicionada = int(input('Quantas unidades você quer adicionar: '))

            escolha = str(input(f'Tem certeza que deseja adicionar novas {quantidade_adicionada} unidades [S/N]:  '))

            if escolha == 'S':

                cursor.execute(
                    'SELECT * FROM produtos WHERE nome LIKE ?',(f'%{nome_produto}%',)
                )

                produto = cursor.fetchone()

                cursor.execute(
                    'UPDATE produtos SET quantidade = ? WHERE nome LIKE ?',(produto[3] + quantidade_adicionada, f'%{nome_produto}%')
                )

                print(f'{nome_produto} atualizado com sucesso!')
                print(f'Qauntidade anterior: {produto[3]} ')
                print(f'Quantidade adicionada: {quantidade_adicionada}')
                print(f'Quantidade atual: {produto[3] + quantidade_adicionada}')

                conn.commit()

            elif escolha == 'N':
                print(f'A atualização de {mostra_produto[1]} foi cancelada!')

            else:
                print('Entrada inválida, tente novamente!')

    except ValueError as e :
        print(e)
    
    finally:
        conn.close()


    

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

            atualizar()

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