#P44: Junção Interna
import pandas as pd 

#(1)-Cria os DataFrames depto e emp
dic_depto = {"id":["D1", "D2", "D3", "D4"], 
             "nomeDepto": ["Compras", "RH", "TI", "Vendas"], 
             "local":["SP","RJ","RJ","SP"]}

dic_emp = {"num":[3199, 3269, 3555, 3788, 3844], 
           "nome": ["Ana", "David", "José", "Marina", "Luis"], 
           "salario": [1600, 2975, 1500, 5000, 3000], 
           "idDepto": ["D2", "D3", None, "D2", "D4"]}

depto = pd.DataFrame(dic_depto)
emp = pd.DataFrame(dic_emp)

#(2)-Efetua a operação de junção

# Combina uma linha de um DataFrame R com uma linha de um DataFrame S
juncao_interna = pd.merge(emp, depto, left_on="idDepto", right_on="id")

# Retorna todas as linhas do DataFrame especificado à Esquerda
j_esq = pd.merge(emp, depto, how="left", left_on="idDepto", right_on="id")

# Retorna todas as linhas do DataFrame especificado à Direita
j_dir = pd.merge(emp, depto, how="right", left_on="idDepto", right_on="id")

# Retorna todos os valores dos DataFrames 
j_full = pd.merge(emp, depto, how="outer", left_on="idDepto", right_on="id")

print('------------------------------')
print("depto:")
print(depto)
print('------------------------------')
print("emp:")
print(emp)
print('------------------------------')
print("junção interna:")
print(juncao_interna)
print('------------------------------')
print("junção esquerda:")
print(j_esq)
print('------------------------------')
print("junção direita:")
print(j_dir)
print('------------------------------')
print("junção full:")
print(j_full)