#P13: Busca em DataFrames
import pandas as pd

# Cria o DataFrame
dados = {'nome': ['Argentina', 'Brasil', 'França', 'Itália', 'Reino Unido'], 
         'continente': ['América', 'América', 'Europa', 'Europa', 'Europa'], 
         'extensão': [2780, 8511, 644, 301, 244], 
         'corVerde': [0, 1, 0, 1, 0]}

siglas = ['AR', 'BR', 'FR', 'IT', 'UK']

paises = pd.DataFrame(dados, index=siglas)

# Testa se um dado rótulo de linha existe
print('----------------------------------------------------------------------')
tem_BR = 'BR' in paises.index
tem_US = 'US' in paises.index
print(f'Existe o rótulo "BR" no índice? {tem_BR}')
print(f'Existe o rótulo "US" no índice? {tem_US}')
print('----------------------------------------------------------------------')

# Testa se um dado rótulo de coluna existe
tem_corVerde = 'corVerde' in paises.columns
tem_corAzul = 'corAzul' in paises.columns
print(f'Existe o Rótulo da Coluna "corVerde"? {tem_corVerde}') 
print(f'Existe o Rótulo da Coluna "corAzul"? {tem_corAzul}')
print('----------------------------------------------------------------------') 

# Testa se o valor faz parte de uma coluna
tem_Brasil = paises['nome'].isin(['Brasil'])
print(f'Existe o valor "Brasil" na coluna "nome"? {tem_Brasil}')
print(tem_Brasil)