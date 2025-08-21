class Pessoa:
    def __init__(self):
        self.nome = str(input("Digite seu nome:"))
        self.idade = int(input(f"Digite sua idade{self.nome}:"))
        self.Sexo = str(input(f"Digite seu sexo {self.nome}:")).upper()

    def aniversario(self):
        print(f"minha idade e {self.idade}")
        
    def cuumprimento(self):
        print(f"Ola me chamo {self.nome}")

        return print(self.nome,self.idade,self.Sexo,)
    
class Animal:

    def __init__(self,nome):
        self.nome = nome
    def faz_barulho(self):
        pass

class Cachorro(Animal):
    def faz_barulho(self):
        return "Latir"
class Gato(Animal):
    def faz_barulho(self):
        return "Miau"

rex = Cachorro("Rex")
miu = Gato("miu")
print(f"{rex.nome} Faz: {rex.faz_barulho()}")
print(f"{miu.nome} Faz: {miu.faz_barulho()}")
