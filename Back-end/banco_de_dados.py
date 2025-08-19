import sqlite3
import bcrypt

# Funções do banco 

def criar_tabela():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute('''
  CREATE TABLE IF NOT EXISTS usuarios (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
cpf TEXT NOT NULL,
celular TEXT NOT NULL,
nome TEXT NOT NULL,
sobrenome TEXT NMOT NULL,
email TEXT NOT NULL,
data_nascimento TEXT NOT NULL,
senha_hash TEXT NOT NULL
)
''')
    conexao.commit()
    conexao.close()

def cadastrar_usuario(cpf, celular, nome, sobrenome, email, data_nascimento, senha):
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    if cursor.fetchone():
        print("Erro: Usuário com este email já existe.")
        conexao.close()
        return False
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    cursor.execute('''
INSERT INTO usuarios (cpf, celular, nome, sobrenome, email, data_nascimento, senha_hash)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', (cpf, celular, nome, sobrenome, email, data_nascimento, senha_hash))
    conexao.commit()
    conexao.close()
    print(f"Usuário {nome} cadastrao com sucesso.")
    return True
    
def logar_usuario(email, senha_digitada):
        conexao = sqlite3.connect("usuarios.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT senha_hash FROM usuarios WHERE email = ?", (email,))
        resultado = cursor.fetchone()
        conexao.close()
        if resultado:
            senha_hash = resultado[0]
            if isinstance(senha_hash, str):
                senha_hash = senha_hash.encode('utf-8')
                if bcrypt.checkpw(senha_digitada.encode('utf-8'), senha_hash):
                    print("Login bem-sucedido.")
                    return True
                else:
                    print("Senha incorreta.")
                    return False
            else:
                print("Usuário não encontrado.")
                return False
            
def listar_usuarios():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT id, cpf, celular, nome, sobrenome, email, data_nascimento FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()
    if usuarios:
        print("\n=== Usuários cadastrados ===")
        for u in usuarios:
            print(u)
        else:
          print("Nenhum usuário cadastrado.")

# Menu interativo 

def painel():
    criar_tabela()
    while True:
        print("\n=== Painel de Usuários ===")
        print("1 - Cadastrar Usuário")
        print("2 - Logar Usuário")
        print("3 - Listar Usuários")
        print("0 - Sair")
        opcao = input(("Escolha uma opção: "))

        if opcao == "1":
            cpf  = input("CPF: ")
            celular = input("Celular: ")
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            email = input("Email: ")
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
            senha = input("Senha: ")
            cadastrar_usuario(cpf, celular, nome, sobrenome, email, data_nascimento, senha)

        elif opcao == "2":
            email = input("Email: ")
            senha = input("Senha: ")
            logar_usuario(email, senha)

        elif opcao == "3":
            listar_usuarios()

        elif opcao == "0":
            print("Saindo do painel.")
            break
        
        else: 
            print("Opção inválida!")

            if __name__ == "__main__":
                painel()