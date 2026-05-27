#P51: Exclusão
import pandas as pd 

#1-Importa as bases de dados
flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags.csv')

#2-Mantém apenas os países com verde, amarelo, azul e branco na bandeira
flags = flags.loc[(flags['green'] == 1) & 
                   (flags['gold'] == 1) & 
                   (flags['blue'] == 1) & 
                   (flags['white'] == 1)]

#3-Imprime o DataFrame alterado
print(flags[['name', 
             'green', 
             'gold', 
             'blue', 
             'white']])

