#P16: Importação CSV sem cabeçalho e com ";" como separador
import pandas as pd 

notas = pd.read_csv("/home/luciano/Documentos/Livro-Pandas-Python/repositorio/notas.csv", sep=";", 
                    names=['matricula', 'nota1', 'nota2'])

print(notas)