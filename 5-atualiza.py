import sqlite3

# 1 - conectando no bd
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - atualizando dados
id = 1
cursor.execute(
    """
        UPDATE filmes SET nota = ? 
        WHERE id = ? 
    """,
    ("8.5", id)
)
conexao.commit()
print('DADOS ATUALIZADOS')