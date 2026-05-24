#P25 BoxPlot: Comparação de Distribuições
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Homens": [4, 2, 7, 3, 1, 4, 2, 4, 8, 1], 
    "Mulheres": [5, 4, 6, 5, 4, 2, 6, 6, 4, 3]
})

boxplot = df.boxplot(column=["Homens", "Mulheres"], 
                     showmeans = True)

plt.show()
