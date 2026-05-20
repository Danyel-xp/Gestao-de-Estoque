from db import conectar, criar_tabela,deletar
from datetime import datetime

criar_tabela()

def cadastrar():

    try:
        conn = conectar()
        cursor = conn.cursor()

        nome = str(input('Nome: ')).strip().lower()

        cursor.execute('''
            SELECT * FROM produtos
             WHERE nome = ?
        ''',(nome,))

        checar_produto = cursor.fetchone()

        if checar_produto:
            print(f'{checar_produto[1]} já existe!')
        
        else:
            categoria = str(input('Categoria: ')).strip().lower()

            quantidade = int(input('Quantidade: '))

            data = str(datetime.today().strftime('%Y/%m/%d às %Hh:%Mm:%Ss'))


            cursor.execute('''
                INSERT INTO produtos(nome,categoria,quantidade,data)
                VALUES(?,?,?,?)
            ''',(nome,categoria,quantidade,data))

            conn.commit()

            cursor.execute(
            '''
            SELECT * FROM produtos
            WHERE nome = ?
            ''',(nome,)
            )

            produto = cursor.fetchone()

            print(f'{produto[1]} cadastrado com sucesso, veja:')

            largura = 45

            print(f'╔{"═" * largura}╗')
            print(f'║{"PRODUTO" :^{largura}}║')
            print(f'╠{"═" * largura}╣')
            print(f'║ {"Id: " + str(produto[0]):<{ largura - 1 }}║')
            print(f'║ {"Nome: " + produto[1][:18]:<{ largura - 1 }}║')
            print(f'║ {"Categoria: " + produto[2][:20]:<{ largura -1 }}║')
            print(f'║ {"Quantidade: " + str(produto[3]) +" uni."[:18]:<{ largura - 1 }}║')
            print(f'║ {"Data: " + produto[4]:<{ largura -1}}║')
            print(f'╚{"═" * largura}╝')

            
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
                "SELECT * FROM produtos WHERE nome = ?",(nome_produto,)
            )

            mostra_produto = cursor.fetchone()

            print(f'Nome: {mostra_produto[1]}')
            print(f'Categoria: {mostra_produto[2]}')
            print(f'Quantidade atual: {mostra_produto[3]} unidades')
            print(f'Ultima data de atualização: {mostra_produto[4]}')

            adicionar_quantidade = int(input('Quantas unidades você quer adicionar: '))
            nova_data = str(datetime.today().strftime('%Y/%m/%d às %Hh:%Mm:%Ss'))

            escolha = str(input(f'Tem certeza que deseja adicionar novas {adicionar_quantidade} unidades [S/N]:  ')).strip().lower

            if escolha == 's' or 'S':

                cursor.execute(
                    'SELECT * FROM produtos WHERE nome = ? ',(nome_produto,)
                )

                produto = cursor.fetchone()

                quantidade_atualizada = produto[3] + adicionar_quantidade
                
                cursor.execute(
                    '''
                    UPDATE produtos SET quantidade = ?, data = ?
                    WHERE nome = ?
                    ''',
                    (quantidade_atualizada, nova_data , nome_produto)
                )

                cursor.execute(
                    'SELECT * FROM produtos WHERE nome = ?',(nome_produto,)
                )

                produto_atualizado = cursor.fetchone()

                print(f'{mostra_produto[1]} atualizado com sucesso!')
                print(f'Qauntidade anterior: {mostra_produto[3]} unidades')
                print(f'Unidades adicionadas: {adicionar_quantidade} unidades')
                print(f'Quantidade atual: {produto_atualizado[3]} unidades')

                conn.commit()

            elif escolha == 'n':
                print(f'A atualização de {mostra_produto[1]} foi cancelada!')

            else:
                print('Entrada inválida, tente novamente!')

        elif op == 2:
            nome_produto = str(input('Digite o nome do produto: ')).strip().lower()

            cursor.execute(
            '''
            SELECT * FROM produtos
            WHERE nome = ?
            ''', (nome_produto,)
            )

            mostra_produto = cursor.fetchone()

            print(f'ID: {mostra_produto[0]}')
            print(f'Nome: {mostra_produto[1]}')
            print(f'Categoria: {mostra_produto[2]}')
            print(f'Quantidade atual: {mostra_produto[3]} unidades')
            print(f'Ultima data de atualização: {mostra_produto[4]}')

            retirar_quantidade = int(input('Quantas unidades você quer retirar:  '))
            nova_data = str(datetime.today().strftime('%Y/%m/%d às %Hh:%Mm:%Ss'))

            escolha = input(f'Tem certeza que deseja retira {retirar_quantidade} unidades de {mostra_produto[1]} [S/N]:  ').strip().lower()

            if escolha == 's':
                
                cursor.execute(
                '''
                SELECT * FROM produtos
                WHERE nome = ?
                ''',(nome_produto,)
                )

                produto = cursor.fetchone()

                quantidade_atualizada = produto[3] - retirar_quantidade

                cursor.execute(
                '''
                UPDATE produtos SET quantidade = ?, data = ?
                WHERE nome = ?
                ''',(quantidade_atualizada,nova_data,produto[1])
                )

                cursor.execute(
                '''
                SELECT * FROM produtos WHERE nome = ?
                ''',(produto[1],)
                )

                produto_atualizado = cursor.fetchone()

                print(f'{produto_atualizado[1]} atualizado com sucesso!')
                print(f'Quantidade anterior: {mostra_produto[3]} unidades')
                print(f'Unidades retiradas: {retirar_quantidade} unidades')
                print(f'Quantidade atual: {produto_atualizado[3]} unidades')

                conn.commit()
            elif escolha == 'n':
                print(f'A atualização de {mostra_produto[1]} foi cancelada!')
            
            else:
                print('Entrada inválida, favor tente novamente!')

    except ValueError as e :
        print(e)
    
    finally:
        conn.close()


def consultar():
    try:

        print('╔══════════════════════════╗')
        print('║    CONSULTAR PRODUTOS    ║')
        print('╠══════════════════════════╣')
        print('║ 1 → Consutar por nome    ║')
        print('║ 2 → Consultar por id     ║')   
        print('║ 3 → Consultar todos      ║')   
        print('╚══════════════════════════╝')

        conn = conectar()
        cursor = conn.cursor()

        op = int(input('Escolha: '))

        if op == 1:
            nome = str(input('Nome do produto: ')).strip().lower()

            cursor.execute(
            '''
            SELECT * FROM produtos
            WHERE nome = ?
            ''',(nome,)
            )

            consultar_produto = cursor.fetchone()

            print(f'\nId: {consultar_produto[0]}')
            print(f'Nome: {consultar_produto[1]}')
            print(f'Categoria: {consultar_produto[2]}')
            print(f'Quantidade atual: {consultar_produto[3]} unidades')
            print(f'Ultima data de atualização: {consultar_produto[4]}')

        elif op == 2 :
            id = int(input('Id do produto: '))

            cursor.execute(
            '''
            SELECT * FROM produtos
            WHERE id = ?
            ''',(id,)
            )

            consultar_produto = cursor.fetchone()

            print(f'\nId: {consultar_produto[0]}')
            print(f'Nome: {consultar_produto[1]}')
            print(f'Categoria: {consultar_produto[2]}')
            print(f'Quantidade atual: {consultar_produto[3]} unidades')
            print(f'Ultima data de atualização: {consultar_produto[4]}')
        
        elif op == 3:
            cursor.execute(
            '''
            SELECT * FROM produtos
            '''
            )

            todos = cursor.fetchall()


            for produto in todos:
                print(f'\nId: {produto[0]}')
                print(f'Nome: {produto[1]}')
                print(f'Categoria: {produto[2]}')
                print(f'Quantidade: {produto[3]} uni.')
                print(f'Ultima data de atualização: {produto[4]}')



    except ValueError as e:
        print('Apenas números são permitidos, favor tente novamente!')
        print(e)

    finally:
        conn.close()
        

# def alerta():


while True:
    largura = 30

    print(f'\n╔{"═" * largura}╗')
    print(f'║{"MENU":^{largura}}║')
    print(f'╠{"═" * largura}╣')
    print(f'║{" 1 → CADASTRA":<{largura}}║')
    print(f'║{" 2 → ATUALIZAR":<{largura}}║')
    print(f'║{" 3 → CONSULTAR":<{largura}}║')
    print(f'║{" 4 → SAIR" :<{largura}}║')
    print(f'╚{"═" * largura}╝')

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
            print('║ 3 → Voltar                  ║')
            print('╚═════════════════════════════╝')

            atualizar()

        elif opcao == 3:

            consultar()

        elif opcao == 4 :
            print('Saindo do Programa...')
            print("Sistema fechado com êxito!")
            break

        elif opcao == 5:
            deletar()
            break

    except ValueError:
        print('\nApenas números são permitidos!')