from db import execute_query, fetch_all
from datetime import datetime

def cadastrar_aluno():
    nome = input("Nome: ")

    cursos = ['Direito', 'História', 'Medicina', 'Matemática', 'Computação']
    print("\nCursos disponíveis:")
    for i, curso in enumerate(cursos, start=1):
        print(f"{i}. {curso}")

    escolha = int(input("Escolha o número do curso: "))
    if escolha < 1 or escolha > len(cursos):
        print("Curso inválido.")
        return

    curso = cursos[escolha - 1]

    # Gerar matrícula automática baseada na última inserida
    ano_atual = datetime.now().year
    prefixo = f"{ano_atual}%"
    sql = "SELECT matricula FROM Aluno WHERE matricula LIKE %s ORDER BY matricula DESC LIMIT 1"
    resultado = fetch_all(sql, (prefixo,))

    if resultado:
        ultima_matricula = int(resultado[0]['matricula'])
        proxima_matricula = ultima_matricula + 1
    else:
        proxima_matricula = int(f"{ano_atual}001")

    matricula = str(proxima_matricula)

    sql = "INSERT INTO Aluno (nome, curso, matricula) VALUES (%s, %s, %s)"
    execute_query(sql, (nome, curso, matricula))

    print(f"Aluno cadastrado com sucesso. Matrícula: {matricula}")

def listar_alunos():
    sql = "SELECT * FROM Aluno ORDER BY id_aluno"
    alunos = fetch_all(sql)

    if not alunos:
        print("Nenhum aluno encontrado.")
        return

    print("\n📋 Lista de Alunos\n")
    print(f"{'ID':<5} {'Nome':<20} {'Curso':<15} {'Matrícula'}")
    print("-" * 60)

    for aluno in alunos:
        print(f"{aluno['id_aluno']:<5} {aluno['nome']:<20} {aluno['curso']:<15} {aluno['matricula']}")

def atualizar_aluno():
    id_aluno = int(input("ID do Aluno: "))
    nome = input("Novo nome: ")

    cursos = ['Direito', 'História', 'Medicina', 'Matemática', 'Computação']
    print("\nCursos disponíveis:")
    for i, curso in enumerate(cursos, start=1):
        print(f"{i}. {curso}")

    escolha = int(input("Escolha o número do curso: "))
    if escolha < 1 or escolha > len(cursos):
        print("Curso inválido.")
        return

    curso = cursos[escolha - 1]

    sql = "UPDATE Aluno SET nome = %s, curso = %s WHERE id_aluno = %s"
    execute_query(sql, (nome, curso, id_aluno))
    print("Aluno atualizado com sucesso.")

def remover_aluno():
    id_aluno = int(input("ID do Aluno: "))

    # Remover inscrições antes de remover o aluno
    execute_query("DELETE FROM Inscricao WHERE id_aluno = %s", (id_aluno,))
    execute_query("DELETE FROM Aluno WHERE id_aluno = %s", (id_aluno,))
    print("Aluno removido com sucesso.")

def menu():
    while True:
        print("\n-- Menu Alunos --")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Remover")
        print("0. Voltar")
        escolha = input("Escolha: ")

        if escolha == "1":
            cadastrar_aluno()
        elif escolha == "2":
            listar_alunos()
        elif escolha == "3":
            atualizar_aluno()
        elif escolha == "4":
            remover_aluno()
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")
