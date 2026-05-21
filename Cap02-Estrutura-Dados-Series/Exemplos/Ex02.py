#P02: Propriedades básicas das Séries
import pandas as pd

# Cria a Series Alunos
alunos = pd.Series({'M02':'Bob', 'M05':'Dayse', 'M13':'Bill', 
                    'M14':'Cris', 'M19':'Jimi'})

# Atribui nomes p/ os vetores de dados e rótulos
alunos.name = "alunos"
alunos.index.name = "matrículas"

# Recupera e imprime as propriedades
print(alunos)
print('--------------')

tamanho = alunos.size
dados = alunos.values
rotulos = alunos.index
alunos_tipo = type(alunos)
alunos_dtype = alunos.dtype
alunos_idx_dtype = alunos.index.dtype

print('Número de Elementos: ', tamanho)
print('Vetor de dados: ', dados)
print('Vetor de Rótulos: ', rotulos)
print('Tipo (type): ', alunos_tipo)
print('dtype da Series: ', alunos_dtype)
print('dtype do Vetor de Rótulos: ', alunos_idx_dtype)