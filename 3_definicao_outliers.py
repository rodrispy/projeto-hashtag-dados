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