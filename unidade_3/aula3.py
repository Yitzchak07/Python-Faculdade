import pandas as pd
from datetime import date
from datetime import datetime as dt
df_selic = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=26/08/2015&dataFinal=26/08/2025")

print(df_selic.info())

df_selic.drop_duplicates(keep='last',inplace=True)

data_extracao = date.today()
df_selic["data_extracao"] = data_extracao
df_selic["responsavel"] = "Autor"

print(df_selic.info)
print(df_selic.head())

print(df_selic.loc[9])
print(df_selic.loc[[0,20,70]])
teste = df_selic["valor"] < 0.01
print(type(teste))
print(teste)
