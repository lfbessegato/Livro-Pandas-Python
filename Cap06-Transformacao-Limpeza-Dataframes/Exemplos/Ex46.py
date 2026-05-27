#P46: Seleção
import pandas as pd

#1-Importa as bases de dados
flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags.csv')

#2-Seleciona apenas as linhas dos países da oceania
v = (flags['landmass'] == 6)
flags_oceania = flags[v]

#3-Imprime os países da oceania
print(flags_oceania)
