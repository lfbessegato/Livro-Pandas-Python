#P30: Gráfico de uma função matemática
import matplotlib.pyplot as plt
import pandas as pd

# Gerar dados para a função y = 2x + 3
df = pd.DataFrame({'x': list(range(1, 11))})
df['y'] = 2 * df['x'] + 3
print(df)

# Criar o gráfico
lines = df.plot.line(x='x', y='y', title='Gráfico da função y = 2x + 3', legend=False)
plt.show()

