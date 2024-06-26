
import os
import pandas as pd
from IPython.display import display


diretorio = "C:\\Users\\Andre\\Desktop\\Vendas"


lista_de_arquivos = os.listdir(diretorio)


frames = []


for arquivo in lista_de_arquivos:
   
    if "Vendas" in arquivo and arquivo.endswith(".csv"):
        
        caminho_arquivo = os.path.join(diretorio, arquivo)
        
        tabela = pd.read_csv(caminho_arquivo)
        frames.append(tabela)


tabela_total = pd.concat(frames, ignore_index=True)


display(tabela_total)


tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']


tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
display(tabela_faturamento)



