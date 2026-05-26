#P45: Comparação entre as bases flags.csv e countries.csv
import pandas as pd 

#----------------------------------------------------------------
#(1)-Importa as base de dados
#----------------------------------------------------------------
flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags.csv')
countries = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/countries.csv')

num_linhas_flags = flags.shape[0]
num_linhas_countries = countries.shape[0]

#---------------------------------------------------------------
#(2)-Realiza a junção entre os DataFrames
#---------------------------------------------------------------

#2.1 - Junção Interna: paises comuns a ambas as bases
ambas = pd.merge(flags, countries, 
                 how="inner", 
                 left_on="name", right_on="country")

num_linhas_ambas = ambas.shape[0]

#2.2 - Left Join: Paises apenas em flags
so_flags = pd.merge(flags, countries, 
                    how="left", 
                    left_on="name", right_on="country")

so_flags = so_flags[pd.isnull(so_flags['country']) == True]
num_linhas_so_flags = so_flags.shape[0]

#2.3 - Right Join: Paises apenas em countries
so_countries = pd.merge(flags, countries,
                       how="right", 
                       left_on="name", right_on="country")

so_countries = so_countries[pd.isnull(so_countries['name']) == True]
num_linhas_so_countries = so_countries.shape[0]

#---------------------------------------------------------------
#(3)-Imprime os resultados
#---------------------------------------------------------------
print('- Num países em "flags": ', num_linhas_flags)
print('- Num países em "contries": ', num_linhas_countries)
print('- Num países em ambas: ', num_linhas_ambas)
print('- Num países só em flags: ', num_linhas_so_flags)
print('- Num países só em "countries": ', num_linhas_so_countries)

print('------------------------------------------------------------')
print("Países só em flags: ")
print(so_flags['name'])
print('------------------------------------------------------------')
print("Países só em countries: ")
print(so_countries['country'])