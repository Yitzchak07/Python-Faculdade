import pandas as pd
import matplotlib.pyplot as plt
import random
import seaborn as sn

# dados1 = random.sample(range(100),k=20)
# dados2 = random.sample(range(100),k=20)
# plt.plot(dados1,dados2)


# dados = {
#     'Produtos':["A","B","C"],
#     'qtde_vendidos':[33,50,45]
# }

# df = pd.DataFrame(dados)

# df.plot(x='Produtos',y='qtde_vendidos',kind='bar')
# df.plot(x='Produtos',y='qtde_vendidos',kind='pie')
# df.plot(x='Produtos',y='qtde_vendidos',kind='line')

sn.set(style='whitegrid')
df_tips = sn.load_dataset('tips')

print(df_tips)
fig, ax = plt.subplots(1,3,figsize=(15,5))

print(sn.barplot(data=df_tips,x='sex',y='total_bill',ax=ax[0]))

print(sn.barplot(data=df_tips,x='sex',y='total_bill',ax=ax[1],estimator=sum))

print(sn.barplot(data=df_tips,x='sex',y='total_bill',ax=ax[2],estimator=len))