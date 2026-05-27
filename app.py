from db import conectar, criar_tabela,deletar3
from datetime import datetime

criar_tabela()

# Cadastra um novo produto no banco, validando os dados antes de inserir.
def cadastrar():

    try:
        conn = conectar()
        cursor = conn.cursor()

        nome = str(input('\nNome: ')).strip().title()

        cursor.execute(
            '''
            SELECT * FROM produtos
            WHERE nome = ?
            ''', (nome,)
        )

        checar_produto = cursor.fetchone()

        # Verifica se o produto já existe antes de inserir
        if checar_produto:
            print(f'\n{checar_produto[1]} já existe!')

        else:
            categoria = str(input('\nCategoria: ')).strip().capitalize()

            preco = float(input(f'\nPreço: '))

            quantidade = int(input('\nQuantidade: '))

            data = str(datetime.today().strftime('%Y-%m-%d %H:%M'))

            cursor.execute(
                '''
                INSERT INTO produtos(nome,categoria,preco,quantidade,data)
                VALUES(?,?,?,?,?)
                ''',
                (
                    nome,
                    categoria,
                    preco,
                    quantidade,
                    data
                )
            )

            conn.commit()

            cursor.execute(
                '''
                SELECT * FROM produtos
                WHERE nome = ?
                ''', (nome,)
            )

            produto = cursor.fetchone()

            print(f'\n{produto[1]} cadastrado com sucesso, veja:')

            # Variavel que guarda o valor do tamanho da tabela
            largura = 38

            print(f'╔{"═" * largura}╗')
            print(f'║{"PRODUTO":^{largura}}║')
            print(f'╠{"═" * largura}╣')
            print(f'║ {"Id: " + str(produto[0]):<{largura - 1}}║')
            print(f'║ {"Nome: " + produto[1][:18]:<{largura - 1}}║')
            print(f'║ {"Categoria: " + produto[2][:20]:<{largura - 1}}║')
            print(f'║ {"Preço: " + f"{produto[3]:.2f}" + " R$":<{largura - 1}}║')
            print(f'║ {"Quantidade: " + str(produto[4]) + " Uni." [:18]:<{largura - 1}}║')
            print(f'║ {"Data: " + produto[5]:<{largura - 1}}║')
            print(f'╚{"═" * largura}╝')

    except ValueError as e:
        print('\nQuantidade deve conter apenas números inteiros, por favor revise o erro e tente novamente!')
        print(e)

    # Fecha a conexão sempre que possível
    finally:
        conn.close()

# Atualiza um produto no estoque: adicionar unidades, retirar unidades ou excluir.
def atualizar():

    try:

        largura = 38

        print(f'╔{"═" * largura}╗')
        print(f'║{"ATUALIZAR PRODUTO":^{largura}}║')
        print(f'╠{"═" * largura}╣')
        print(f'║{" 1 → ADICIONAR UNIDADES":<{largura}}║')
        print(f'║{" 2 → RETIRAR UNIDADES":<{largura}}║')
        print(f'║{" 3 → DELETAR PRODUTO":<{largura}}║')
        print(f'║{" 4 → VOLTAR":<{largura}}║')
        print(f'╚{"═" * largura}╝')

        conn = conectar()
        cursor = conn.cursor()

        op = int(input('\nEscolha: '))

        if op == 1:

            print(f'╔{"═" * largura}╗')
            print(f'║{"ADICONAR UNIDADES":^{largura}}║')
            print(f'╠{"═" * largura}╣')
            print(f'║{" 1 → NOME":<{largura}}║')
            print(f'║{" 2 → ID":<{largura}}║')
            print(f'║{" 3 → VOLTAR":<{largura}}║')
            print(f'╚{"═" * largura}╝')

            escolha = int(input('\nEscolha: '))

            if escolha == 1:

                nome_produto = str(
                    input('\nDigite o nome do produto: ')).strip().title()

                cursor.execute(
                    '''
                    SELECT * FROM produtos
                    WHERE nome = ?
                    ''', (nome_produto,)
                )

                checar_produto = cursor.fetchone()

                # Checar o produto se existe no banco de dados
                if checar_produto:

                    cursor.execute(
                        '''
                        SELECT * FROM produtos
                        WHERE nome = ?
                        ''', (nome_produto,)
                    )

                    mostra_produto = cursor.fetchone()

                    status = alerta(mostra_produto)
                    
                    id_tabela = ' ID: ' + str(mostra_produto[0])
                    nome = ' Nome: '+ mostra_produto[1]
                    categoria = ' Categoria: ' + mostra_produto[2]
                    preco = ' Preço: ' + f"{mostra_produto[3]:.2f}" + ' R$'
                    quantidade = ' Quantidade: ' + str(mostra_produto[4]) + ' Unidades'
                    data = ' Ultima atualização: ' + mostra_produto[5]
                    
                    print(f'╔{"═" * largura}╗')
                    print(f'║{"DADOS DO PRODUTO":^{largura}}║')
                    print(f'╠{"═" * largura}╣')
                    print(f'║{id_tabela :<{largura}}║')
                    print(f'║{nome :<{largura}}║')
                    print(f'║{categoria :<{largura}}║')
                    print(f'║{preco :<{largura}}║')
                    print(f'║{quantidade :<{largura}}║')
                    print(f'║{" Status: " + status :<{largura - 1}}║')
                    print(f'║{data :<{largura}}║')
                    print(f'╚{"═" * largura}╝')

                    if mostra_produto[4] <= 3:
                        print(
                            f'\n⚠️ ATENÇÃO O PRODUTO {mostra_produto[1]} ESTÁ COM O ESTOQUE MUITO BAIXO!')

                    adicionar_quantidade = int(
                        input('\nQuantas unidades você quer adicionar: '))

                    # Atualiza a data automaticamente ao alterar o estoque
                    nova_data = str(
                        datetime.today().strftime('%Y-%m-%d %H:%M'))

                    # Opção final para ter certeza se o usuario realmente quer atualizar o produto escolhido
                    escolha = str(input(
                        f'\nTem certeza que deseja adicionar novas {adicionar_quantidade} unidades [S/N]: ')).strip().lower()

                    if escolha == 's':

                        cursor.execute(
                            '''
                            SELECT * FROM produtos
                            WHERE nome = ? 
                            ''', (nome_produto,)
                        )

                        produto = cursor.fetchone()

                        quantidade_atualizada = produto[4] +  adicionar_quantidade

                        cursor.execute(
                            '''
                            UPDATE produtos SET quantidade = ?, data = ?
                            WHERE nome = ?
                            ''',
                            (
                                quantidade_atualizada,
                                nova_data,
                                nome_produto
                            )
                        )

                        cursor.execute(
                            '''
                            SELECT * FROM produtos
                            WHERE nome = ?
                            ''', (nome_produto,)
                        )

                        produto_atualizado = cursor.fetchone()

                        status = alerta(produto_atualizado)

                        print(f'╔{"═"* largura}╗')
                        print(f'║{"ATUALIZAÇÃO CONCLUIDA":^{largura}}║')
                        print(f'╠{"═" * largura}╣')
                        print(f'║{" Quantidade anterior: " + str(mostra_produto[4]) + " unidades" :<{largura}}║')
                        print(f'║{" Unidades adicionadas: " + str(adicionar_quantidade) + " unidades" :<{largura}}║')
                        print(f'║{" Quantidade atual: " + str(produto_atualizado[4]) + " unidades " :<{largura}}║')
                        print(f'║{" Status:" + status :<{largura -1}}║')
                        print(f'╚{"═" * largura}╝')

                        conn.commit()

                    elif escolha == 'n':
                        print(
                            f'\nA atualização de {mostra_produto[1]} foi cancelada!')

                    else:
                        print('\nEntrada inválida, tente novamente!')

                else:
                    print('Produto não encontrado')

            elif escolha == 2:

                id = int(input('Digite o ID do produto: '))

                cursor.execute(
                    '''
                SELECT * FROM produtos
                WHERE id = ?
                ''', (id,)
                )

                checar_produto = cursor.fetchone()

                if checar_produto:

                    cursor.execute(
                        '''
                    SELECT * FROM produtos
                    WHERE id = ?
                    ''', (id,)
                    )

                    mostra_produto = cursor.fetchone()

                    status = alerta(mostra_produto)
                    
                    id_tabela = ' ID: ' + str(mostra_produto[0])
                    nome = ' Nome: '+ mostra_produto[1]
                    categoria = ' Categoria: ' + mostra_produto[2]
                    preco = ' Preço: ' + f"{mostra_produto[3]:.2f}" + ' R$'
                    quantidade = ' Quantidade: ' + str(mostra_produto[4]) + ' Unidades'
                    data = ' Ultima atualização: ' + mostra_produto[5]
                    
                    print(f'╔{"═" * largura}╗')
                    print(f'║{"DADOS DO PRODUTO":^{largura}}║')
                    print(f'╠{"═" * largura}╣')
                    print(f'║{id_tabela :<{largura}}║')
                    print(f'║{nome :<{largura}}║')
                    print(f'║{categoria :<{largura}}║')
                    print(f'║{preco :<{largura}}║')
                    print(f'║{quantidade :<{largura}}║')
                    print(f'║{" Status: " + status :<{largura - 1}}║')
                    print(f'║{data :<{largura}}║')
                    print(f'╚{"═" * largura}╝')

                    if mostra_produto[4] <= 3:
                        print(
                            f'\n⚠️ ATENÇÃO O PRODUTO {mostra_produto[1]} ESTÁ COM O ESTOQUE MUITO BAIXO!')

                    adicionar_quantidade = int(
                        input('\nQuantas unidades você quer adicionar: '))

                    nova_data = str(
                        datetime.today().strftime('%Y-%m-%d %H:%M'))

                    escolha = str(input(
                        f'\nTem certeza que deseja adicionar novas {adicionar_quantidade} unidades [S/N]: ')).strip().lower()

                    if escolha == 's':

                        cursor.execute(
                            '''
                            SELECT * FROM produtos
                            WHERE id = ? 
                            ''', (id,)
                        )

                        produto = cursor.fetchone()

                        quantidade_atualizada = produto[4] + adicionar_quantidade

                        cursor.execute(
                            '''
                            UPDATE produtos SET quantidade = ?, data = ?
                            WHERE id = ?
                            ''',
                            (
                                quantidade_atualizada,
                                nova_data,
                                id
                            )
                        )

                        cursor.execute(
                            '''
                            SELECT * FROM produtos
                            WHERE id = ?
                            ''', (id,)
                        )

                        produto_atualizado = cursor.fetchone()

                        status = alerta(produto_atualizado)

                        print(f'╔{"═"* largura}╗')
                        print(f'║{"ATUALIZAÇÃO CONCLUIDA":^{largura}}║')
                        print(f'╠{"═" * largura}╣')
                        print(f'║{" Quantidade anterior: " + str(mostra_produto[4]) + " unidades" :<{largura}}║')
                        print(f'║{" Unidades adicionadas: " + str(adicionar_quantidade) + " unidades" :<{largura}}║')
                        print(f'║{" Quantidade atual: " + str(produto_atualizado[4]) + " unidades" :<{largura}}║')
                        print(f'║{" Status:" + status :<{largura -1}}║')
                        print(f'╚{"═" * largura}╝')
                        conn.commit()

                    elif escolha == 'n':
                        print(
                            f'\nA atualização de {mostra_produto[1]} foi cancelada!')

                    else:
                        print('\nEntrada inválida, tente novamente!')
                else:
                    print('\nProduto não encontado')

            elif escolha == 3:
                print('Voltando...')

        elif op == 2:

            print(f'╔{"═" * largura}╗')
            print(f'║{"RETIRAR UNIDADES" :^{largura}}║')
            print(f'╠{"═" * largura}╣')
            print(f'║{" 1 → NOME" :<{largura}}║')
            print(f'║{" 2 → ID" :<{largura}}║')
            print(f'║{" 3 → VOLTAR" :<{largura}}║')
            print(f'╚{"═" * largura}╝')

            escolha = int(input('Escolhar: '))

            if escolha == 1:

                nome_produto = str(
                    input('\nDigite o nome do produto: ')).strip().title()

                cursor.execute(
                    '''
                    SELECT * FROM produtos
                    WHERE nome = ?
                    ''', (nome_produto,)
                )

                checar_produto = cursor.fetchone()

                if checar_produto:
                    cursor.execute(
                        '''
                    SELECT * FROM produtos
                    WHERE nome = ?
                    ''', (nome_produto,)
                    )

                    mostra_produto = cursor.fetchone()

                    status = alerta(mostra_produto)

                    id_tabela = ' ID: ' + str(mostra_produto[0])
                    nome = ' Nome: '+ mostra_produto[1]
                    categoria = ' Categoria: ' + mostra_produto[2]
                    preco = ' Preço: ' + f"{mostra_produto[3]:.2f}" + ' R$'
                    quantidade = ' Quantidade: ' + str(mostra_produto[4]) + ' Unidades'
                    data = ' Ultima atualização: ' + mostra_produto[5]
                    
                    print(f'╔{"═" * largura}╗')
                    print(f'║{"DADOS DO PRODUTO":^{largura}}║')
                    print(f'╠{"═" * largura}╣')
                    print(f'║{id_tabela :<{largura}}║')
                    print(f'║{nome :<{largura}}║')
                    print(f'║{categoria :<{largura}}║')
                    print(f'║{preco :<{largura}}║')
                    print(f'║{quantidade :<{largura}}║')
                    print(f'║{" Status: " + status :<{largura - 1}}║')
                    print(f'║{data :<{largura}}║')
                    print(f'╚{"═" * largura}╝')
                    
                    if mostra_produto[4] <= 3:
                        print(
                            f'\n⚠️ ATENÇÃO O PRODUTO {mostra_produto[1]} ESTÁ COM O ESTOQUE MUITO BAIXO!')

                    retirar_quantidade = int(
                        input('\nQuantas unidades você quer retirar: '))

                    nova_data = str(
                        datetime.today().strftime('%Y-%m-%d %H:%M'))

                    escolha = input(
                        f'\nTem certeza que deseja retira {retirar_quantidade} unidades de {mostra_produto[1]} [S/N]: ').strip().lower()

                    if escolha == 's':

                        cursor.execute(
                            '''
                            SELECT * FROM produtos
                            WHERE nome = ?
                            ''', (nome_produto,)
                        )

                        produto = cursor.fetchone()

                        quantidade_atualizada = produto[4] - retirar_quantidade
                        
                        if retirar_quantidade > produto[4]:
                            print('\nQuantidade indisponivel no estoque! ')
                            print(f'Estoque atual: {produto[4]}')
                        
                        else:

                            cursor.execute(
                                '''
                                UPDATE produtos SET quantidade = ?, data = ?
                                WHERE nome = ?
                                ''',
                                (
                                    quantidade_atualizada,
                                    nova_data,
                                    produto[1]
                                )
                            )

                            cursor.execute(
                                '''
                                SELECT * FROM produtos WHERE nome = ?
                                ''', (produto[1],)
                            )

                            produto_atualizado = cursor.fetchone()

                            status = alerta(produto_atualizado)

                            print(f'\n╔{"═"* largura}╗')
                            print(f'║{"ATUALIZAÇÃO CONCLUIDA":^{largura}}║')
                            print(f'╠{"═" * largura}╣')
                            print(f'║{" Quantidade anterior: " + str(mostra_produto[4]) + " unidades" :<{largura}}║')
                            print(f'║{" Unidades retiradas: " + str(retirar_quantidade) + " unidades" :<{largura}}║')
                            print(f'║{" Quantidade atual: " + str(produto_atualizado[4]) + " unidades" :<{largura}}║')
                            print(f'║{" Status: " + status :<{largura - 1}}║')
                            print(f'╚{"═" * largura}╝')

                            conn.commit()

                    elif escolha == 'n':
                        print(
                            f'\nA atualização de {mostra_produto[1]} foi cancelada!')

                    else:
                        print('\nEntrada inválida, favor tente novamente!')
                else:
                    print('\nProduto não encontrado')

            elif escolha == 2:

                id = int(input('\nDigite o ID do produto: '))

                cursor.execute(
                    '''
                    SELECT * FROM produtos
                    WHERE id = ?
                    ''', (id,)

                )

                checar_produto = cursor.fetchone()

                if checar_produto:
                    cursor.execute(
                        '''
                    SELECT * FROM produtos
                    WHERE id = ?
                    ''', (id,)
                    )

                    mostra_produto = cursor.fetchone()

                    status = alerta(mostra_produto)

                    id_tabela = ' ID: ' + str(mostra_produto[0])
                    nome = ' Nome: '+ mostra_produto[1]
                    categoria = ' Categoria: ' + mostra_produto[2]
                    preco = ' Preço: ' + f"{mostra_produto[3]:.2f}" + ' R$'
                    quantidade = ' Quantidade: ' + str(mostra_produto[4]) + ' Unidades'
                    data = ' Ultima atualização: ' + mostra_produto[5]
                    
                    print(f'╔{"═" * largura}╗')
                    print(f'║{"DADOS DO PRODUTO":^{largura}}║')
                    print(f'╠{"═" * largura}╣')
                    print(f'║{id_tabela :<{largura}}║')
                    print(f'║{nome :<{largura}}║')
                    print(f'║{categoria :<{largura}}║')
                    print(f'║{preco :<{largura}}║')
                    print(f'║{quantidade :<{largura}}║')
                    print(f'║{" Status: " + status :<{largura - 1}}║')
                    print(f'║{data :<{largura}}║')
                    print(f'╚{"═" * largura}╝')

                    if mostra_produto[4] <= 3:
                        print(
                            f'\n⚠️ ATENÇÃO O PRODUTO {mostra_produto[1]} ESTÁ COM O ESTOQUE MUITO BAIXO!')

                    retirar_quantidade = int(
                        input('\nQuantas unidades você quer retirar: '))

                    nova_data = str(
                        datetime.today().strftime('%Y-%m-%d %H:%M'))

                    escolha = input(
                        f'\nTem certeza que deseja retira {retirar_quantidade} unidades de {mostra_produto[1]} [S/N]: ').strip().lower()

                    if escolha == 's':

                        cursor.execute(
                            '''
                            SELECT * FROM produtos
                            WHERE id = ?
                            ''', (id,)
                        )

                        produto = cursor.fetchone()

                        quantidade_atualizada = produto[4] - retirar_quantidade

                        if retirar_quantidade > produto[4]:
                            print('\nQuantidade indisponivel no estoque! ')
                            print(f'Estoque atual: {produto[4]}')

                        else:
                            cursor.execute(
                                '''
                                UPDATE produtos SET quantidade = ?, data = ?
                                WHERE id = ?
                                ''',
                                (
                                    quantidade_atualizada,
                                    nova_data,
                                    id
                                )
                            )

                            cursor.execute(
                                '''
                                SELECT * FROM produtos WHERE id = ?
                                ''', (id,)
                            )

                            produto_atualizado = cursor.fetchone()

                            status = alerta(produto_atualizado)


                            print(f'\n╔{"═"* largura}╗')
                            print(f'║{"ATUALIZAÇÃO CONCLUIDA":^{largura}}║')
                            print(f'╠{"═" * largura}╣')
                            print(f'║{"Quantidade anterior: " + str(mostra_produto[4]) + " unidades" :<{largura}}║')
                            print(f'║{"Unidades retiradas: " + str(retirar_quantidade) + " unidades" :<{largura}}║')
                            print(f'║{"Quantidade atual: " + str(produto_atualizado[4]) + " unidades" :<{largura}}║')
                            print(f'║{"Status: " + status :<{largura -1}}║')
                            print(f'╚{"═" * largura}╝')

                        conn.commit()

                    elif escolha == 'n':
                        print(
                            f'\nA atualização de {mostra_produto[1]} foi cancelada!')

                    else:
                        print('\nEntrada inválida, favor tente novamente!')
                else:
                    print('\nProduto não encontrado')

            elif escolha == 3:
                print('Voltando...')
                return

        elif op == 3:
            deletar()

        elif op == 4:
            print('Voltando...')
            return

        else:
            print('\nOpção inválida, por favor tente novamente!')

    except ValueError as e:
        print(e)

    finally:
        conn.close()


# Consulta produtos por nome, id ou lista todos os itens do estoque.
def consultar():
    try:

        largura = 38

        print(f'╔{"═" * largura}╗')
        print(f'║{"CONSULTAR PRODUTOS":^{largura}}║')
        print(f'╠{"═" * largura}╣')
        print(f'║{" 1 → CONSULTAR POR NOME":<{largura}}║')
        print(f'║{" 2 → CONSULATAR POR ID":<{largura}}║')
        print(f'║{" 3 → CONSULTAR TODOS":<{largura}}║')
        print(f'║{" 4 → VOLTAR":<{largura}}║')
        print(f'╚{"═" * largura}╝')

        conn = conectar()
        cursor = conn.cursor()

        op = int(input('\nEscolha: '))

        if op == 1:
            nome = str(input('\nNome do produto: ')).strip().title()

            cursor.execute(
                '''
                SELECT * FROM produtos
                WHERE nome = ?
                ''', (nome,)
            )

            consultar_produto = cursor.fetchone()

            if consultar_produto:

                status = alerta(consultar_produto)

                id_tabela = ' Id: ' + str(consultar_produto[0])
                nome = ' Nome: ' + consultar_produto[1]
                categoria = ' Categoria: ' + consultar_produto[2]
                preco = ' Preço: ' + f"{consultar_produto[3]:.2f}" + ' R$'
                quantidade = ' Quantidade: ' + str(consultar_produto[4]) + ' Unidades'
                data = ' Ultima atualização: ' + consultar_produto[5]

                print(f'╔{"═" * largura}╗')
                print(f'║{'DADOS DO PRODUTO' :^{largura}}║')
                print(f'╠{"═" * largura}╣')
                print(f'║{id_tabela :<{largura}}║')
                print(f'║{nome :<{largura}}║')
                print(f'║{categoria :<{largura}}║')
                print(f'║{preco :<{largura}}║')
                print(f'║{quantidade :<{largura}}║')
                print(f'║{" Status:" + status :<{largura - 1}}║')
                print(f'║{data :<{largura}}║')
                print(f'╚{"═" * largura}╝')

                if consultar_produto[4] <= 3:
                    print(f'\n⚠️ ATENÇÃO O PRODUTO {consultar_produto[1]} ESTÁ COM O ESTOQUE MUITO BAIXO!')

            else:
                print('\nProduto não encontrado')

        elif op == 2:
            id = int(input('\nId do produto: '))

            cursor.execute(
                '''
                SELECT * FROM produtos
                WHERE id = ?
                ''', (id,)
            )

            consultar_produto = cursor.fetchone()

            if consultar_produto:

                status = alerta(consultar_produto)

                id_tabela = ' Id: ' + str(consultar_produto[0])
                nome = ' Nome: ' + consultar_produto[1]
                categoria = ' Categoria: ' + consultar_produto[2]
                preco = ' Preço: ' + f"{consultar_produto[3]:.2f}" + ' R$'
                quantidade = ' Quantidade: ' + str(consultar_produto[4]) + ' Unidades'
                data = ' Ultima atualização: ' + consultar_produto[5]

                print(f'╔{"═" * largura}╗')
                print(f'║{'DADOS DO PRODUTO' :^{largura}}║')
                print(f'╠{"═" * largura}╣')
                print(f'║{id_tabela :<{largura}}║')
                print(f'║{nome :<{largura}}║')
                print(f'║{categoria :<{largura}}║')
                print(f'║{preco :<{largura}}║')
                print(f'║{quantidade :<{largura}}║')
                print(f'║{" Status:" + status :<{largura - 1}}║')
                print(f'║{data :<{largura}}║')
                print(f'╚{"═" * largura}╝')

                if consultar_produto[4] <= 3:
                    print(f'\n⚠️ ATENÇÃO O PRODUTO {consultar_produto[1]} ESTÁ COM O ESTOQUE MUITO BAIXO!')

            else:
                print('\nProduto não encontrado')

        elif op == 3:
            cursor.execute(
                '''
                SELECT * FROM produtos
                '''
            )

            checar_produtos = cursor.fetchall()

            if checar_produtos:

                cursor.execute(
                    '''
                    SELECT * FROM produtos
                    '''
                )

                todos = cursor.fetchall()

                linha = '-' * 155

                print('\n'+linha)
                print('║{:^20}║ {:^20}║ {:^20}║ {:^20}║ {:^20}║ {:^20} ║ {:^20}║'.format(
                    "ID", "Nome", "Categoria", "Preço", "Quantidade", "Status ", "Data"))
                print(linha)

                for produto in todos:

                    status = alerta(produto)

                    print('║{:^20}║ {:^20}║ {:^20}║ {:^20}║ {:^20}║ {:^20}║ {:^20}║'.format(
                        f"{produto[0]}", f"{produto[1]:}", f"{produto[2]}", f"{produto[3]:.2f}", f"{produto[4]}", f"{status}", f"{produto[5]}"))
                    print('-' * 155)

                    # print(f'\nId: {produto[0]}')
                    # print(f'Nome: {produto[1]}')
                    # print(f'Categoria: {produto[2]}')
                    # print(f'Preço: {produto[3]:.2f} R$')
                    # print(f'Quantidade: {produto[4]} uni.')
                    # print(f'Status: {status}')
                    # print(f'Ultima data de atualização: {produto[5]}')
            else:
                print('Nenhum produto encontrado')

        elif op == 4:
            print('\nVoltando...')
            return

        else:
            print('\nProduto não encontrado')

    except ValueError as e:
        print('\nApenas números são permitidos, favor tente novamente!')
        print(e)

    finally:
        conn.close()


# Retorna o status de estoque do produto com base na quantidade disponível.
def alerta(produto):
    try:

        if produto[4] <= 3:
            return '🔴 Critico'

        elif 3 < produto[4] <= 10:
            return '🟡 Baixo'

        else:
            return '🟢 Normal'

    except ValueError as e:
        print(e)


# Deleta um produto pelo nome ou pelo id após confirmação.
def deletar():

    try:
        largura = 38

        print(f'╔{"═" * largura}╗')
        print(f'║{"DELETAR PRODUTO":^{largura}}║')
        print(f'╠{"═" * largura}╣')
        print(f'║{" 1 → DELETAR POR NOME":<{largura}}║')
        print(f'║{" 2 → DELETAR POR ID":<{largura}}║')
        print(f'║{" 3 → VOLTAR":<{largura}}║')
        print(f'╚{"═" * largura}╝')

        conn = conectar()
        cursor = conn.cursor()

        op = int(input('\nEscolha: '))

        if op == 1:
            nome = input('\nNome do produto: ').strip().title()

            cursor.execute(
                '''
                SELECT * FROM produtos
                WHERE nome = ?
                ''', (nome,)
            )

            produto = cursor.fetchone()

            if produto:

                escolha = input(
                    f'\nTem certeza que deseja deletar permanentemente {produto[1]} do estoque [S/N]: ').strip().lower()

                if escolha == 's':
                    cursor.execute(
                        '''
                        DELETE FROM produtos
                        WHERE nome = ?
                        ''', (nome,)
                    )

                    conn.commit()

                    print(f'\n{produto[1]} deletado com sucesso!')

                elif escolha == 'n':
                    print('\nA ação de deletar produto foi cancelada!')

                else:
                    print('\nEntrada invalida, tente novamente!')

            else:
                print('\nProduto não encontrado')

        elif op == 2:
            id = int(input('\nId: '))

            cursor.execute(
                '''
                SELECT * FROM produtos
                WHERE id = ?
                ''', (id,)
            )

            produto = cursor.fetchone()

            if produto:

                escolha = str(input(
                    f'\nTem certeza que deseja deletar permanentemente {produto[1]} do estoque [S/N]: ')).strip().lower()

                if escolha == 's':
                    cursor.execute(
                        '''
                        DELETE FROM produtos 
                        WHERE id = ?
                        ''', (id,)
                    )

                    conn.commit()

                    print(f'\n{produto[1]} deletado com sucesso!')

                elif escolha == 'n':
                    print('\nA ação de deletar produto foi cancelada!')

                else:
                    print('\nEntrada invalida, tente novamente!')

            else:
                print('\nProduto não encontrado')

        elif op == 3:
            print('Voltando...')
            return

        else:
            print('\nOpção inválida!')

    except ValueError as e:
        print('\nApenas números são permitidos, favor tente novamente!')
        print(e)

    finally:
        conn.close()

# Loop principal do menu com seleção de ações.
while True:
    try:

        largura = 38

        print(f'\n╔{"═" * largura}╗')
        print(f'║{"MENU":^{largura}}║')
        print(f'╠{"═" * largura}╣')
        print(f'║{" 1 → CADASTRAR":<{largura}}║')
        print(f'║{" 2 → ATUALIZAR":<{largura}}║')
        print(f'║{" 3 → CONSULTAR":<{largura}}║')
        print(f'║{" 4 → SAIR":<{largura}}║')
        print(f'╚{"═" * largura}╝')

        opcao = int(input('\nEscolha: '))

        if opcao == 1:
            cadastrar()

        elif opcao == 2:
            atualizar()

        elif opcao == 3:
            consultar()

        elif opcao == 4:
            print('\nfechando o programa...')
            print('\nAté logo👋')
            break
        elif opcao == 5:
            deletar3()

        else:
            print('Apenas números de 1 a 4 são permitidos')

    except ValueError as e:
        print('\nApenas números são permitidos!')
        print(e)
