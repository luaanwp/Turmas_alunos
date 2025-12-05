def listar_aprovados(lista):
    print(f"\n--- Alunos Aprovados ---")
    print(f"\n---- Média (7,0) ---")
    for aluno in lista:
        if aluno["notas"] >= 7:
            print(f"{aluno['nome']} - Nota: {aluno['notas']}")
    print("------------------------------------")
def listar_reprovados(lista):
    print(f"\n--- Alunos Reprovados ---")
    print(f"\n--- Média (7,0) ---")
    for aluno in lista:
        if aluno ["notas"] <=6:
            print(f"{aluno['nome']} - Nota: {aluno['notas']}")
    print("------------------------------------")
## agora so chamar a função.