#P22: Tipos de Atributos
import pandas as pd

# Cria o DataFrame "pme"
dados = {"renda": [6.46, 1.50, 0.00, 
                   2.57, 9.90, 6.22], 
         "empregos": [1,1,0,1,2,3], 
         "sexo": ["F","M","F","M","M","F"],
         "escolaridade": ["Pós-Graduaçãp","Fundamental", "Médio", "Médio", "Superior", "Médio"]
}

pme = pd.DataFrame(dados)

# Imprime o nome de cada atributo e seu dtype
print("\n Atributos e seus dtypes:")
print('-----------------------------')
print(pme.dtypes)