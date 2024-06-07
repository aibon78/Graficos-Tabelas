
import os
import pandas as pd
from IPython.display import display
lista_de_arquivos = os.listdir("C:\\Users\\Andre\\Desktop\\Vendas")
display(lista_de_arquivos)


tabela_total = pd.DataFrame()
for arquivo in lista_de_arquivos:
    if "Vendas" in arquivo:
        print(f"C:\\Users\\Andre\\Desktop\\Vendas\\{arquivo}")
        tabela = pd.read_csv(f"C:\\Users\\Andre\\Desktop\\Vendas\\{arquivo}")
        tabela_total = tabela_total.append(tabela)
display(tabela_total)
.
# Tratar / Compilar base de dados
# Passo 4 - Calcular o produto mais vendido (em quantidade)
# Passo 5 - Calcular o produto que mais faturo (em faturamento)
# Calcular a cidade/loja que mais vendeu (em faturamento) - criar um grafico/dashboard


