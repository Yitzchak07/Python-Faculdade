import pandas as pd
# Criando um Dicionario
dados = {'nome':["isac","luis","Ramon","marko"],
         'idade':[18,17,17,14]
}
# Criando uma serie a partir do Dicionario
series_idade = pd.Series(dados["idade"],index = dados["nome"])
# mostrando o resultador da idade,e idade madia dentre as pessoas 

print("\n Series de Idades")
print("\n",series_idade)


media_idade = series_idade.mean()
print(f"\n Idade Media {media_idade}")