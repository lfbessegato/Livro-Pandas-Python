#P37: Estudando a base de dados Flags
# II. Cores e suas frequências nas bandeiras
import pandas as pd

#------------------------------------------------------------------------------
#(1)-Importa a base de dados
#------------------------------------------------------------------------------

flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags.csv')

#------------------------------------------------------------------------------
#(2)-Gera a tabela de frequências
#------------------------------------------------------------------------------

df_cores = pd.DataFrame()
for c in flags.columns:
    if c in ['red', 'green', 'blue', 'gold', 'white', 'black', 'orange']:
        df_cores[c]= flags[c].value_counts()

print(df_cores)
