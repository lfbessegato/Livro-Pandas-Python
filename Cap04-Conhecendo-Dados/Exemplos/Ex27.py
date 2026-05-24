#P27: Métodos sort_values() e rank()
import pandas as pd

#1-Cria o DataFrame da prova de 50m
dados = {"nadador": ["Simonas Bilis", 
                     "Benjamin Proud",
                     "Antony Ervin",
                     "Florent Manaudou",
                     "Audriy Hovorov",
                     "Nathan Adrian",
                     "Bruno Fratus",
                     "Brad Tandy"], 
        "nacionalidade": ["Lituânia",
                          "Reino Unido",
                          "Estados Unidos",
                          "França",
                          "Ucrânia",
                          "Estados Unidos",
                          "Brasil",
                          "África do Sul"],
        "tempo": [22.08, 
                  21.68, 
                  21.40, 
                  21.41,
                  21.74,
                  21.49,
                  21.79,
                  21.79]
}

raias = list(range(1,9))
             
prova50m = pd.DataFrame(dados, index=raias)
prova50m.index.name = 'raia'

#2-Ordena o DataFrame pelo tempo de forma crescente
prova50m.sort_values(by="tempo", inplace=True)
print(" * * Resultado final ordenado por tempo: ")
print(prova50m)

#3-Gera os rankings dos nadadores
resultado_por_raia = prova50m['tempo'].rank(method='min')
print("\n * * Posição de cada nadador (por raia): ")
print(resultado_por_raia) 
