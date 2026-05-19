from db import conectar, criar_tabela
from datetime import datetime

criar_tabela()
largura = 45

def cadastrar():

    try:
        conn = conectar()
        cursor = conn.cursor()

        nome = str(input('Nome: ')).strip().lower()

        cursor.execute('''
            SELECT * FROM produtos
             WHERE nome LIKE ?
        ''',(f'%{nome}%',))

        produto = cursor.fetchone()

        if nome == produto[1]:
            print(f'{nome} já existe!')
        
        else:
            categoria = str(input('Categoria: ')).strip().lower()
            quantidade = int(input('Quantidade: '))
            data = str(datetime.today().strftime('%Y/%m/%d às %Hh:%Mm:%Ss'))


            cursor.execute('''
                INSERT INTO produtos(nome,categoria,quantidade,data)
                VALUES(?,?,?,?)
            ''',(nome,categoria,quantidade,data))

            print(f'{nome} Cadatrado com sucesso, veja:')

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
                "SELECT * FROM produtos WHERE nome = ?",(nome_produto,)
            )

            mostra_produto = cursor.fetchone()

            print(f'Nome: {mostra_produto[1]}')
            print(f'Categoria: {mostra_produto[2]}')
            print(f'Quantidade atual: {mostra_produto[3]}')
            print(f'Ultima data de atualização: {mostra_produto[4]}')

            adicionar_quantidade = int(input('Quantas unidades você quer adicionar: '))
            nova_data = str(datetime.today().strftime('%Y/%m/%d às %Hh:%Mm:%Ss'))

            escolha = str(input(f'Tem certeza que deseja adicionar novas {adicionar_quantidade} unidades [S/N]:  ')).strip().lower

            if escolha == 's':

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
                print(f'Qauntidade anterior: {mostra_produto[3]} ')
                print(f'Unidades adicionadas: {adicionar_quantidade}')
                print(f'Quantidade atual: {produto_atualizado[3]}')

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
            print(f'Quantidade atual: {mostra_produto[3]}')
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
                print(f'Quantidade anterior: {mostra_produto[3]}')
                print(f'Unidades retiradas: {retirar_quantidade}')
                print(f'Quantidade atual: {produto_atualizado[3]}')

                conn.commit()

    except ValueError as e :
        print(e)
    
    finally:
        conn.close()


    

# def consultar():

# def alerta():


while True:
    largura = 30

    print(f'╔{"═" * largura}╗')
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