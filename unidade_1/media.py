from ola_mundo import Nome
nome = Nome().nome()
nota1 = float(input("Digite sua nota"))
nota2 = float(input("Digite sua nota"))
nota3 = float(input("Digite sua nota"))
nota4 = float(input("Digite sua nota"))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"{nome} sua media foi {media} ")
if media >= 6 :
    print("Aprovado")
else:
    print("Reprovado")