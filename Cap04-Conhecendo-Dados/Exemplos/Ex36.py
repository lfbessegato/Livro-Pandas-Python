#P36: Estudando a base de dados Flags
# I. Propriedades básicas de cada atributo
import pandas as pd

#----------------------------------------------------------------------
#(1)-Importa a base de dados 
#----------------------------------------------------------------------
flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags.csv')

#----------------------------------------------------------------------
#(2)-Obtém as propriedades básicas de cada atributo
#----------------------------------------------------------------------
i=0
for c in flags.columns: 
    i += 1
    att = flags[c] # Atributo
    att_dtype = att.dtype # dtype
    att_tam_dominio = att.unique().size # Tamanho do domínio

    att_tem_nulo = any(att.isnull()) # Tem valor nulo?
    if (att_tam_dominio < 8):
        print("("+str(i) + ") atributo: ", c, "\t", 
              "dtype: ", att_dtype, "\t", 
              "nulos: ", att_tem_nulo, "\n",
              "dominio (primeiros elementos): ", att.unique())
    else:
        if (att_dtype=='object'):
            print("("+str(i) + ") atributo: ", c, "\t", 
                "dtype: ", att_dtype, "\t", 
                "nulos: ", att_tem_nulo, "\n",
                "dominio (primeiros elementos): ", att.unique()[:8])
        else:
            print("("+str(i) + ") atributo: ", c, "\t", 
              "dtype: ", att_dtype, "\t", 
              "nulos: ", att_tem_nulo, "\n",
              "min: ", att.min(), "\t",
              "max: ", att.max(), "\t",
              "média: ", round(att.mean(),2), "\t",
              "desvio padrão: ", round(att.std(),2))
