from IPython.display import display
import pandas as pd
import pathlib

df = pd.read_csv('base_airbnb_completo.csv')
df2 = pd.read_csv('primeiros_registros.csv')


# Analisando se algumas colunas são iguais, como por exemplo:
print((df['host_listings_count']==df['host_total_listings_count']).value_counts())