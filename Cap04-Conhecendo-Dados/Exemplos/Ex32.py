#P32: Gráfico de barras Horizontal
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame([70, 25, 50], 
                  index=['Teatro', "Escultura", "Pintura"])

barras = df.plot(kind='barh', legend=False)
plt.show()