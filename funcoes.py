import datetime

# Cria a estrutura de um item de estoque com os campos necessários.
# Cada item usa um dicionário para manter nome, quantidade, valor e data de atualização.
def criar_item(nome, quantidade, valor, data_atualizacao=None):
    # Se não houver data de atualização informada, usa a data atual.
    if data_atualizacao is None:
        data_atualizacao = datetime.date.today().isoformat()

    # Retorna o item montado como dicionário.
    return {
        "nome": nome,
        "quantidade": quantidade,
        "valor": valor,
        "data_atualizacao": data_atualizacao,
    }


# Adiciona um item diretamente na lista original.
def adicionar_item(itens, item):
    itens.append(item)
    return itens


# Retorna a lista original para uso direto sem cópia.
def listar_itens(itens):
    return itens


# Remove todos os itens com o nome informado, alterando a lista original.
def remover_item(itens, nome):
    itens[:] = [item for item in itens if item.get("nome") != nome]
    return itens


# Atualiza os campos de um item identificado pelo nome.
# Se nenhum valor for passado para quantidade ou valor, mantém o valor anterior.
def atualizar_item(itens, nome, quantidade=None, valor=None, data_atualizacao=None):
    if data_atualizacao is None:
        data_atualizacao = datetime.date.today().isoformat()

    for item in itens:
        if item.get("nome") == nome:
            if quantidade is not None:
                item["quantidade"] = quantidade
            if valor is not None:
                item["valor"] = valor
            item["data_atualizacao"] = data_atualizacao
    return itens


# ----- funções auxiliares de leitura de dados do usuário -----

# Lê texto do usuário e remove espaços no início e fim.
def ler_texto(prompt):
    return input(prompt).strip()


# Lê um inteiro e garante que o valor seja válido.
def ler_inteiro(prompt, minimo=None):
    while True:
        try:
            valor = int(input(prompt))
            if minimo is not None and valor < minimo:
                print(f"Digite um número maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Apenas números são permitidos.")


# Lê um valor decimal e aceita vírgula ou ponto como separador.
def ler_valor(prompt):
    while True:
        try:
            texto = input(prompt).strip().replace(",", ".")
            return float(texto)
        except ValueError:
            print("Digite um valor numérico válido.")


# Cria um novo produto a partir da entrada do usuário.
def cadastrar(itens):
    nome = ler_texto("Nome do produto: ")
    quantidade = ler_inteiro("Quantidade inicial: ", minimo=0)
    valor = ler_valor("Valor unitário: R$ ")
    item = criar_item(nome, quantidade, valor)
    return adicionar_item(itens, item)


# Atualiza a quantidade de um item especificado por nome.
# Se a quantidade ficar zero ou negativa, remove o item na lista original.
def atualizar_quantidade(itens, nome, delta):
    item = next((item for item in itens if item.get("nome") == nome), None)
    if item is None:
        return itens

    nova_quantidade = item["quantidade"] + delta
    if nova_quantidade <= 0:
        return remover_item(itens, nome)
    return atualizar_item(itens, nome, quantidade=nova_quantidade)


# Busca um item pelo nome e retorna o item encontrado.
def consultar_por_nome(itens, nome):
    return next((item for item in itens if item.get("nome") == nome), None)
