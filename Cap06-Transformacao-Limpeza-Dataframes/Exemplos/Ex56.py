#P56: Normalização
import pandas as pd 

#1-Importa as bases de dados 
flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags.csv')

#2-Normaliza a área
area_max = max(flags['area'])
area_min = min(flags['area'])
flags['area_norm'] = (flags['area'] - area_min) / (area_max - area_min)

#3-Imprime o DataFrame Alterado
print(flags[['name', 
             'area', 
             'area_norm']])