#P38: Estudando a base de dados Flags
# III. Gráficos de barras com as frequências das cores
import pandas as pd
import matplotlib.pyplot as plt

#--------------------------------------------------------------
#(1)-Importa a base de dados
#---------------------------------------------------------------
flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags.csv')

#---------------------------------------------------------------
#(2)-Gera a tabela de frequências
#---------------------------------------------------------------
df_cores = pd.DataFrame()
for c in flags.columns:
    if c in ['red', 'green', 'blue', 'gold', 'white', 'black', 'orange']:
        df_cores[c]= flags[c].value_counts()

#---------------------------------------------------------------
#(3)-Gera os gráficos de barras
#---------------------------------------------------------------
lst_cores = ['red', 
             'green', 
             'blue', 
             'gold', 
             'whitesmoke', 
             'black', 
             'orange']

df_cores.plot(kind='barh',
              subplots=True, 
              figsize=(8,25),
              color = lst_cores)

plt.show()
