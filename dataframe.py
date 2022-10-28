## Importando as bibliotecas e bases de dados
from IPython.display import display
import pandas as pd
import pathlib
import numpy as np

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
# 1. IDs, links e informações não relevantes para o modelo;
# 2. Colunas repetidas ou extremamente parecidas (data, ano, mês);
# 3. Colunas preenchidas com texto livre (não rodaremos nenhuma análise de palavras ou algo do tipo);
# 4. Colunas em que todos ou quase todos os valores são iguais (podemos analisar a coluna em específico na tabela toda fazendo um value.counts())

# Criando um arquivo em excel com os 1000 primeiros registros para fazer uma análise qualitativa
#base_airbnb.head(1000).to_csv('primeiros_registros.csv')

# Criando também um arquivo em excel do DataFrame completo para fins de análises comparativas, com todas as informações presentes
#base_airbnb.to_csv('base_airbnb_completo.csv', sep=",")

# Após filtrar as colunas na planilha de primeiros_registros, vamos criar uma lista com essas colunas para filtrar o df completo
colunas = ['host_response_time','host_response_rate','host_is_superhost','host_listings_count','latitude','longitude','property_type','room_type','accommodates','bathrooms','bedrooms','beds','bed_type','amenities','price','security_deposit','cleaning_fee','guests_included','extra_people','minimum_nights','maximum_nights','number_of_reviews','review_scores_rating','review_scores_accuracy','review_scores_cleanliness','review_scores_checkin','review_scores_communication','review_scores_location','review_scores_value','instant_bookable','is_business_travel_ready','cancellation_policy','ano','mes']

base_airbnb = base_airbnb.loc[:, colunas]
display(base_airbnb)


# Visualizando os dados, percebemosd que existe uma grande disparidade em dados faltantes. As colunas com mais de 300.000 valores NaN foram excluídas da análise.
# Para as outras colunas, como temos muitos dados (mais de 900.000 linhas) vamos excluir as linhas que contém dados NaN

# Verificando quantos valores são nulos
#print(base_airbnb.isnull().sum())

# Excluindo as colunas que tem muitos valores nulos
for coluna in base_airbnb:
    if base_airbnb[coluna].isnull().sum() > 300000:
        base_airbnb = base_airbnb.drop(coluna, axis=1)
        
# As linhas que sobraram com valores vazios são tão poucas que também podemos excluir
base_airbnb = base_airbnb.dropna()
# Verificando se agora não temos mais valores vazios
print(base_airbnb.isnull().sum())


# Agora vamos verificar os tipos de dados de cada coluna (essencial para saber se os números realmente são tipos numéricos que Python conseguirá utilizar de modo correto)
print(base_airbnb.dtypes) #printando todos os tipos de cada coluna para comparação
print('-'*60)
print(base_airbnb.iloc[0]) #analisando somente a primeira linha de cada coluna para sabermos como estão os valores e compará-los aos tipos printados anteriormente
#Podemos inferir que a coluna "price" e "extra_people" estão com o tipo "object" ao invés de "float"
#Na planilha, temos o $ e a , como caracteres que está interferindo no tipo de variável

# Modificando os tipos de variáveis nas colunas apontadas
base_airbnb['price'] = base_airbnb['price'].str.replace('$', '')
base_airbnb['price'] = base_airbnb['price'].str.replace(',', '')
base_airbnb['price'] = base_airbnb['price'].astype(np.float32, copy=False) #propriedade da biblioteca numpy (imported as np)

base_airbnb['extra_people'] = base_airbnb['extra_people'].str.replace('$', '')
base_airbnb['extra_people'] = base_airbnb['extra_people'].str.replace(',', '')
base_airbnb['extra_people'] = base_airbnb['extra_people'].astype(np.float32, copy=False) #propriedade da biblioteca numpy (imported as np)

print(base_airbnb.dtypes)