lista_de_compras = []

def adicionar_item(item, unidade):
    lista_de_compras.append((item, unidade))

def remover_item(item, unidade):
    for i, (produto, quantidade) in enumerate(lista_de_compras):
        if produto == item:
            if quantidade <= unidade:
                del lista_de_compras[i]
                print(f'{quantidade} de {item} foram removidos.')
            else:
                lista_de_compras[produto] = (item, unidade - quantidade)
                print(f'{unidade} de {item} foram removido da sua lista de compras.')
            return
        print(f'{item} não esta na sua lista de compras.')

def listar_itens():
    if len(lista_de_compras) == 0:
        print("A lista de compras está vazia.")
    else:
        print("Itens na lista de compras:")
        for item, quantidade in lista_de_compras:
            print(f"{quantidade}x {item}")

while True:
    print("Selecione uma opção:")
    print("1. Adicionar item à lista de compras")
    print("2. Remover item da lista de compras")
    print("3. Listar itens na lista de compras")
    print("4. Sair")
    opcao = input("Opção selecionada: ")

    if opcao == "1":
        item = input("Digite o nome do item: ")
        quantidade = int(input("Digite a quantidade: "))
        adicionar_item(item, quantidade)
    elif opcao == "2":
        item = input("Digite o nome do item: ")
        quantidade = int(input("Digite a quantidade: "))
        remover_item(item, quantidade)
    elif opcao == "3":
        listar_itens()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")





