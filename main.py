from database import criar_tabela, cadastrar_produto, listar_produtos, deletar_produto, atualizar_quantidade

criar_tabela()

def cadastro():
    produto = str(input("Qual produto: "))
    preco = float(input("Qual o preco do produto: "))
    quantidade = int(input("Qual a quantidade de produtos: "))
    cadastrar_produto(produto, quantidade, preco)

def excluir():
    nome = input("Qual produto quer excluir: ")
    print(repr(nome))
    deletar_produto(nome)

def lista():
    produtos = listar_produtos()
    for item in produtos:
        print(f"{item[0]} - {item[1]} | Qtd: {item[2]} | R$ {item[3]}")

def mudar_quantidade():
    produto = input("Qual produto deseja alterar: ")
    nova_quantidade = int(input("Digite a nova quantidade: "))
    atualizar_quantidade(nova_quantidade, produto)

while True:
    print("1 - Cadastrar produto")
    print("2 - Deletar produto")
    print("3 - Ver produtos")
    print("4 - Alterar quantidade")
    print("0 - Fechar")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            cadastro()
        case "2":
            excluir()
        case "3":
            lista()
        case "4":
            mudar_quantidade()
        case "0":
            print("Fechando, até mais")
            break
        case _:
            print("Opção inválida, tente novamente.")













