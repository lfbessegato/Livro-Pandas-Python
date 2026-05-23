#P12: Propriedades Básicas dos DataFrames
import pandas as pd

# Cria o DataFrame
dados = {'nome': ['Argentina', 'Brasil', 'França', 'Itália', 'Reino Unido'], 
         'continente': ['América', 'América', 'Europa', 'Europa', 'Europa'], 
         'extensão': [2780, 8511, 644, 301, 244], 
         'corVerde': [0, 1, 0, 1, 0]}

siglas = ['AR', 'BR', 'FR', 'IT', 'UK']

paises = pd.DataFrame(dados, index=siglas)

# Recupera e imprime as propriedades do DataFrame
print('----------------------------------------------------------------------')
num_linhas = paises.shape[0]
num_colunas = paises.shape[1]
indices = paises.index
colunas = paises.columns
paises_tipo = type(paises)
paises_dtypes = paises.dtypes
paises_idx_dtype = paises.index.dtype

print(f'Número de linhas: {num_linhas}')
print(f'Número de colunas: {num_colunas}')
print(f'Rótulos das linhas: {indices}')
print(f'Rótulos das colunas: {colunas}')
print(f'Tipo do objeto: {paises_tipo}')
print(f'Tipos de dados das colunas:\n{paises_dtypes}')
print(f'Tipo dos rótulos das linhas: {paises_idx_dtype}')