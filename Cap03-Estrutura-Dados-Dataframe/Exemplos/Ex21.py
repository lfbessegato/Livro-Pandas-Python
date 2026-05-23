#P21: Quais os paises  que também têm verde, amarelo, azul e 
# branco entre as cores de sua bandeira nacional?
import pandas as pd

#-----------------------------------------------------------------------
# (1)-Importa a base de dados
#-----------------------------------------------------------------------
flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags.csv')

#-----------------------------------------------------------------------
# (2)-Alguns métodos para obter informações básicas
#-----------------------------------------------------------------------
# Imprime as primeiras linhas
print('head():'); print(flags.head())
print('---------------------------------------------------------------')
# Imprime as últimas linhas
print('tail():'); print(flags.tail())
print('---------------------------------------------------------------')

#-----------------------------------------------------------------------
# (3)-Quem tem verde, amarelo, azul e branco entre as cores na bandeira?
#-----------------------------------------------------------------------
# Separa as cores
verde = flags['green']
amarelo = flags['gold']
azul = flags['blue']
branco = flags['white']

soma = verde + amarelo + azul + branco

# Gera o vetor booleano com True para quem tem as 4 cores
tem_todas = (soma == 4)

# Imprime os noms dos países com as quatro cores
print('Paises com verde, amarelo, azul e branco na bandeira:')
print(flags[tem_todas.values]['name'])