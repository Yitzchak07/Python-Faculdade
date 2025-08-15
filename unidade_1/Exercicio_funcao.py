def media_aluno():
    while True:
        media = 0

        nota1 = float(input(f"digite a nota do aluno "))
        nota2 = float(input(f"digite a nota do aluno "))
        nota3 = float(input(f"digite a nota do aluno "))
        nota4 = float(input(f"digite a nota do aluno "))
            
        media = (nota1 + nota2 + nota3 + nota4) / 4 
        if media >= 6:
            print("Aluno aprovado")
        elif media >= 4 and media <= 5:
            print("recuperancao")
        else:
            print("reprovado")

        print("deseja Continuar S/N:")
        resp = str(input("Digite sua resposta:")).upper().strip()
        if resp == "S":
            print(f"media dos aluno foi {media} ")
            
            continue
        else:
            print(f"media dos aluno foi {media} ")
            break
    

media_aluno()
    