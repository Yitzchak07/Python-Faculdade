confirmados = ['joao','bruna']
nao_confir = ['bia','julio']

print("Pessoas que ainda nao confirmaram sua presenca")
for pess in nao_confir:
    print(nao_confir)

    print("deseja Convidalas novamente?")

    opcao = str(input("S/N")).strip().upper()
    if opcao == "S":
        print(f"{nao_confir} foram convidados {len(nao_confir)}")
        confirmados.append(nao_confir)
        print(f"pessoas confirmadas na festas {confirmados}")
        break
    else:
        print(f"{nao_confir} nao foram convidados")
        break



