import seaborn as sn
import matplotlib.pyplot as plt

sn.set(style='whitegrid')

df = sn.load_dataset('tips')

plt.figure(figsize=(8,5))
sn.barplot(x='time',y='total_bill',data=df,estimator=sum,ci=None,palette="Set2")
plt.xlabel('Periodo (Time)')
plt.ylabel('Total de Gastos')
plt.title("total de gastos por periodo (Almoco ou Jantar)")
plt.show()