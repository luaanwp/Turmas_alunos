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


def cadastrar(lista):
    print("\n=== CADASTRAR ALUNO ===")
    nome = input("Nome: ").strip()
    notas = input("Nota: ").strip()

    if nome == "" or notas == "":
        print("ERRO: Nome e nota não podem ficar vazios!")
        return
    if not notas.replace(".", "", 1).isdigit():
        print("ERRO: Nota deve ser um número!")
        return

    notas = float(notas)
    if notas < 0:
        print("ERRO: Nota não pode ser negativa!")
        return

    lista.append({"nome": nome, "notas": notas})
    print(f"Aluno {nome} cadastrado com sucesso!")

def listar(lista):
    print("\n=== LISTA DE ALUNOS ===")
    if not lista:
        print("Nenhum aluno cadastrado.")
        return
    for a in lista:
        print(f"Nome: {a['nome']} - Nota: {a['notas']}")

def buscar(lista):
    print("\n=== BUSCAR ALUNO ===")
    nome = input("Digite o nome do aluno: ").strip()
    for a in lista:
        if a["nome"].lower() == nome.lower():
            print(f"Aluno encontrado: {a['nome']} - Nota: {a['notas']}")
            return
    print("Aluno não encontrado.")

def atualizar(lista):
    print("\n=== ATUALIZAR ALUNO ===")
    nome = input("Digite o nome do aluno: ").strip()
    for a in lista:
        if a["nome"].lower() == nome.lower():
            nova_nota = input(f"Nova nota para {nome} (deixe em branco para não mudar): ").strip()
            if nova_nota != "":
                if nova_nota.replace(".", "", 1).isdigit():
                    a["notas"] = float(nova_nota)
                    print(f"Nota de {nome} atualizada com sucesso!")
                else:
                    print("ERRO: Nota inválida!")
            return
    print("Aluno não encontrado.")

def remover(lista):
    print("\n=== REMOVER ALUNO ===")
    nome = input("Digite o nome do aluno a remover: ").strip()
    for a in lista:
        if a["nome"].lower() == nome.lower():
            lista.remove(a)
            print(f"Aluno {nome} removido com sucesso!")
            return
    print("Aluno não encontrado.")

def media_turma(lista):
    if not lista:
        print("Nenhum aluno cadastrado.")
        return
    soma = sum(a["notas"] for a in lista)
    media = soma / len(lista)
    print(f"Média da turma: {media:.2f}")

def ordenar_por_nome(lista):
    lista.sort(key=lambda x: x["nome"].lower())
    print("Lista ordenada por nome.")
    listar(lista)


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
            media_turma(lista)
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
