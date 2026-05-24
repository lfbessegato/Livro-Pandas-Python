#P28: Métodos unique() e value_counts()
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

#2-Retorna o domínio dps atributos categóricos
print("Domínio dos atributos categóricos:")
print("------------------------------------")
print("Sexo:", vendas["Sexo"].unique())
print("Bairro:", vendas["Bairro"].unique())
print("Cartão:", vendas["Cartão"].unique())

#3-Retorna as frequências dos valores de cada coluna
print("\n")
print("Tabelas de frequência: ")
print("\n1-sexo:")
print(vendas["Sexo"].value_counts())
print("\n2-Bairro:")
print(vendas["Bairro"].value_counts())
print("\n3-Cartão:")
print(vendas["Cartão"].value_counts())
