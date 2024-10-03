"""
BACHARELADO EM CIENCIAS DA COMPUTACAO - UFMT 2024
PROFESSOR : IVAIRTON M. SANTOS 
ALUNO 1: JOÃO PAULO ALVES CAMPOS 
ALUNO 2: ENDLEY MORAES
 
TRABALHO DE AMOSTRAGEM E MANIPULAÇAO DE BASE DE DADOS COM PYTHON
(FETCHING_CALIFORNIA_HOUSING)     
    
"""
# Biblioteca NumPY
import numpy as np  
# Biblioteca Pandas
import pandas as pd 
# Biblioteca Seaborn
import seaborn as sns 
# Biblioteca Matplotlib(requisitos 2)
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


#------------------------Requisitos 1------------------------
#import base de dados
def fetch_california_housing():
    from sklearn.datasets import fetch_california_housing
    imoveis = fetch_california_housing()

    x = imoveis.data
    y = imoveis.target
    #nomes das colunas
    #MeddInc = renda Media familiar por regiao
    #HouseAge = Idade media da casa na regiao
    #AveRooms = numero medio de comodos por casa na regiao
    #Avebedroms = numero medio de quartos por casa na regiao
    #population = populacao na regiao
    #AveOccup = numero medio de moradores por casa na regiao
    #latitude = latitude na regiao
    #longitude = longitude na regiao
    #MedhouseVal = valor do imóvel expresso em múltiplos de US$ 100.000
    imoveisC_colunas = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

    base = pd.DataFrame(x, columns = imoveisC_colunas)
    describe = base.describe()
    print(describe)
    return base


#------------------------Requisitos 2------------------------
# Amostragem gráficos latitude e longitude
def plotar_graficos(base):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=base, x='Longitude', y='Latitude', alpha=0.5)
    plt.title('Gráficos Latitude e Longitude')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.show()
    

#------------------------Requisitos 3------------------------
#calculo das métricas
def calculo_metricas(base):
    colunas = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
    metricas = {}
    for coluna in colunas:
        metricas[coluna]= {
            'media': base[coluna].mean(),
            'mediana': base[coluna].median(),
            'moda': base[coluna].mode()[0],
            'variancia': base[coluna].var(),
            'desvio_padrao': base[coluna].std(),
            'quantis': base[coluna].quantile([0.25, 0.5, 0.75]),
            'IQR': base[coluna].quantile(0.75) - base[coluna].quantile(0.25)
        }
        metricasDT = pd.DataFrame(metricas).T
        print(metricasDT.round(2))
#chamar funçoes
base = fetch_california_housing()
plotar_graficos(base)
calculo_metricas(base)





