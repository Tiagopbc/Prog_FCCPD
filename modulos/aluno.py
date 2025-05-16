from db import execute_query, fetch_all

def create_aluno():
    nome = input("Nome: ")
    curso = input("Curso: ")
    matricula = input("Matrícula: ")
    execute_query(
        "INSERT INTO Aluno (nome, curso, matricula) VALUES (%s, %s, %s)",
        (nome, curso, matricula)
    )

def list_alunos():
    alunos = fetch_all("SELECT * FROM Aluno")
    for a in alunos:
        print(a)

def update_aluno():
    id_aluno = input("ID do Aluno: ")
    nome = input("Novo nome: ")
    curso = input("Novo curso: ")
    execute_query(
        "UPDATE Aluno SET nome = %s, curso = %s WHERE id_aluno = %s",
        (nome, curso, id_aluno)
    )

def delete_aluno():
    id_aluno = input("ID do Aluno: ")
    execute_query("DELETE FROM Aluno WHERE id_aluno = %s", (id_aluno,))

def menu():
    print("\n-- Menu Alunos --")
    print("1. Cadastrar")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Remover")
    opcao = input("Escolha: ")
    if opcao == '1':
        create_aluno()
    elif opcao == '2':
        list_alunos()
    elif opcao == '3':
        update_aluno()
    elif opcao == '4':
        delete_aluno()
