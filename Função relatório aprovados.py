def listar_aprovados(lista):
    print(f"\n--- Alunos Aprovados ---")
    print(f"\n---- Média(7,0) ---")
    for aluno in lista:
        if aluno["notas"] >= 6:
            print(aluno["nome"])
