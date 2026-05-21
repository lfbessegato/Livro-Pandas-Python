#P07: Operações Aritméticas
 
import pandas as pd 
import numpy as np 

# Cria as Séries S1 e S2
s1 = pd.Series([2, 4, 6])
s2 = pd.Series([1, 3, 5])
print('S1:'); print(s1)
print('S2:'); print(s2)

# Efetua as operações artiméticas
print('--------------------------------')
print('S1 * 2')
print(s1 * 2)
print('--------------------------------')
print('S1 + S2')
print(s1 + s2)
print('--------------------------------')
print('Raiz Quadrada dos elementos de S1')
print(np.sqrt(s1)) # Com a Numpy
