#P18: Importação de planilha Excel
import pandas as pd

cidades = pd.read_excel('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/capitais.xlsx')
print(cidades)

