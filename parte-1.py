## Importando as bibliotecas e bases de dados
from IPython.display import display
import pandas as pd
import pathlib

# Criando um dicionário com os meses do ano, para seleção durante a iteração dos documentos da pasta dataset
meses = {'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4, 'mai': 5, 'jun': 6, 'jul': 7, 'ago': 8, 'set': 9, 'out': 10, 'nov': 11, 'dez': 12}

# Definindo o caminho com o pathlib para iterar os arquivos da pasta dataset
caminho_bases = pathlib.Path('dataset')
# Criando um dataframe principal para adicionar os dataframes futuros
base_airbnb = pd.DataFrame()
# Criando um for para percorrer a lista de arquivos e adicionar cada arquivo no dataframe principal
for arquivo in caminho_bases.iterdir():
    mes = meses[arquivo.name[:3]]
    
    ano = arquivo.name[-8:]
    ano = int(ano.replace('.csv', ''))
    
    df = pd.read_csv(caminho_bases / arquivo.name)
    df['ano'] = ano
    df['mes'] = mes
    base_airbnb = base_airbnb.append(df)

# Como temos muitas colunas, nosso modelo pode acabar ficando muito lento
# Além disso, uma análise rápida permite ver que várias colunas não são necessárias para o nosso modelo de previsão, portanto vamos excluir algumas
# Tipos de colunas que serão excluídas:
#

# Criando um arquivo em excel com os 1000 primeiros registros para fazer uma análise qualitativa
base_airbnb.head(1000).to_csv('primeiros_registros.csv', sep=';')