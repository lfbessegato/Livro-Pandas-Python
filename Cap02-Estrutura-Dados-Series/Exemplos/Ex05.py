# P05: Inserindo, Alterando e Removendo elementos de Series
import pandas as pd 

# Cria a Series "Alunos"
alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill',
                    'M14':'Cris','M19':'Jimi'})

print('Series Original: ')
print(alunos)

# Insere o Aluno de Matrícula M55, Rakesh
alunos['M55'] = 'Rakesh'

# Altera os Nomes Bill, Cris e Jimi para Billy, Cristy e Jimmy
alunos['M13'] = 'Billy'
alunos[['M14','M19']] = ['Cristy','Jimmy']

# Remove o aluno de Matrícula M02 (Bob)
alunos = alunos.drop('M02')

print('----------------------------------------')
print('Series após as alterações:')
print(alunos)