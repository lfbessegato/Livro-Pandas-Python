#P58: Transformação da base de flags
import pandas as pd 

#--------------------------------------------------------
#(1)-Importa a base de dados
#--------------------------------------------------------
flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags.csv')

#--------------------------------------------------------
#(2)-Conversão dos atributos do Grupo 2
# De: Categórico não binários
# Para: Categóricos binários
#--------------------------------------------------------
for c in flags.columns:
    if c in ['landmass', 'zone', 
             'language', 'religion', 'mainhue', 
             'topleft', 'botright']: 
        dummies = pd.get_dummies(flags[c], prefix=c)
        flags = flags.join(dummies)

#--------------------------------------------------------
#(3)-Normalização dos atributos dos Grupos 3 e 4
# De: Numéricos contínuos e discretos
# Para: Numéricos com valores na faixa entre 0 e 1
#--------------------------------------------------------
for c in flags.columns:
    if c in ['area', 'population',
             'bars', 'strips', 'colours',
             'circles', 'crosses', 'saltires', 
             'quartes', 'sunstars']: 
        
        c_max = max(flags[c])
        c_min = min(flags[c])
        flags[c] = (flags[c] - c_min) / (c_max -c_min)

#--------------------------------------------------------
#(4)-Exclusão dos atributos indesejados
#--------------------------------------------------------
flags = flags.drop(columns=['name', 'landmass', 
                            'zone', 'language', 
                            'religion', 'mainhue', 
                            'topleft', 'botright', 
                            ])

#--------------------------------------------------------
#(5)-Imprime a configuração final das flags
#--------------------------------------------------------
# Imprime as primeiras linhas
print('head(): '); print(flags.head())
print('--------------------------------------------------------')

# Imprime as últimas linhas
print('tail(): '); print(flags.tail())
print('--------------------------------------------------------')

#--------------------------------------------------------
#(6)-Salva o dataset alterado para um arquivo
#--------------------------------------------------------
flags.to_csv("/home/luciano/Documentos/Livro-Pandas-Python/Cap06-Transformacao-Limpeza-Dataframes/Exemplos/flags_transf.csv", sep=" ", index=False)
