alunos = [{"matricula": "001", "nome": "João", "idade": 20, "media": 7.5},
    {"matricula": "002", "nome": "Maria", "idade": 22, "media": 8.0}]

def remove():
    print("\n=== REMOVER ALUNO ===")
    matricula = input("Digite a matrícula do aluno que deseja remover: ")

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            alunos.remove(aluno)
            print(f"Aluno {aluno['nome']} removido com sucesso!")
            return

    print("Aluno não encontrado.")
remove()
