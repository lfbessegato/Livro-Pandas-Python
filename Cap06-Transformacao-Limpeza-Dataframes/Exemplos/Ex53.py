#P53: Método apply()
import pandas as pd 

#1-Importa as bases de dados 
flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags.csv')

#2-Apply
flags['name'] = flags['name'].apply(str.upper)

#3-Imprime o DataFrame alterado
print(flags)