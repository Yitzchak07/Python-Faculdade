print("Avalie os Filmes")

filmes = ["vingadores","Fnf","invocacao do mal","freira","Transformes"] 
top = []
medio = []
ruim = []

for film in filmes:
    print(f"Nota de 0 A 10 Qual a nota para {film}")
    avalaliacao = int(input(f"Avalie o filme {film}:"))

    if avalaliacao >= 7:
        top.append(film)
    elif avalaliacao >= 4 and avalaliacao <= 6:
        medio.append(film)
    else:
        ruim.append(film)
    parar = str(input(f"S para parar/N para nao Parar")).upper().strip()

    if parar == "S":
        break
    else:
        continue

print(f"Filmes com as melhores Avaliacoes {top}")
print(f"Filmes com avaliacoes medias {medio}")
print(f"Filmes com Pessimas avaliacoes {ruim}")
    