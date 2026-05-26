#P39: Concatenção de DataFrames
import pandas as pd

#(1)-Cria os DataFrames com as vendas de cada loja  
lojaA = pd.DataFrame({"loja":["A", "A", "A"], 
                      "dia":["sex", "sáb", "dom"],
                      "valor": [7500, 9500, 8200]}
)

lojaB = pd.DataFrame({"loja":["B", "B", "B"], 
                      "dia":["sex", "sáb", "dom"],
                      "valor": [5100, 8250, 9900]}
)

lojaC = pd.DataFrame({"loja":["C", "C"], 
                      "dia":["sáb", "dom"],
                      "valor": [7500, 11000]}
)

#(2)-Concatena tudo em um único DataFrame
lojasABC = pd.concat([lojaA, lojaB, lojaC], ignore_index=True)
print(lojasABC)

