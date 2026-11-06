from flask import Flask, render_template, request, redirect
from database import criar_tabela, listar_produtos, cadastrar_produto, deletar_produto, atualizar_quantidade

app = Flask(__name__)

criar_tabela()

@app.route('/produtos')
def produtos():  # put application's code here
    lista = listar_produtos()
    return render_template("produtos.html", produtos=lista)

@app.route('/cadastro', methods=["GET", "POST"])
def cadastro1():
    if request.method == "POST":
        nome = request.form["nome"]
        quantidade = int(request.form["quantidade"])
        preco = int(request.form["preco"])
        cadastrar_produto(nome, quantidade, preco)
        return redirect("/produtos")
    return render_template("cadastro.html")

@app.route('/excluir', methods=["POST"])
def excluir():
    nome = request.form["nome"]
    deletar_produto(nome)
    return redirect("/produtos")

@app.route('/alterar/<nome>', methods=["POST", "GET"])
def alterar(nome):
    if request.method == "POST":
        quantidade = int(request.form["quantidade"])
        atualizar_quantidade(quantidade, nome)
        return redirect("/produtos")
    return render_template("alterar.html", nome=nome)


if __name__ == '__main__':
    app.run()
