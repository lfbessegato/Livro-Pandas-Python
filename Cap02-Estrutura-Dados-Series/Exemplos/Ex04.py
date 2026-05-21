# P04: Busca em Series
import pandas as pd 

# Cria a Serie "Alunos"
alunos = pd.Series({'M02':'Bob', 'M05':'Dayse', 'M13':'Bill',
                    'M14':'Cris', 'M19':'Jimi'})

# Testa se Rótulos fazem parte de uma Series
tem_M13 = 'M13' in alunos
tem_M99 = 'M99' in alunos
print("Existe o Rótulo 'M13'? -> ", tem_M13)
print("Existe o Rótulo 'M99'? -> ", tem_M99)
print('------------------------------------')

# Testa se o valor faz parte de uma Series
tem_Bob = alunos.isin(['Bob'])
print("Existe o valor 'Bob'")
print(tem_Bob) 
