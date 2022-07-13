## Importando as bibliotecas e bases de dados
from IPython.display import display
import pandas as pd
import pathlib

# Definindo o caminho com o pathlib para iterar os arquivos da pasta dataset
caminho_bases = pathlib.Path('dataset')
# Criando um dataframe principal para adicionar os dataframes futuros
base_airbnb = pd.DataFrame()
# Criando um for para percorrer a lista de arquivos e adicionar cada arquivo no dataframe principal
for arquivo in caminho_bases.iterdir():
    df = pd.read_csv(caminho_bases / arquivo.name)
    base_airbnb = base_airbnb.append(df)

display(base_airbnb)