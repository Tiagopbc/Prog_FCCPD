from modulos import aluno, turma, inscricao

def main():
    while True:
        print("\nMenu Principal")
        print("1. Gerenciar Alunos")
        print("2. Gerenciar Turmas")
        print("3. Gerenciar Inscrições")
        print("4. Relatórios")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            aluno.menu()
        elif opcao == '2':
            turma.menu()
        elif opcao == '3':
            inscricao.menu()
        elif opcao == '4':
            inscricao.gerar_relatorios()
        elif opcao == '5':
            print("Encerrando.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
