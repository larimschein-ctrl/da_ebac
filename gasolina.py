import pandas as pd
import matplotlib.pyplot as plt

# Ler os dados
df = pd.read_csv("gasolina.csv")

# Criar o gráfico
plt.figure()
plt.plot(df["dia"], df["venda"])
plt.xlabel("Dia")
plt.ylabel("Preço da gasolina (R$)")
plt.title("Preço médio da gasolina - SP (Julho/2021)")

# Salvar o gráfico
plt.savefig("gasolina.png")
plt.close()
