#P52: Método replace()
import pandas as pd 

#1-Importa as bases de dados
flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags.csv')

#2-Replace
flags['green'] = flags['green'].replace([0,1],['Não', 'Sim'])

#3-Imprime o DataFrame alterado
print(flags[['name', 'green']])