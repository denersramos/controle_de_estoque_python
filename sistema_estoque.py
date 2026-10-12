#--------------FUNÇÕES--------------

def cadastrar_produto():
    produto = input("Digite o nome do produto: ")

    while True:

        try:
            estoque = int(input("Digite a quantidade inicial: "))
        except ValueError:
            print("Digite um número inteiro.")
            continue

        if estoque < 0:
            print("O estoque não pode ser negativo.")
            continue

        return produto, estoque

def adicionar_produto():
    global estoque
    while True:
    
        #Trata entradas que não sejam números inteiros

        try:
            quantidade = int(input("Digite a quantidade que deseja adicionar: "))
        except ValueError:
            print("\n" "Entrada inválida. Por favor, digite um número inteiro.")
            continue

        if quantidade <= 0:
            print("\n" "A quantidade não pode ser negativa ou igual a zero.")
            continue

        #(estoque = estoque + quantidade) é menos utilizada que o de baixo, porém o resultado é o mesmo.

        estoque += quantidade
        print("\n" f"Estoque atualizado de {produto} para: {estoque}")

        break

def retirar_produto():
    global estoque
    while True:

        #Trata entradas que não sejam números inteiros

        try:
            print("\n" f"{estoque} unidades disponíveis no estoque.")
            quantidade = int(input("Digite a quantidade que deseja retirar: "))
        except ValueError:
            print("\n" "Entrada inválida. Por favor, digite um número inteiro.")
            continue

        #Trata entradas que sejam negativas ou iguais a zero

        if quantidade <= 0:
            print("\n" "A quantidade não pode ser negativa ou igual a zero.")
            continue

        estoque_atualizado = estoque - quantidade

        break
    
    if estoque_atualizado < 0:
        print("\n" "Estoque insuficiente.")
        print(f"Apenas {estoque} unidades disponíveis no estoque.")

    elif estoque_atualizado == 1:
        print("\n" f"Atualizado para {estoque_atualizado} unidade disponível no estoque.")
        estoque = estoque_atualizado

    elif estoque_atualizado == 0:
        print("\n" f"Atualizado para {estoque_atualizado} unidades disponíveis no estoque.")
        print("ATENÇÃO, O ESTOQUE ZEROU!")
        estoque = estoque_atualizado

    else:
        estoque = estoque_atualizado
        print("\n" f"Estoque atualizado de {produto} para: {estoque}")

#--------------INÍCIO--------------

#Pega os dois valores retornados e coloca cada um na variável correspondente.
produto, estoque = cadastrar_produto()

while True:

    #Menu de opções

    print("\n O que você deseja fazer?")
    print("1. Adicionar produtos ao estoque")
    print("2. Retirar produtos do estoque")
    print("3. Cadastrar novo produto")
    print("4. Sair do programa")

    opcao = input("\n" "Escolha uma opção: ")

    #Se a opção escolhida for 1, adiciona produtos ao estoque

    if opcao == "1":
        adicionar_produto()

    #Se a opção escolhida for 2, retira produtos do estoque

    elif opcao == "2":
        retirar_produto()

    #Se a opção escolhida for 3, cadastra um novo produto

    elif opcao == "3":
        produto, estoque = cadastrar_produto()

    #Se a opção escolhida for 4, sai do programa

    elif opcao == "4":
        print("\n" "Saindo do programa...")
        break

    #Se a opção escolhida for diferente de 1, 2 ,3 ou 4 exibe uma mensagem de erro.

    else:
        print("\n" "Opção inválida. Por favor, escolha uma opção válida.")
