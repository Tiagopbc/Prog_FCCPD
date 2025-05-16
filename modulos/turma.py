from db import execute_query, fetch_all

def list_disciplinas():
    disciplinas = fetch_all("SELECT id_disc, nome FROM Disciplina")
    print("\n-- Disciplinas Disponíveis --")
    for d in disciplinas:
        print(f"{d[0]} - {d[1]}")
    return disciplinas

def list_professores():
    professores = fetch_all("SELECT id_prof, nome FROM Professor")
    print("\n-- Professores Disponíveis --")
    for p in professores:
        print(f"{p[0]} - {p[1]}")
    return professores

def create_turma():
    semestre = input("Semestre (ex: 2025.1): ")
    ano = input("Ano: ")

    list_disciplinas()
    id_disc = input("ID da Disciplina: ")

    list_professores()
    id_prof = input("ID do Professor: ")

    execute_query(
        "INSERT INTO Turma (semestre, ano, id_disc, id_prof) VALUES (%s, %s, %s, %s)",
        (semestre, ano, id_disc, id_prof)
    )
    print("Turma criada com sucesso.")

def list_turmas():
    turmas = fetch_all("""
        SELECT t.id_turma, t.semestre, t.ano, d.nome AS disciplina, p.nome AS professor
        FROM Turma t
        JOIN Disciplina d ON t.id_disc = d.id_disc
        JOIN Professor p ON t.id_prof = p.id_prof
    """)
    print("\n-- Lista de Turmas --")
    for t in turmas:
        print(f"ID: {t[0]}, Semestre: {t[1]}, Ano: {t[2]}, Disciplina: {t[3]}, Professor: {t[4]}")

def update_turma():
    id_turma = input("ID da Turma a atualizar: ")
    semestre = input("Novo semestre: ")
    ano = input("Novo ano: ")

    list_disciplinas()
    id_disc = input("Novo ID da Disciplina: ")

    list_professores()
    id_prof = input("Novo ID do Professor: ")

    execute_query(
        "UPDATE Turma SET semestre = %s, ano = %s, id_disc = %s, id_prof = %s WHERE id_turma = %s",
        (semestre, ano, id_disc, id_prof, id_turma)
    )
    print("Turma atualizada com sucesso.")

def delete_turma():
    id_turma = input("ID da Turma a remover: ")
    execute_query("DELETE FROM Turma WHERE id_turma = %s", (id_turma,))
    print("Turma removida com sucesso.")

def menu():
    print("\n-- Menu Turmas --")
    print("1. Cadastrar Turma")
    print("2. Listar Turmas")
    print("3. Atualizar Turma")
    print("4. Remover Turma")
    opcao = input("Escolha: ")
    if opcao == '1':
        create_turma()
    elif opcao == '2':
        list_turmas()
    elif opcao == '3':
        update_turma()
    elif opcao == '4':
        delete_turma()