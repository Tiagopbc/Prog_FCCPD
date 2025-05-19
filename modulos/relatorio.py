from db import fetch_all

def listar_alunos_por_turma():
    sql = """
        SELECT t.id_turma, t.semestre, t.ano,
               d.nome AS disciplina,
               p.nome AS professor,
               a.id_aluno, a.nome AS nome_aluno, a.matricula
        FROM Turma t
        JOIN Disciplina d ON t.id_disc = d.id_disc
        JOIN Professor p ON t.id_prof = p.id_prof
        LEFT JOIN Inscricao i ON t.id_turma = i.id_turma
        LEFT JOIN Aluno a ON i.id_aluno = a.id_aluno
        ORDER BY t.id_turma, a.nome
    """
    dados = fetch_all(sql)

    if not dados:
        print("Nenhum dado encontrado.")
        return

    turma_atual = None
    for linha in dados:
        id_turma = linha['id_turma']
        nome_disc = linha['disciplina']
        professor = linha['professor']
        semestre = linha['semestre']
        ano = linha['ano']

        if id_turma != turma_atual:
            turma_atual = id_turma
            print(f"\n📘 Turma {id_turma} – {nome_disc} ({professor}, {ano}/{semestre})")
            print(f"{'ID':<5} {'Nome':<20} {'Matrícula'}")
            print("-" * 40)

        if linha['id_aluno']:
            print(f"{linha['id_aluno']:<5} {linha['nome_aluno']:<20} {linha['matricula']}")
        else:
            print("Nenhum aluno inscrito nessa turma.")

def listar_turmas_por_aluno():
    id_aluno = int(input("ID do Aluno: "))

    sql_nome = "SELECT nome FROM Aluno WHERE id_aluno = %s"
    aluno = fetch_all(sql_nome, (id_aluno,))
    if not aluno:
        print("Aluno não encontrado.")
        return

    nome = aluno[0]['nome']

    sql = """
        SELECT t.id_turma, t.semestre, t.ano, d.nome AS disciplina
        FROM Turma t
        JOIN Inscricao i ON t.id_turma = i.id_turma
        JOIN Disciplina d ON t.id_disc = d.id_disc
        WHERE i.id_aluno = %s
    """
    turmas = fetch_all(sql, (id_aluno,))

    if not turmas:
        print(f"Nenhuma turma encontrada para {nome}.")
        return

    print(f"\n🎓 Turmas de {nome}\n")
    print(f"{'ID':<5} {'Semestre':<10} {'Ano':<6} {'Disciplina'}")
    print("-" * 50)
    for t in turmas:
        print(f"{t['id_turma']:<5} {t['semestre']:<10} {t['ano']:<6} {t['disciplina']}")

def listar_turmas_com_detalhes():
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
        print("Nenhuma turma encontrada.")
        return

    print("\n📚 Turmas com Professor e Disciplina\n")
    print(f"{'ID':<5} {'Semestre':<10} {'Ano':<6} {'Disciplina':<20} {'Professor'}")
    print("-" * 70)
    for t in turmas:
        print(f"{t['id_turma']:<5} {t['semestre']:<10} {t['ano']:<6} {t['disciplina']:<20} {t['professor']}")

def listar_inscricoes_detalhadas():
    sql = """
        SELECT i.id_insc, a.nome AS aluno, a.matricula,
               d.nome AS disciplina, p.nome AS professor,
               t.semestre, t.ano, i.data_insc
        FROM Inscricao i
        JOIN Aluno a ON i.id_aluno = a.id_aluno
        JOIN Turma t ON i.id_turma = t.id_turma
        JOIN Disciplina d ON t.id_disc = d.id_disc
        JOIN Professor p ON t.id_prof = p.id_prof
        ORDER BY i.id_insc
    """
    inscricoes = fetch_all(sql)

    if not inscricoes:
        print("Nenhuma inscrição encontrada.")
        return

    print("\n📄 Inscrições Detalhadas\n")
    print(f"{'ID':<5} {'Aluno':<20} {'Matrícula':<10} {'Disciplina':<20} {'Professor':<15} {'Sem':<4} {'Ano':<6} {'Data'}")
    print("-" * 90)
    for i in inscricoes:
        print(f"{i['id_insc']:<5} {i['aluno']:<20} {i['matricula']:<10} {i['disciplina']:<20} {i['professor']:<15} {i['semestre']:<4} {i['ano']:<6} {i['data_insc']}")

def menu():
    while True:
        print("\n-- Menu de Relatórios --")
        print("1. Alunos por Turma")
        print("2. Turmas por Aluno")
        print("3. Listar Turmas com Professores e Disciplinas")
        print("4. Listar Inscrições Detalhadas")
        print("0. Voltar")
        escolha = input("Escolha: ")

        if escolha == "1":
            listar_alunos_por_turma()
        elif escolha == "2":
            listar_turmas_por_aluno()
        elif escolha == "3":
            listar_turmas_com_detalhes()
        elif escolha == "4":
            listar_inscricoes_detalhadas()
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")
