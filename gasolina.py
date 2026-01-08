import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("gasolina.csv")

plt.figure()
sns.lineplot(x="dia", y="venda", data=df)
plt.title("Preço médio da gasolina - SP (Julho/2021)")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")

plt.savefig("gasolina.png")
plt.close()
