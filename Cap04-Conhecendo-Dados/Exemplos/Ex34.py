#P34: Histograma
import pandas as pd
import matplotlib.pyplot as plt
       
df = pd.DataFrame({
    "Tempo":[4,5,1,7,7,8,6,6,5,
             2,5,8,7,1,6,3,4,8,
             5,7,4,6,3,6,2,6,8]
})

hist = df.plot(kind="hist", bins=3)
plt.show()