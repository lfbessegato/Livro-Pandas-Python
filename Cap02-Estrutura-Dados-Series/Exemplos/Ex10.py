#P10: Indexação Hieráquica 
import pandas as pd 

moedas = ['Peso', 'Real', 'Euro', 'Euro', 'Libra']
paises = [['América', 'América', 'Europa', 'Europa', 'Europa'], 
          ['AR', 'BR', 'FR', 'IT', 'UK']]

paises = pd.Series(moedas, index=paises)

print(paises) # Imprime toda a Series
print('-----------------------')
print(paises['América']) # {AR: Peso, BR: Real}
print('-----------------------')
print(paises[:, 'IT']) # {Europa: Euro}
print('-----------------------')
print(paises['Europa', 'IT']) # Euro