#P20: Salva o conteúdo do DataFrame em um arquivo CSV
import pandas as pd

# Cria o DataFrame
dados = {'codigo': [1001, 1002, 1003, 1004, 1005],
         'nome': ['Leite', 'Café', 'Biscoito', 'Chá', 'Torradas']
}
produtos = pd.DataFrame(dados)

# Salva seu conteúdo para um arquivo 
produtos.to_csv('/home/luciano/Documentos/Livro-Pandas-Python/Cap03-Estrutura-Dados-Dataframe/Exemplos/produtos.csv', 
                sep="\t", index=False)

# Exportar no formato Excel
produtos.to_excel('/home/luciano/Documentos/Livro-Pandas-Python/Cap03-Estrutura-Dados-Dataframe/Exemplos/produtos.xlsx',
                 index=False)