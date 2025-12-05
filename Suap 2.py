alunos = []


def listar_aprovados():
    print("=====================================")
    print("\n--- Alunos Aprovados ---")
    print("---- Média (>= 7,0) ----")
    for aluno in alunos:
        if aluno["media"] >= 7:
            print(f"{aluno['nome']} - Nota: {aluno['media']}")
    print("=====================================")


def listar_reprovados():
    print("=====================================")
    print("--- Alunos Reprovados ---")
    print("---- Média (< 7,0) ----")
    for aluno in alunos:
        if aluno["media"] < 7:
            print(f"{aluno['nome']} - Nota: {aluno['media']}")
    print("=====================================")


def ordenar_por_nome():
    print("\n--- Alunos ordenados por nome ---")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        print("_")
        return

    ordenados = sorted(alunos, key=lambda a: a["nome"].lower())

    for aluno in ordenados:
        print(f"{aluno['nome']} - Nota: {aluno['media']}")

    print("================================================")



def remove():
    print("\n=============== REMOVER ALUNO ==================")
    matricula = input(
        "Digite a matrícula do aluno que deseja remover: ").strip()

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            alunos.remove(aluno)
            print(f"Aluno {aluno['nome']} removido com sucesso!")
            return
    print("Aluno não encontrado.")


def cadastrar():
    print("\n-------------- CADASTRAR ALUNO -----------------")

    # ---------------- MATRÍCULA ----------------
    while True:
        matricula = input(
            "Digite a matrícula do aluno (máx. 4 números): ").strip()

        if matricula == "":
            print("A matrícula não pode ficar vazia. Tente novamente.")
            continue

        if not matricula.isdigit():
            print("A matrícula deve conter apenas números.")
            continue

        if len(matricula) > 4:
            print("A matrícula deve ter NO MÁXIMO 4 dígitos.")
            continue

        todas = [a["matricula"] for a in alunos]
        if matricula in todas:
            print("Já existe um aluno com essa matrícula. Tente outra.")
            continue
        break

    nome = input("Nome: ").strip()
    if nome == "":
        nome = "Sem Nome"

    while True:
        idade_str = input("Idade: ").strip()
        if idade_str == "":
            idade = None
            break

        if idade_str.isdigit():
            idade = int(idade_str)
            break

        print("Idade inválida. Digite um número inteiro ou deixe vazio.")

    while True:
        media_str = input("Média (use ponto para decimal, ex: 7.5): ").strip()
        if media_str == "":
            media = 0.0
            break

        if media_str.count('.') <= 1:
            partes = media_str.split('.')
            if all(p.isdigit() or p == "" for p in partes):
                media = float(media_str)
                break

        print("Média inválida. Digite um número, ex: 7.5, ou deixe vazio.")

    novoAluno = {
        "matricula": matricula,
        "nome": nome,
        "idade": idade,
        "media": media
    }

    alunos.append(novoAluno)
    print(f"Aluno(a) '{nome}' cadastrado com sucesso!")


def listar():
    print("\n============== LISTA DE ALUNOS =================")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for a in alunos:
        idade = a.get("idade", "N/A")
        print(
            f"Matrícula: {a['matricula']} | Nome: {a['nome']} | Idade: {idade} | Média: {a['media']}")
    print("================================================")


def buscar():
    print("\n=============== BUSCAR ALUNO ===================")
    nome_busca = input("Digite o nome do aluno: ").strip().lower()

    for a in alunos:
        if a["nome"].lower() == nome_busca:
            idade = a.get("idade", "N/A")
            print("Aluno encontrado:")
            print(f"Nome: {a['nome']}")
            print(f"Matrícula: {a['matricula']}")
            print(f"Idade: {idade}")
            print(f"Média: {a['media']:.2f}")
            return

    print("Aluno não encontrado.")


def atualizar():
    print("\n============== ATUALIZAR ALUNO =================")
    nome_busca = input(
        "Digite o NOME do aluno que deseja atualizar: ").strip().lower()

    for a in alunos:
        if a["nome"].lower() == nome_busca:
            print(
                f"Atualizando aluno: {a['nome']} (matrícula {a['matricula']})")

            #  nome
            novo_nome = input(f"Novo nome [{a['nome']}](enter p/ manter): ").strip()
            if novo_nome:
                a["nome"] = novo_nome

            # idade
            idade_atual = a["idade"] if a["idade"] else "N/A"
            while True:
                nova_idade = input(
                    f"Nova idade [{idade_atual}] (enter p/ manter): "
                ).strip()
                if not nova_idade:
                    break
                if nova_idade.isdigit():
                    a["idade"] = int(nova_idade)
                    break
                print("Idade inválida. Digite um número inteiro.")

            # média
            while True:
                nova_media = input(
                    f"Nova média [{a['media']}] (enter p/ manter): "
                ).strip()
                if not nova_media:
                    break
                if nova_media.replace(".", "", 1).isdigit():
                    a["media"] = float(nova_media)
                    break
                print("Média inválida. Digite um número válido usando ponto.")

            print("Aluno atualizado com sucesso!")
            return

    print("Aluno não encontrado.")


def media_turma():
    print("\n============== MÉDIA DA TURMA ==================")
    if len(alunos) == 0:
        print("Não há alunos cadastrados.")
        return
    soma = 0.0
    for a in alunos:
        soma += a["media"]
    media = soma / len(alunos)
    print(f"Média da turma ({len(alunos)} aluno(s)): {media:.2f}")
    print("================================================")


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
        print("================================================")
        opcao = input("O que você deseja fazer?: ").strip()
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            atualizar()
        elif opcao == "5":
            remove()
        elif opcao == "6":
            listar_aprovados()
            listar_reprovados()
        elif opcao == "7":
            media_turma()
        elif opcao == "8":
            ordenar_por_nome()
        elif opcao == "0":
            print("Sessão finalizada.")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
