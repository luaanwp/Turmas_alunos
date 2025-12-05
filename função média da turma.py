soma = 0
def media(notas):

    print("--------- Média da turma ---------")
    for nota in notas:

        soma += nota

    media_total = soma / len(notas)
    print(f"Média da turma: {media_total:.2f} ")  
print("------------------------------------")    