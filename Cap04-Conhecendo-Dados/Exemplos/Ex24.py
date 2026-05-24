#P24: Estatísticas Básicas: Medidas de Variabilidade
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
        "juiz_A": [4,1,3,2,4,4,2],
        "juiz_B": [2,1,4,1,1,5,6]
}

df = pd.DataFrame(dados)

# Calcula as medidas de Variabilidade
print("Juiz A:")
print("----------------")
print("Amplitude: ", df["juiz_A"].max() - df["juiz_A"].min())
print("Desvio Padrão: ", df["juiz_A"].std())
print("Variância: ", df["juiz_A"].var())

print("\nJuiz B:")
print("----------------")
print("Amplitude: ", df["juiz_B"].max() - df["juiz_B"].min())
print("Desvio Padrão: ", df["juiz_B"].std())
print("Variância: ", df["juiz_B"].var())    

