#P57: Normalização de atributo categórico
import pandas as pd 

#1-Importa as bases de dados
flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags.csv')

#2-Realiza a transformação com get_dummies() e join()
dummies = pd.get_dummies(flags['language'], prefix='lg')
flags = flags.join(dummies)

print(flags[["language", 
             "lg_1", 
             "lg_2", 
             "lg_3", 
             "lg_4", 
             "lg_5", 
             "lg_6", 
             "lg_7", 
             "lg_8", 
             "lg_9", 
             "lg_10"]])