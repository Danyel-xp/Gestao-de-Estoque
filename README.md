# Gestão de Estoque

Este projeto é um sistema simples de controle de estoque em Python, feito como trabalho para a faculdade. A ideia principal é gerenciar produtos, cadastrar itens e manter uma lista de estoque organizada.

## Estrutura do projeto

- `app.py`
  - Arquivo principal para interagir com o usuário.
  - Mostra um menu básico para cadastrar, atualizar, consultar e sair.
  - Ainda está em desenvolvimento com a interface de menu pronta.

- `db.py`
  - Cria uma conexão com um banco de dados SQLite (`estoque.db`).
  - Cria a tabela `produtos` se ela não existir.
  - No momento, a implementação está pronta apenas para criar a tabela.

- `funcoes.py`
  - Contém as funções que manipulam a lista de estoque.
  - É o coração do projeto e foi desenvolvido para ser usado por `app.py`.
  - Inclui funções para criar, adicionar, listar, remover e atualizar itens.

## Como o projeto funciona

A ideia é que cada produto seja representado como um dicionário com os seguintes campos:

- `nome`: nome do produto
- `quantidade`: quantidade disponível em estoque
- `valor`: preço do produto
- `data_atualizacao`: data da última alteração

As funções em `funcoes.py` atuam diretamente na lista de itens, ou seja, elas modificam a lista original em vez de criar cópias novas.

## Como rodar o código

1. Abra o terminal na pasta do projeto.
2. Certifique-se de ter Python 3 instalado.
3. Execute o arquivo principal:

```bash
python3 app.py
```

Se não tiver um ambiente virtual, você pode criar um com:

```bash
python3 -m venv venv
source venv/bin/activate
```

Depois, rode o comando acima para iniciar o programa.

## Desenvolvimento atual

- O menu em `app.py` está preparado para exibir opções de cadastro, atualização e consulta.
- `db.py` já cria a tabela de produtos no banco de dados SQLite.
- `funcoes.py` já possui funções úteis para trabalhar com estoque de forma simples e direta.

## Próximos passos possíveis

- Ligar o menu de `app.py` às funções de `funcoes.py`.
- Salvar os produtos diretamente no banco de dados SQLite em vez de manter somente em memória.
- Criar uma opção de consulta completa para listar todos os produtos.
- Adicionar categorias e descrição dos produtos.

## Observações

Este projeto ainda está em desenvolvimento e a ideia é deixá-lo fácil de adaptar para outras regras de estoque. O código está escrito em linguagem simples para facilitar o entendimento de quem está estudando.

