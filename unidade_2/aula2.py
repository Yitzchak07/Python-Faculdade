meu_conjunto = set()

meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)
print(meu_conjunto)

elemento = 20
if elemento in meu_conjunto:
    print(f"{elemento} esta no conjunto")
else:
    print(f"{elemento} nao esta no conjunto")
meu_conjunto.remove(20)
print(f"conjunto apos remover o elemento 20 {meu_conjunto}")