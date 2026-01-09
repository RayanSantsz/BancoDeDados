import streamlit as st  
import dados             

# Define o título principal que aparece no topo da página
st.title("Filmes")

# Cria um campo de texto para o usuário digitar o nome do filme
nome = st.text_input("Nome do filme: ")

# Cria um campo numérico com botões de + e -
# min_value e max_value limitam o intervalo de anos aceitos
ano = st.number_input("Ano do filme: ", min_value=2010, max_value=2024)

# Cria uma barra deslizante para selecionar a nota de 0.0 a 10.0
nota = st.slider("Nota do filme: ", min_value=0.0, max_value=10.0)

if st.button('Adicionar'):
    # Chama a função do seu arquivo 'dados.py' passando as informações coletadas
    dados.insere_dados(nome, ano, nota)
    
    # Exibe uma mensagem verde de confirmação na tela
    st.success("Filme Cadastrado")

# Chama a função que busca todos os filmes cadastrados (geralmente retorna uma lista ou DataFrame)
filmes = dados.obter_dados()

# Define um cabeçalho secundário
st.header("Lista de Filmes: ")

# Renderiza uma tabela estática no navegador com os dados retornados
st.table(filmes)