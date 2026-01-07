import sqlite3

# 1- Conectando
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Leitura
dados = cursor.execute("SELECT * FROM filmes")
print(dados.fetchall())
