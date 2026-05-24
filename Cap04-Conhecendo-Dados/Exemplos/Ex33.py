#P33: Gráfico de barras agrupadas
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({"Mulheres": [40, 10, 30], 
                   "Homens": [30, 15, 20]},
                   index=["Teatro", "Escultura", "Pintura"])


barras = df.plot(kind="bar", legend=True, color=["yellow", "blue"])

plt.show()