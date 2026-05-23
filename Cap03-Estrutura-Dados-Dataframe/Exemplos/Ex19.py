#P19: Importação de arquivo JSON
import pandas as pd
import json

#(1)-Importar o arquivo JSON para memória
with open('/home/luciano/Documentos/Livro-Pandas-Python/repositorio/notas.json') as f:
    j_notas = json.load(f)

#(2)-Transfere as informações para um DataFrame
notas = pd.DataFrame(j_notas, 
                     columns=['matricula', 'notas'])

print(notas)