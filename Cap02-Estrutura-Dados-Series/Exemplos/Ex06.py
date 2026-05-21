# P06: Iteração
import pandas as pd 

alunos = pd.Series({'M02':'Bob', 'M05':'Dayse', 'M13':'Bill',
                    'M14':'Cris', 'M19':'Jimi'})

# Itera sobre os dados (nomes dos alunos)
for aluno in alunos: print(aluno)

# Itera sobre os indices (Matrículas)
for indice in alunos.index: print(indice)