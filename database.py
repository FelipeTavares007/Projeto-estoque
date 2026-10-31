import sqlite3


def criar_tabela():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER, 
            preco REAL
    )
""")
    conexao.commit()
    conexao.close()

criar_tabela()

def cadastrar_produto(nome, quantidade, preco):
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
        (nome, quantidade, preco)
    )
    conexao.commit()
    conexao.close()


def listar_produtos():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conexao.close()
    return produtos


def atualizar_quantidade(quantidade, nome):
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE produtos SET quantidade = ? WHERE nome = ?  COLLATE NOCASE ",
(quantidade, nome)
    )
    conexao.commit()
    conexao.close()


def deletar_produto(nome):
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE nome = ? COLLATE NOCASE",
        (nome,)

    )
    conexao.commit()
    conexao.close()


print(listar_produtos())