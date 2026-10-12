#--------------FUNÇÕES--------------

#Função que cadastra um produto e a quantidade inicial em estoque.

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

#Função que retorna a quantidade de unidades no singular ou plural, dependendo do valor de n.

def unidades(n):
    return f"{n} unidade" if n == 1 else f"{n} unidades"

#Função que adiciona produtos ao estoque.

def adicionar_produto(produto, estoque):
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
        print("\n" f"Estoque de {produto} atualizado para: {unidades(estoque)}")
        return estoque

#Função que retira produtos do estoque.

def retirar_produto(produto, estoque):
    while True:

        #Trata entradas que não sejam números inteiros

        try:
            print("\n" f"{unidades(estoque)} no estoque.")
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
        print(f"Apenas {unidades(estoque)} no estoque.")

    elif estoque_atualizado == 0:
        estoque = estoque_atualizado
        print("\n" f"Estoque de {produto} atualizado para: {unidades(estoque)}")
        print("ATENÇÃO, O ESTOQUE ZEROU!")

    else:
        estoque = estoque_atualizado
        print("\n" f"Estoque de {produto} atualizado para: {unidades(estoque)}")

    return estoque

#--------------INÍCIO--------------

#Pega os dois valores retornados na função e coloca cada um na variável correspondente.
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
        estoque = adicionar_produto(produto, estoque)

    #Se a opção escolhida for 2, retira produtos do estoque

    elif opcao == "2":
        estoque = retirar_produto(produto, estoque)

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
