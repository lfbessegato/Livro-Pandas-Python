# P01: Hello Series
import pandas as pd

# Cria a Series Notas
notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.4])

# Cria a Series Alunos
lst_matriculas = ['M02', 'M05', 'M13', 'M14', 'M19']
lst_nomes = ['Bob', 'Dayse', 'Bill', 'Cris', 'Jimi']
alunos = pd.Series(lst_nomes, index=lst_matriculas)

# Imprime as duas Series
print(notas); print("---------------"); print(alunos)

##### Chaves de Dicionários
dic_alunos={'M02':'Bob','M05':'Dayse','M13':'Bill','M14':'Cris','M19':'Jimi'}
alunos = pd.Series(dic_alunos)
print(alunos)

