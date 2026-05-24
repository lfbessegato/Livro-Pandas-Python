#P29: Agragação com o método 'group_by()'
import pandas as pd

#1-Cria o DataFrame
dados = {"Sexo": ["F", "M", "F", "F", "F", "M"],
         "Bairro": ["BelVerde", 
                    "BelVerde", 
                    "Savassi", 
                    "Anchieta", 
                    None, 
                    "Savassi"], 
        "Valor": [150.00, 
                  35.00,
                  80.00,
                  250.00,
                  9.00,
                  25.00], 
        "Cartão": ["Master",
                   "Visa",
                   "Visa",
                   "Amex",
                   "Elo", 
                   "Master"]
}

id_clientes = [1, 2, 3, 4, 5, 6]

vendas = pd.DataFrame(dados, index=id_clientes)

#2-Gera uma variável "grouped"
# onde a chave é bairro e a medida "valor"
grupo_valor_bairro = vendas['Valor'].groupby(vendas['Bairro'])

#3-Computa agregados a partir da variável gerada
print('- Quantidade de clientes, por bairro:\n ', grupo_valor_bairro.count())
print('-----------------------------------------')
print('- Valor total das vendas, por bairro:\n ', grupo_valor_bairro.sum())
print('-----------------------------------------')
print('- Valor médio das vendas, por bairro:\n ', grupo_valor_bairro.mean())
