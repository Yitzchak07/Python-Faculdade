import pandas as pd

data = {  
    'nome':["produto A","produto B","produto C","produto A","produto E"],
    'quantidade de Itens comprados':[3,1,4,3,2],
    'tipos de itens':["eletronicos","vestuario","alimentos","eletronico","alimentos"],
    'receita total':[120,80,60,120,90]


}   
df = pd.DataFrame(data)

print(df)

df.drop_duplicates(keep='last', inplace=True)

df['preco do item'] = df['receita total'] / df['quantidade de Itens comprados']

itens_acima = df[df["preco do item"] > 50.00]
print(itens_acima)
