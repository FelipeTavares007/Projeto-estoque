from database import criar_tabela, cadastrar_produto, listar_produtos

criar_tabela()

while True:
    print("1 - Cadastrar produto")
    print("0 - Fechar")
    opcao = input("Escolha uma opção: ")

    if opcao == "1" :
        produto = str(input("Qual produto: "))
        preco = float(input("Qual o preco do produto: "))
        quantidade = int(input("Qual a quantidade de produtos: "))
        cadastrar_produto(produto, quantidade, preco)
    elif opcao == "0":
        print("Fechando...")
        break
    else:
        print("Opção invalida, tente novamente")

