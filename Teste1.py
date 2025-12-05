a1 = {"nome": "João", "notas": 8.5}

def listar_aprovados(lista):
    print("=====================================")
    print("\n--- Alunos Aprovados ---")
    print("---- Média (>= 7,0) ----")
    for aluno in lista:
        if aluno["notas"] >= 7:
            print(f"{aluno['nome']} - Nota: {aluno['notas']}")
    print("=====================================")


def listar_reprovados(lista):
    print("=====================================")
    print("--- Alunos Reprovados ---")
    print("---- Média (< 7,0) ----")
    for aluno in lista:
        if aluno["notas"] < 7:
            print(f"{aluno['nome']} - Nota: {aluno['notas']}")
    print("=====================================")


def cadastrar(lista): pass
def listar(lista): pass
def buscar(lista): pass
def atualizar(lista): pass
def remover(lista): pass
def media(lista):
    print("--------- Média da turma ---------")

    if not lista:
        print("Nenhum aluno cadastrado.")
        return
    
    soma = 0
    for aluno in lista:
        soma += aluno["notas"]

    media_total = soma / len(lista)
    print(f"Média da turma: {media_total:.2f}")

    print("------------------------------------")
    input("Pressione ENTER para continuar...")

def ordenar_por_nome(lista): pass


def menu():
    while True:
        print("\n===== SISTEMA DE TURMA E ALUNOS (SUAP 2.0) =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar aluno")
        print("4 - Atualizar dados do aluno")
        print("5 - Remover aluno")
        print("6 - Relatório: Aprovados e Reprovados")
        print("7 - Relatório: Média da turma")
        print("8 - Relatório: Ordenar por nome")
        print("0 - Sair")
        print("=====================================")
        opcao = input("O que você deseja fazer?: ").strip()
        if opcao == "1":
            cadastrar(lista)
        elif opcao == "2":
            listar(lista)
        elif opcao == "3":
            buscar(lista)
        elif opcao == "4":
            atualizar(lista)
        elif opcao == "5":
            remover(lista)
        elif opcao == "6":
            listar_aprovados(lista)
            listar_reprovados(lista)
        elif opcao == "7":
            media(lista)
        elif opcao == "8":
            ordenar_por_nome(lista)
        elif opcao == "0":
            print("Sessão finalizada.")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    lista = [a1]
    menu()
