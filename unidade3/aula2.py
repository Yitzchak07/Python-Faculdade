import pandas as pd
# # Criando uma Lista de valores
# exemplo1 = [10,20,30,40,50]
# # Criando uma Series a partir da Lista

# series1 =  pd.Series(data = exemplo1)
# print(series1)

# exemplo2 = {"a":100,"b":200,"c":300,"d":400,"e":500}

# seires2 = pd.Series(data = exemplo2)
# print(seires2)

url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))

df_bancos = dfs[0]
print(df_bancos.shape)
print(df_bancos.dtypes)
print(df_bancos.head())