import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('titulo.db')

# 2 - Criando o cursor (responsavel por permitir fazer alterações no bd)
cursor = conexao.cursor()

# 3 - Criando a tabela
cursor.execute(
    """
        CREATE TABLE filmes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        );
    """
)

# 4 - Fecha conexão
conexao.close()
print('Tabela criada com sucesso')