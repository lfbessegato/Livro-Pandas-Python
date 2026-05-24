#P26: Estatísticas sobre Colunas e Linhas de um DataFrame
import pandas as pd

# Cria um DataFrame com as notas de 4 alunos em 3 provas
notas = pd.DataFrame({
    "A1": [9.8, 7.2, 8.0], 
    "A2": [5.3, 4.0, 3.5], 
    "A3": [5.5, 8.1, 7.2],
    "A4": [7.0, 7.5, 6.5]},
    index = ["P1", "P2", "P3"]
)

# Imprime o DataFrame
print("\nNome finais")
print('------------------')
print(notas)

# Computa e imprime as estatíticas por aluno e prova
print("\nMédia por aluno")
print('------------------')
print(notas.mean())

print("\nMaior nota de cada Aluno: ")
print('------------------------------')
print(notas.max())

print("\nMédia por prova")
print('------------------')
print(notas.mean(axis=1))

print("\nMaior nota de cada prova: ")
print('-------------------------')
print(notas.max(axis=1))

