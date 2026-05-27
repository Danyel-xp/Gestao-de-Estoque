# 📦 Gestão de Estoque

Sistema simples de gerenciamento de estoque desenvolvido em Python com SQLite, criado para praticar lógica de programação, manipulação de banco de dados e operações CRUD no terminal.

O projeto permite cadastrar produtos, atualizar quantidades, consultar informações e remover itens do estoque de forma prática e organizada.

---

# 🚀 Começando

Essas instruções permitem executar o projeto localmente em qualquer sistema operacional para fins de estudo, testes e aprendizado.

O sistema roda diretamente no terminal e utiliza banco de dados SQLite local, sem necessidade de instalar servidores adicionais.

---

# 📋 Pré-requisitos

Antes de executar o projeto, é necessário possuir:

- Python 3 instalado
- Terminal ou Prompt de Comando
- Editor de código opcional:
  - VS Code
  - PyCharm
  - Sublime Text

---

# 🔧 Instalação

## 1. Crie uma pasta

```bash
mkdir C:\user\SeuUsuario\NomedaPasta
```

---

## 2. Entre na pasta que você criou

```bash
cd C:\user\SeuUsuario\NomedaPasta
```

---

## 3. Clone o repositório

```bash
git clone https://github.com/Daniel-xp/Gestao-de-Estoque.git
```
### Certifique-se de estar na pasta C:\user\seuUsuario\NomedaPasta

---


## 4. Verifique se o Python está instalado

### Windows

```bash
python --version
```

### Linux / Mac

```bash
python3 --version
```

Se aparecer algo como:

```bash
Python 3.x.x
```

significa que está tudo pronto.

---

## 5. Execute o sistema

### Windows

```bash
python app.py
```

### Linux / Mac

```bash
python3 app.py
```

---

# ▶️ Como usar o sistema

Ao executar o programa, aparecerá um menu no terminal com as opções disponíveis.

Exemplo:

```bash
1 - Cadastrar produto
2 - Atualizar estoque
3 - Consultar produto
4 - Remover produto
5 - Sair
```

Basta digitar o número correspondente à operação desejada.

---

# 📌 Funcionalidades Implementadas

✅ Cadastro de produtos

✅ Consulta por:
- nome
- ID
- listagem completa

✅ Atualização de estoque:
- adicionar unidades
- remover unidades

✅ Exclusão de produtos

✅ Banco de dados SQLite

✅ Alertas automáticos de estoque:
- 🔴 Crítico
- 🟡 Baixo
- 🟢 Normal

✅ Registro automático de data

✅ Tratamento de entradas inválidas

---

# ⚙️ Executando os testes

O projeto foi testado manualmente diretamente pelo terminal.

Os testes realizados incluem:

- cadastro de produtos;
- atualização de quantidades;
- consultas;
- remoção de itens;
- validação de entradas inválidas;
- verificação do banco SQLite.

---

# 🔩 Análise dos testes de ponta a ponta

Os testes verificam:

- funcionamento correto do CRUD;
- persistência dos dados no banco;
- atualização automática do estoque;
- comportamento do menu;
- validação de erros do usuário.

Exemplos testados:

```bash
Cadastrar produto
Atualizar quantidade
Consultar produto
Excluir produto
```

---

# ⌨️ Testes de estilo de codificação

O código segue boas práticas básicas de organização:

- separação de arquivos;
- reutilização de funções;
- comentários explicativos;
- nomes semânticos;
- uso correto de funções Python.

Também foram aplicados:

- tratamento de exceções;
- organização modular;
- separação da lógica do banco em `db.py`.

---

# 📦 Implantação

O projeto pode ser executado em:

- Windows
- Linux
- MacOS
- Google Colab

Não é necessário instalar banco de dados externo, pois o SQLite já funciona localmente automaticamente.

---

# ☁️ Executando no Google Colab

## 1. Abra o Google Colab

Acesse:

```txt
https://colab.research.google.com/
```

---

## 2. Faça upload dos arquivos

Envie:
- `app.py`
- `db.py`

---

## 3. Execute uma célula com:

```python
!python3 app.py
```

---

## 4. Utilize normalmente

O sistema abrirá o menu diretamente no notebook.

O arquivo `estoque.db` será criado automaticamente.

---

# 🛠️ Construído com

- Python 3
- SQLite3
- Datetime

---

# 🖇️ Estrutura do Projeto

```bash
gestao-de-estoque/
│
├── app.py
├── db.py
├── estoque.db
├── README.md
└── .gitignore
```

---

# 📌 Versão

Projeto acadêmico inicial desenvolvido para prática de:

- lógica de programação;
- banco de dados;
- CRUD;
- Python básico/intermediário.

Versão atual:

```bash
1.0.0
```

---

# ✒️ Autores

## Daniel

Desenvolvimento principal do sistema, implementação das funcionalidades de gerenciamento de estoque, integração com SQLite e organização da estrutura do projeto.

GitHub:
[Daniel-xp][link]

[link]:https://github.com/Danyel-xp

---

## Nicolas Ribeiro

Auxílio no desenvolvimento, testes, documentação e organização das funcionalidades do sistema.

GitHub:
[NicolasWebMaster][link]

[link]:https://github.com/NicolasWebMaster

---

## Estevão

Auxílio na organização, validações e testes das funcionalidades implementadas.

GitHub:
[Estevao-exe][link]

[link]:https://github.com/Estevao-exe

---

# 📄 Licença

Este projeto foi desenvolvido para fins educacionais e acadêmicos.

Uso livre para aprendizado e estudos.

---

# 🎁 Expressões de gratidão

📢 Compartilhe este projeto com outros estudantes.

🧠 Continue evoluindo constantemente.

🚀 Cada projeto desenvolvido aumenta sua experiência prática.

💻 Programação se aprende construindo.

---