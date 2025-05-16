from db import execute_query, fetch_all
import psycopg2

def inscrever_aluno():
    print("\nAlunos disponíveis:")
    alunos = fetch_all("SELECT * FROM Aluno")
    for a in alunos:
        print(a)

    print("\nTurmas disponíveis:")
    turmas = fetch_all("SELECT * FROM Turma")
    for t in turmas:
        print(t)

    id_aluno = input("ID do Aluno: ")
    id_turma = input("ID da Turma: ")

    try:
        execute_query(
            "INSERT INTO Inscricao (id_aluno, id_turma) VALUES (%s, %s)",
            (id_aluno, id_turma)
        )
        print("Inscrição realizada com sucesso.")
    except psycopg2.errors.UniqueViolation:
        print("Erro: aluno já inscrito nessa turma.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def cancelar_inscricao():
    inscricoes = fetch_all("""
        SELECT i.id_insc, a.nome AS aluno, t.id_turma
        FROM Inscricao i
        JOIN Aluno a ON i.id_aluno = a.id_aluno
        JOIN Turma t ON i.id_turma = t.id_turma
    """)
    for i in inscricoes:
        print(i)

    id_insc = input("ID da inscrição a cancelar: ")
    execute_query("DELETE FROM Inscricao WHERE id_insc = %s", (id_insc,))
    print("Inscrição cancelada.")

def listar_por_turma():
    id_turma = input("ID da Turma: ")
    alunos = fetch_all("""
        SELECT a.id_aluno, a.nome, a.matricula
        FROM Inscricao i
        JOIN Aluno a ON i.id_aluno = a.id_aluno
        WHERE i.id_turma = %s
    """, (id_turma,))
    for a in alunos:
        print(a)

def listar_por_aluno():
    id_aluno = input("ID do Aluno: ")
    turmas = fetch_all("""
        SELECT t.id_turma, d.nome AS disciplina, p.nome AS professor
        FROM Inscricao i
        JOIN Turma t ON i.id_turma = t.id_turma
        JOIN Disciplina d ON t.id_disc = d.id_disc
        JOIN Professor p ON t.id_prof = p.id_prof
        WHERE i.id_aluno = %s
    """, (id_aluno,))
    for t in turmas:
        print(t)

def gerar_relatorios():
    print("\n-- Relatórios --")
    print("1. Alunos por Turma")
    print("2. Turmas por Aluno")
    opcao = input("Escolha: ")
    if opcao == '1':
        listar_por_turma()
    elif opcao == '2':
        listar_por_aluno()

def menu():
    print("\n-- Menu Inscrições --")
    print("1. Inscrever Aluno")
    print("2. Cancelar Inscrição")
    print("3. Listar por Turma")
    print("4. Listar por Aluno")
    opcao = input("Escolha: ")
    if opcao == '1':
        inscrever_aluno()
    elif opcao == '2':
        cancelar_inscricao()
    elif opcao == '3':
        listar_por_turma()
    elif opcao == '4':
        listar_por_aluno()