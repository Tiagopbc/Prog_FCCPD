from db import execute_query, fetch_all

def listar_turmas():
    sql = """
        SELECT t.id_turma, t.semestre, t.ano,
               d.nome AS disciplina,
               p.nome AS professor
        FROM Turma t
        JOIN Disciplina d ON t.id_disc = d.id_disc
        JOIN Professor p ON t.id_prof = p.id_prof
        ORDER BY t.id_turma
    """
    turmas = fetch_all(sql)

    if not turmas:
        print("Nenhuma turma cadastrada.")
        return

    print("\n📚 Lista de Turmas\n")
    print(f"{'ID':<5} {'Semestre':<10} {'Ano':<6} {'Disciplina':<20} {'Professor'}")
    print("-" * 60)

    for turma in turmas:
        print(f"{turma['id_turma']:<5} {turma['semestre']:<10} {turma['ano']:<6} {turma['disciplina']:<20} {turma['professor']}")

def cadastrar_turma():
    semestre = input("Semestre: ")
    ano = int(input("Ano: "))

    # Listar disciplinas
    disciplinas = fetch_all("SELECT id_disc, nome FROM Disciplina ORDER BY id_disc")
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return

    print("\nDisciplinas disponíveis:")
    for d in disciplinas:
        print(f"{d['id_disc']}. {d['nome']}")

    id_disc = int(input("Escolha o ID da disciplina: "))

    # Listar professores
    professores = fetch_all("SELECT id_prof, nome FROM Professor ORDER BY id_prof")
    if not professores:
        print("Nenhum professor cadastrado.")
        return

    print("\nProfessores disponíveis:")
    for p in professores:
        print(f"{p['id_prof']}. {p['nome']}")

    id_prof = int(input("Escolha o ID do professor: "))

    sql = """
        INSERT INTO Turma (semestre, ano, id_disc, id_prof)
        VALUES (%s, %s, %s, %s)
    """
    execute_query(sql, (semestre, ano, id_disc, id_prof))
    print("Turma cadastrada com sucesso.")

def atualizar_turma():
    id_turma = int(input("ID da Turma a atualizar: "))

    semestre = input("Novo semestre: ")
    ano = int(input("Novo ano: "))

    disciplinas = fetch_all("SELECT id_disc, nome FROM Disciplina ORDER BY id_disc")
    print("\nDisciplinas disponíveis:")
    for d in disciplinas:
        print(f"{d['id_disc']}. {d['nome']}")
    id_disc = int(input("Escolha o ID da disciplina: "))

    professores = fetch_all("SELECT id_prof, nome FROM Professor ORDER BY id_prof")
    print("\nProfessores disponíveis:")
    for p in professores:
        print(f"{p['id_prof']}. {p['nome']}")
    id_prof = int(input("Escolha o ID do professor: "))

    sql = """
        UPDATE Turma SET semestre = %s, ano = %s,
        id_disc = %s, id_prof = %s
        WHERE id_turma = %s
    """
    execute_query(sql, (semestre, ano, id_disc, id_prof, id_turma))
    print("Turma atualizada com sucesso.")

def remover_turma():
    id_turma = int(input("ID da Turma: "))

    # Remover inscrições antes
    execute_query("DELETE FROM Inscricao WHERE id_turma = %s", (id_turma,))
    execute_query("DELETE FROM Turma WHERE id_turma = %s", (id_turma,))
    print("Turma removida com sucesso.")

def menu():
    while True:
        print("\n-- Menu Turmas --")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Remover")
        print("0. Voltar")
        escolha = input("Escolha: ")

        if escolha == "1":
            cadastrar_turma()
        elif escolha == "2":
            listar_turmas()
        elif escolha == "3":
            atualizar_turma()
        elif escolha == "4":
            remover_turma()
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")
