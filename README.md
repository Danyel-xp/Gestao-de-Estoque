# Gestão de Estoque

Projeto em Python para controle de estoque simples, com cadastro, atualização, consulta e exclusão de produtos.

## Sobre o projeto

Este sistema usa `sqlite3` para armazenar produtos em um banco de dados local chamado `estoque.db`. O programa roda no terminal e apresenta um menu para escolher as ações.

É um CRUD simples, funcional e direto:
- Create: cadastrar novo produto
- Read: consultar produto por nome, por id ou listar todos
- Update: adicionar unidades ou retirar unidades
- Delete: remover produto do estoque

## Como foi criado

1. Em `db.py`:
   - foi criada a função `conectar()` para abrir conexão com `estoque.db`
   - foi criada a função `criar_tabela()` para gerar a tabela `produtos` quando o programa inicia
   - a tabela guarda `id`, `nome`, `categoria`, `quantidade` e `data`

2. Em `app.py`:
   - o código importa `conectar` e `criar_tabela` do `db.py`
   - chama `criar_tabela()` logo no começo para garantir que o banco existe
   - define funções para cadastrar, atualizar, consultar e deletar produtos
   - cada função usa SQL com `sqlite3` para manipular os dados
   - usa `datetime` para registrar a data de cadastro ou atualização

3. No menu principal:
   - o usuário escolhe entre cadastrar, atualizar, consultar ou sair
   - o programa trata entradas de teclado e mostra mensagens claras
   - a conexão com o banco é aberta e fechada em cada operação

## Funcionalidades principais

- Cadastro de produto com nome, categoria, quantidade e data atual
- Atualização do estoque com adição ou retirada de unidades
- Exclusão de produto por nome ou por id
- Consulta de produto por nome, por id ou exibição de todos
- Alerta de estoque:
  - `🔴 Critico` quando a quantidade está em 3 ou menos
  - `🟡 Baixo` quando a quantidade está entre 4 e 10
  - `🟢 Normal` quando a quantidade é maior que 10

## Tecnologias usadas

- Python 3
- sqlite3
- datetime

## Como rodar no terminal

1. Abra o terminal na pasta do projeto.
2. Verifique o Python:
   ```bash
   python3 --version
   ```
3. Execute o programa:
   ```bash
   python3 app.py
   ```
4. Use o menu para selecionar as opções.

## Como rodar no Google Colab

1. Abra o Google Colab no navegador.
2. Crie um novo notebook.
3. Faça upload dos arquivos `app.py` e `db.py` no Colab.
4. Execute uma célula com:
   ```python
   !python3 app.py
   ```
5. O menu será exibido na saída da célula e o banco `estoque.db` será criado no ambiente do notebook.

## Membros do grupo

- Nicolas
- Daniel
- Estevão
