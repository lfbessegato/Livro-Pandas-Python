#P42: Comparação de DataFrames
import pandas as pd 

#(1)-Cria três DataFrames de Filmes
filmes1 = pd.DataFrame({"titulo": ["O Filho da Noiva", 
                                  "La La Land"], 
                        "ano": [2001, 
                                2017]})

filmes2 = pd.DataFrame({"titulo": ["Noel, Poeta da Vila", 
                                  "La La Land"], 
                        "ano": [2007, 
                                2017]})

filmes3 = pd.DataFrame({"titulo": ["O Filho da Noiva", 
                                  "La La Land"], 
                                  "ano": [2001, 
                                          2017]})

#(2)-Verifica quais DataFrames são iguais
# (possuem o mesmo conteúdo)
print('filmes1 são iguais à filmes2 -> ', filmes1.equals(filmes2))
print('filmes1 são iguais à filmes3 -> ', filmes1.equals(filmes3))