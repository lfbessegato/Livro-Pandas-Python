#P23: Estatísticas Básicas: Medidas de Tendência Central
import pandas as pd

# Cria o DataFrame
dados = {"jogador": ["Marcelo", 
                     "Pedro", 
                     "Marcelo", 
                     "Adriano", 
                     "Mauro", 
                     "Pedro", 
                     "Marcelo"], 
                     
        "infracao": ["FALTA VIOLENTA",
                     "RECLAMAÇÃO",
                     "FALTA COMUM",
                     "RECLAMAÇÃO",
                     "FALTA COMUM",
                     "FALTA VIOLENTA", 
                     "RECLAMAÇÃO"], 
        "punição": [4,1,3,2,4,4,2]
}

df = pd.DataFrame(dados)

# Calcula as medidas de Tendência Central
print("Média:", df["punição"].mean())
print("Mediana:", df["punição"].median())
print("Moda:", df["punição"].mode().values)