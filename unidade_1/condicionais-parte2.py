from ola_mundo import Nome

nome = Nome()
user = nome.nome()
idade = int(input(f"Digite sua idade {user}:"))

if idade < 12:
    print(f"Filme 1 recomendado para Criancas {user}")
elif idade >= 12 and idade <18:
    print(f"Filme 2 recomendado para Adolescentes {user}")
else:
    print(f"Filme 3 recomendado para maiores de idade {user}")

compa_ingresso = int(input("Digite o total de ingressos que deseja comprar:"))

ingresso_disponiveis = 2
ingresso = (ingresso_disponiveis - compa_ingresso)

if compa_ingresso > ingresso_disponiveis:
    print(f"nao foi possivel numero de compra maior que o estoque, compra {compa_ingresso} estoque {ingresso_disponiveis} ")
else:
    print(f"compra efetuada com sucesso bom filme ")

if ingresso_disponiveis > 0:
    print(f"{ingresso} ingressos disponiveis, bom filme")
else:
    print(f"total de {ingresso_disponiveis} para o filme desculpe")