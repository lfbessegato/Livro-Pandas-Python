#P55: Aplicando a função classe_area()
import pandas as pd 

#1-Define a função
def classe_area(area):
    if (area < 10):
        return 'F'
    elif (area >= 10 and area < 50):
        return 'E'
    elif (area >= 50 and area < 100):
        return 'D'
    elif (area >= 100 and area < 500):
        return 'C'
    elif (area >= 500 and area <1000):
        return 'B'
    else: 
        return 'A'
    
#2-Importa as bases de dados
flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags.csv')

#3-Aplica a função com apply(), criando novo atributo
flags['classe_area'] = flags['area'].apply(classe_area)

#4-Imprime o DataFrame alterado
print(flags[['name', 
             'area', 
             'classe_area'
            ]])