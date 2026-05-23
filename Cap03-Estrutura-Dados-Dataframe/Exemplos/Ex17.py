#P17: Importação de arquivo com serie temporal
import pandas as pd

# Importa o arquivo para um DataFrame
serie_gols = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/gols.txt', sep=" ", index_col=0)

# Converter o DataFrame para uma Series
series_gols = serie_gols.squeeze("columns")

# Converte o tipo do índice para datetime e imprime a série
series_gols.index = pd.to_datetime(series_gols.index, format='%d/%m/%Y')

print(series_gols)