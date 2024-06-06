
import os
import pandas as pd
from IPython.display import display
lista_de_arquivos = os.listdir("C:\\Users\\Andre\\Desktop\\Vendas")
display(lista_de_arquivos)

# Passo 2 - Importar base de dados de vendas
tabela_total = pd.DataFrame()
for arquivo in lista_de_arquivos:
    if "Vendas" in arquivo:
        print(f"C:\\Users\\Andre\\Desktop\\Vendas\\{arquivo}")
        tabela = pd.read_csv(f"C:\\Users\\Andre\\Desktop\\Vendas\\{arquivo}")
        tabela_total = tabela_total.append(tabela)
display(tabela_total)

# Passo 3 - Tratar / Compilar base de dados
# Passo 4 - Calcular o produto mais vendido (em quantidade)
# Passo 5 - Calcular o produto que mais faturo (em faturamento)
# Passo 6 - Calcular a cidade/loja que mais vendeu (em faturamento) - criar um grafico/dashboard


