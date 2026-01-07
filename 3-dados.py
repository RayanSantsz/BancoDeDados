import _sqlite3

# 1 - Conectando no bd
conexao = _sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Inserindo dados
cursor.execute(
    """
        INSERT INTO filmes(nome,ano,nota)
        Values ('Sonic', 2020, 8.0)
    """
)
conexao.commit()
conexao.close()
print('Dados inseridos na tabela')