import random
from faker import Faker
import psycopg2

fake = Faker()

# Conexão com o banco de dados
conn = psycopg2.connect(
    dbname="biblioteca",
    user="postgres",
    password="pgadmin",
    host="localhost",
    port="5432"
)
biblioteca = conn.cursor()

# Configurar a quantidade de linhas que você deseja gerar para cada tabela
Livro = 200
Categoria = 500
Emprestimos = 500
Usuario = 500
Instituicoes = 10


# Gerar e inserir dados na tabela Livro
for x in range(Livro):
    biblioteca.execute("INSERT INTO Livro (id_livro, nomelivro, autor, co_autor) VALUES (%s, %s, %s, %s) ", (x, fake.catch_phrase(), fake.name(), fake.name()))

# Gerar e inserir dados na tabela Universidade
for x in range(Categoria):
    Categoria_id = random.randint(1, Livro)
    biblioteca.execute("INSERT INTO Categoria (id_categoria, nomecategoria) VALUES (%s, %s)", (x, fake.name()))

for x in range(Emprestimos):
    Emprestimo_id = random.randint(1, Livro)
    biblioteca.execute("INSERT INTO Emprestimos (id_emprestimo, nome) VALUES (%s, %s)", (x, fake.name()))
    
for x in range(Usuario):
    Usuario_id = random.randint(1, Livro)
    biblioteca.execute("INSERT INTO Usuario (id_usuario, nome, sobrenome) VALUES (%s, %s, %s)", (x, fake.name(), fake.name()))
                       
for x in range(Instituicoes):
    Instituicoes_id = random.randint(1, Livro)
    biblioteca.execute("INSERT INTO Instituicoes (id_instituicao, nomeinstituicao) VALUES (%s, %s)", (x, fake.city()))
# Fechar a conexão
# Confirmar as alterações e fechar a conexão
conn.commit()
biblioteca.close()
conn.close()