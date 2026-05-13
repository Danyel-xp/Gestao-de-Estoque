from db import conectar, criar_tabela
import datetime

criar_tabela()
# def cadastrar():

# def atualizar():

# def consultar():

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
            print('')
            # cadastrar()

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