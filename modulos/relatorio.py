from db import fetch_all

def listar_alunos_por_turma():
    id_turma = input("ID da Turma: ")
    alunos = fetch_all("""
        SELECT a.id_aluno, a.nome, a.matricula
        FROM Inscricao i
        JOIN Aluno a ON i.id_aluno = a.id_aluno
        WHERE i.id_turma = %s
    """, (id_turma,))
    
    print("\n-- Alunos da Turma --")
    for a in alunos:
        print(f"ID: {a[0]}, Nome: {a[1]}, Matrícula: {a[2]}")

def listar_turmas_por_aluno():
    id_aluno = input("ID do Aluno: ")
    turmas = fetch_all("""
        SELECT t.id_turma, d.nome AS disciplina, p.nome AS professor, t.semestre, t.ano
        FROM Inscricao i
        JOIN Turma t ON i.id_turma = t.id_turma
        JOIN Disciplina d ON t.id_disc = d.id_disc
        JOIN Professor p ON t.id_prof = p.id_prof
        WHERE i.id_aluno = %s
    """, (id_aluno,))
    
    print("\n-- Turmas do Aluno --")
    for t in turmas:
        print(f"Turma ID: {t[0]}, Disciplina: {t[1]}, Professor: {t[2]}, Semestre: {t[3]}, Ano: {t[4]}")

def listar_turmas_com_professores_disciplinas():
    turmas = fetch_all("""
        SELECT t.id_turma, t.semestre, t.ano, d.nome AS disciplina, p.nome AS professor
        FROM Turma t
        JOIN Disciplina d ON t.id_disc = d.id_disc
        JOIN Professor p ON t.id_prof = p.id_prof
    """)
    
    print("\n-- Turmas com Disciplinas e Professores --")
    for t in turmas:
        print(f"ID: {t[0]}, Semestre: {t[1]}, Ano: {t[2]}, Disciplina: {t[3]}, Professor: {t[4]}")

def listar_inscricoes_detalhadas():
    inscricoes = fetch_all("""
        SELECT i.id_insc, a.nome AS aluno, d.nome AS disciplina, p.nome AS professor, t.semestre, t.ano
        FROM Inscricao i
        JOIN Aluno a ON i.id_aluno = a.id_aluno
        JOIN Turma t ON i.id_turma = t.id_turma
        JOIN Disciplina d ON t.id_disc = d.id_disc
        JOIN Professor p ON t.id_prof = p.id_prof
        ORDER BY i.id_insc
    """)
    
    print("\n-- Todas as Inscrições Detalhadas --")
    for i in inscricoes:
        print(f"Inscrição: {i[0]}, Aluno: {i[1]}, Disciplina: {i[2]}, Professor: {i[3]}, Semestre: {i[4]}, Ano: {i[5]}")

def menu():
    print("\n-- Menu de Relatórios --")
    print("1. Alunos por Turma")
    print("2. Turmas por Aluno")
    print("3. Listar Turmas com Professores e Disciplinas")
    print("4. Listar Inscrições Detalhadas")
    
    opcao = input("Escolha: ")
    if opcao == '1':
        listar_alunos_por_turma()
    elif opcao == '2':
        listar_turmas_por_aluno()
    elif opcao == '3':
        listar_turmas_com_professores_disciplinas()
    elif opcao == '4':
        listar_inscricoes_detalhadas()
    else:
        print("Opção inválida.")