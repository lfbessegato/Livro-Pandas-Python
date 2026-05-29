#P59: Programa Final
# Cria um classificador K-NN
# Avalia este classificador com o método LOO

#---------------------------------------------------------
# Parte 1: Importação das Bibliotecas
#---------------------------------------------------------
import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier

#---------------------------------------------------------
# Parte 2: Carrega a base de dados de treinamento
#---------------------------------------------------------
flags = pd.read_csv('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/flags_transf.csv')

#---------------------------------------------------------
# Parte 3: Configura os parâmetros e variáveis auxiliares
#---------------------------------------------------------
# Valor de k a ser usado no k-nn
k=3

# Nomes dos labels (rótulos de classe)
labels = ['red', 
          'green', 
          'blue', 
          'gold', 
          'white', 
          'black', 
          'orange']

# Número de labels (=7)
q = len(labels)

# Número de registros da base de treinamento (194)
N = flags.shape[0]

#---------------------------------------------------------
# Parte 4: Cria um classificador com o algoritmo k-NN
# e faz a estimativa do desempenho preditivo com o
# método LOO (Leave-One-Out)
#---------------------------------------------------------

#---------------------------------------------------------
# 4.1 - for j: laço que percorre cada rótulo
#---------------------------------------------------------
for j in range(0,q):
    print('-------------------------------------------')
    print("PROCESSANDO O RÓTULO ", labels[j])

    #---------------------------------------------------------
    # 4.1.1 - Instancia uma matriz de confusão para o rótulo
    #---------------------------------------------------------
    mc = pd.DataFrame({'predito_nao': [0,0], 
                       'predito_sim': [0,0]},
                       index = ['real_nao', 'real_sim'])
    
    #---------------------------------------------------------
    # 4.1.2 - Divide a base de treinamento verticalmente 
    # em duas partes: X (atributos preditivos) e 
    #                 Y (atributo class)
    #---------------------------------------------------------
    X = flags.drop(columns=labels)
    Y = flags[labels[j]]

    #---------------------------------------------------------
    # 4,2 - for i: laço que realiza o LOO para o rótulo j
    #---------------------------------------------------------
    for i in range(0,N):

        #---------------------------------------------------------
        # 4.2.1 - Separa os dados que serão utilizados para 
        # treinar o modelo
        #---------------------------------------------------------
        X_treino = X.drop([i])
        Y_treino = Y.drop([i])

        #---------------------------------------------------------
        # 4.2.2 - Separa o objeto de teste
        #---------------------------------------------------------
        X_teste = X.iloc[[i],:]
        Y_teste = Y.iloc[i]

        #---------------------------------------------------------
        # 4.2.3 - Treinamento do modelo k-NN 
        # com os dados de treino
        #---------------------------------------------------------
        modelo=KNeighborsClassifier(n_neighbors=k)
        modelo.fit(X_treino,Y_treino)

        #---------------------------------------------------------
        # 4.2.4 - Teste do modelo k-NN com o objeto de teste
        #---------------------------------------------------------
        pred = modelo.predict(X_teste)

        #---------------------------------------------------------
        # 4.2.5 - Atualiza a célula adequada da matriz de confusão
        # em função do resultado do teste
        #---------------------------------------------------------
        if (Y_teste == 0):
            if (pred == 0): mc.iloc[0,0] += 1
            if (pred == 1): mc.iloc[0,1] += 1
        else:
            if (pred == 0): mc.iloc[1,0] += 1
            if (pred == 1): mc.iloc[1,1] += 1

    #---------------------------------------------------------
    # 4.3 - Fim do LOO para o rótulo j 
    # imprime a sua matriz de confusão e acurácia
    #---------------------------------------------------------
    print(mc)
    acuracia = (mc.iloc[0,0] + mc.iloc[1,1]) / N
    print('acurácia = ', round(acuracia,2))
