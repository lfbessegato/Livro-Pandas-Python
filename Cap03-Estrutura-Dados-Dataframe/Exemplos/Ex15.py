#P15: Importação de CSV padrão para um DataFrame
import pandas as pd

paises = pd.read_csv("/home/luciano/Documentos/Livro-Pandas-Python/repositorio/paises.csv", index_col="sigla")
print(paises) 