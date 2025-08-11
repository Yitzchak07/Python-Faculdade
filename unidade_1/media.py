from unidade_1.ola_mundo import Nome
nome = Nome()
aluno = nome.nome()
nota1 = float(input("Digite sua nota"))
nota2 = float(input("Digite sua nota"))
nota3 = float(input("Digite sua nota"))
nota4 = float(input("Digite sua nota"))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"{aluno} sua media foi {media} ")
if media >= 6 :
    print("Aprovado")
else:
    print("Reprovado")