import numpy as np 
lista = np.array([1,2,3,4,5])

print("array Original")
print(lista)

lista_ao_quadrado = lista ** 2
soma = np.sum(lista)

print("\n ao quadrado")
print(lista_ao_quadrado)
print("\n soma dos elementos")
print(soma)

elementos = lista[2]
print(f"\n elemento no indice 2 {elementos}")