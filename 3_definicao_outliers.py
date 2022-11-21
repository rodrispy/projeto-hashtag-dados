# Análise Exploratória e tratamento de outliers

# Analisando feature por feature e decidindo se manteremos todas
# Definindo os outliers -> fatores que estão abaixo do limite inferior e acima do limite superior
# Estatisticamente, a fórmula para se defirnir os outliers são:
# Q1 - 1.5 * Amplitude
# Q3 + 1.5 * Amplitude

from IPython.display import display
import pandas as pd
import pathlib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

base_airbnb = pd.read_csv("BaseTratada.csv")

#plt.figure(figsize=(15, 10))
#sns.heatmap(base_airbnb.corr(), annot=True, cmap='Greens')

# Definição de funções para análise de outliers
def limites(coluna):
    q1 = coluna.quantile(0.25)
    q3 = coluna.quantile(0.75)
    amplitude = q3 - q1
    return q1 - 1.5 * amplitude, q3 + 1.5 * amplitude

print(limites(base_airbnb['price']))

# Plotando um gráfico
def diagrama_caixa(coluna):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(15,5)
    sns.boxplot(x=coluna, ax=ax1)
    ax2.set_xlim(limites(coluna))
    sns.boxplot(x=coluna, ax=ax2)
        
# Criando gráfico de histograma
def histograma(coluna):
    plt.figure(figsize=(15,5))
    sns.distplot(coluna, hist=True)
    
# Como estamos construindo um modelo para imóveis comuns, acredito que os valores acima do limite superior serão apenas de apartamentos de altíssimo luxo, que não é o nosso objetivo principal. Por isso, podemos excluir esses outliers.

# Função para excluir os outliers da base de dados
def excluir_outliers(df, nome_coluna):
    qtde_linhas = df.shape[0]
    lim_inf, lim_sup = limites(df[nome_coluna])
    
    df = df.loc[(df[nome_coluna] >= lim_inf) & (df[nome_coluna] <= lim_sup), :]
    linhas_removidas = qtde_linhas - df.shape[0]
    
    return df, linhas_removidas

# Definindo uma função para gráficos de barra
def grafico_barra(coluna):
    plt.figure(figsize=(15,5))
    ax = sns.barplot(x=coluna.value_counts().index, y=coluna.value_counts())
    ax.set_xlim(limites(coluna))


# Aplicando a função na coluna de "price"
base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'price')
print(f'{linhas_removidas} linhas removidas')

diagrama_caixa(base_airbnb['price'])
histograma(base_airbnb['price'])

# Aplicando a função na coluna de "extra_people"
base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'extra_people')
print(f'{linhas_removidas} linhas removidas')

diagrama_caixa(base_airbnb['extra_people'])
histograma(base_airbnb['extra_people'])


# Analisando as próximas colunas com a função do gráfico de barras e excluindo ou não os outliers
grafico_barra(base_airbnb['host_listings_count'])

base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'host_listings_count')
base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'accommodates')
base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'bathrooms')
base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'beds')
base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'bedrooms')
base_airbnb, linhas_removidas = excluir_outliers(base_airbnb, 'minimum_nights')


# Removendo "guests_included" e "maximum_nights" da análise
base_airbnb = base_airbnb.drop('guests_included', axis=1)
base_airbnb = base_airbnb.drop('maximum_nights', axis=1)
base_airbnb = base_airbnb.drop('number_of_reviews', axis=1)



