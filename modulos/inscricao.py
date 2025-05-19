from db import execute_query, fetch_all

def inscrever_aluno():
    id_aluno = int(input("ID do Aluno: "))
    id_turma = int(input("ID da Turma: "))
    sql = "INSERT INTO Inscricao (id_aluno, id_turma) VALUES (%s, %s)"
    execute_query(sql, (id_aluno, id_turma))
    print("Aluno inscrito com sucesso!")

def cancelar_inscricao():
    id_aluno = int(input("ID do Aluno: "))
    id_turma = int(input("ID da Turma: "))
    sql = "DELETE FROM Inscricao WHERE id_aluno = %s AND id_turma = %s"
    execute_query(sql, (id_aluno, id_turma))
    print("Inscrição cancelada com sucesso.")

def listar_por_turma():
    id_turma = int(input("ID da Turma: "))
    sql = """
        SELECT a.id_aluno, a.nome, a.matricula
        FROM Aluno a
        JOIN Inscricao i ON a.id_aluno = i.id_aluno
        WHERE i.id_turma = %s
    """
    alunos = fetch_all(sql, (id_turma,))

    if not alunos:
        print(f"\nNenhum aluno encontrado para a turma {id_turma}.\n")
        return

    print(f"\n📋 Alunos da Turma {id_turma}\n")
    print(f"{'ID':<5} {'Nome':<20} {'Matrícula'}")
    print("-" * 40)

    for aluno in alunos:
        print(f"{aluno['id_aluno']:<5} {aluno['nome']:<20} {aluno['matricula']}")

def listar_por_aluno():
    id_aluno = int(input("ID do Aluno: "))

    # Buscar o nome do aluno
    sql_nome = "SELECT nome FROM Aluno WHERE id_aluno = %s"
    resultado = fetch_all(sql_nome, (id_aluno,))

    if not resultado:
        print(f"\nAluno com ID {id_aluno} não encontrado.\n")
        return

    nome_aluno = resultado[0]['nome']

    # Buscar as turmas
    sql = """
        SELECT t.id_turma, t.semestre, t.ano, d.nome AS disciplina
        FROM Turma t
        JOIN Inscricao i ON t.id_turma = i.id_turma
        JOIN Disciplina d ON t.id_disc = d.id_disc
        WHERE i.id_aluno = %s
    """
    turmas = fetch_all(sql, (id_aluno,))

    if not turmas:
        print(f"\nNenhuma turma encontrada para o aluno {nome_aluno}.\n")
        return

    print(f"\n🎓 Turmas de {nome_aluno}\n")
    print(f"{'ID':<5} {'Semestre':<10} {'Ano':<6} {'Disciplina'}")
    print("-" * 50)

    for turma in turmas:
        print(f"{turma['id_turma']:<5} {turma['semestre']:<10} {turma['ano']:<6} {turma['disciplina']}")

def menu():
    while True:
        print("\n-- Menu Inscrições --")
        print("1. Inscrever Aluno")
        print("2. Cancelar Inscrição")
        print("3. Listar por Turma")
        print("4. Listar por Aluno")
        print("0. Voltar")
        escolha = input("Escolha: ")

        if escolha == "1":
            inscrever_aluno()
        elif escolha == "2":
            cancelar_inscricao()
        elif escolha == "3":
            listar_por_turma()
        elif escolha == "4":
            listar_por_aluno()
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")
