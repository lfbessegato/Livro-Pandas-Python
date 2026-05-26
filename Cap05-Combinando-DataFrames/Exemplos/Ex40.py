#P40: Concatenação de DataFrames Incompatíveis
import pandas as pd

#(1)-Cria dois DataFrames com definição diferente
d1 = pd.DataFrame({"Carro": ["Hyundai", "Renault", "Fiat"]})
d2 = pd.DataFrame({"Animal": ["Capivara", "Bem-Te-Vi"]})

#(2)-Concatena os DataFrames
d3 = pd.concat([d1, d2], ignore_index=True, sort=False)

print(d3)

