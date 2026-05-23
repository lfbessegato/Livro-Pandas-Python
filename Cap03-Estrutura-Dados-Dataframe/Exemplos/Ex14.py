#P14: Modificação de DataFrame
import pandas as pd

# Cria o DataFrame
dados = {'nome': ['Argentina', 'Brasil', 'França', 'Itália', 'Reino Unido'], 
         'continente': ['América', 'América', 'Europa', 'Europa', 'Europa'], 
         'extensão': [2780, 8511, 644, 301, 244], 
         'corVerde': [0, 1, 0, 1, 0]}

siglas = ['AR', 'BR', 'FR', 'IT', 'UK']

paises = pd.DataFrame(dados, index=siglas)

# Insere o País Japaão (JP)
paises.loc['JP'] = {'nome': 'Japão', 
                    'continente': 'Ásia', 
                    'extensão': 372, 
                    'corVerde': 0}

# Altera a extensão do Brasil
paises.at['BR', 'extensão'] = 8512

# Remove a Argentina e o Reino Unido
paises = paises.drop(['AR', 'UK'])

print('DataFrame após as alterações')
print(paises)