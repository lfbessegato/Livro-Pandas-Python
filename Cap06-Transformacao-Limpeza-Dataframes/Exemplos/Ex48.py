#P48: Método 'reset_index()'
import pandas as pd 

#1-Importa as bases de dados
flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags.csv')

#2-Seleciona apenas as linhas dos países da oceania
# com área acima de 200 mil quilômetros quadrados
v = (flags['landmass'] == 6) & (flags['area'] > 200)
df = flags[v]

#3-Projeta apenas as colunas "name", "colours", "language", "landmass" e "area"
df = df[['name', 'colours', 'language', 'landmass', 'area']]

#4-Reseta os indices
df = df.reset_index(drop=True)

#5-Imprime o resultado
print(df)