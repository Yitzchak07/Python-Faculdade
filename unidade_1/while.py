import ola_mundo
user = ola_mundo.Nome().nome()

num = int(input(f"digite um numero {user}:"))

while num != 0:
    if num %2 == 0:
        print("Numero par")
        break
    else:
        print("Numero impar")
        num = int(input(f"Digite um numero {user}:"))

        continue 
