"""
BACHARELADO EM CIENCIAS DA COMPUTACAO - UFMT 2024
PROFESSOR : IVAIRTON M. SANTOS 
ALUNO 1: JOÃO PAULO ALVES CAMPOS 
ALUNO 2: ENDLEY MORAES
TRABALHO DE AMOSTRAGEM E MANIPULAÇAO DE BASE DE DADOS COM PYTHON
(FETCHING_CALIFORNIA_HOUSING) 
Trabalho feito seguindo o tutorial passado no arquivo do trabalho.
 
"""   

# Importação de bibliotecas
import numpy as np  
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

#------------------------Requisitos 1------------------------
# Importar base de dados
def fetch_california_housing():
    from sklearn.datasets import fetch_california_housing
    imoveis = fetch_california_housing()

    x = imoveis.data
    y = imoveis.target
    # Nomes das colunas
    imoveisC_colunas = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
    base = pd.DataFrame(x, columns=imoveisC_colunas)
    base['ValorImovel'] = y  # Adicionando o valor do imóvel ao DataFrame

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
# Cálculo das métricas
def calculo_metricas(base):
    colunas = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude', 'ValorImovel'] #necessario o uso de malditas matrizes :(
    metricas = {}#matriz vazia
    
    for coluna in colunas:
        quantis = base[coluna].quantile([0.25, 0.5, 0.75]).round(2).to_dict()
        metricas[coluna] = {  # criar dicionário e arrendonda os resultados no terminal 
            'media': round(base[coluna].mean(), 2),
            'mediana': round(base[coluna].median(), 2),
            'moda': base[coluna].mode()[0],
            'variancia': round(base[coluna].var(), 2),
            'desvio_padrao': round(base[coluna].std(), 2),
            'quantis': quantis,
            'IQR': round(base[coluna].quantile(0.75) - base[coluna].quantile(0.25), 2)
        }
    
    # Transformar dicionário em DataFrame e transpor
    metricasDT = pd.DataFrame(metricas).T  
    print(metricasDT)  
    return metricasDT  

#------------------------Requisitos 4------------------------
# gerar boxplot e histogramas
def req4(base):
    #boxplot
    plt.figure(figsize=(12, 10))  # Ajustar o tamanho da figura
    sns.boxplot(data=base)
    plt.title('Boxplot das Métricas')
    plt.xticks(rotation=45)  # Rotacionar os nomes dos eixos
    plt.show()  # Mostrar o gráfico
    
    # Histograma
    base.hist(bins=30, figsize=(12, 10), layout=(3, 3), edgecolor='black')
    plt.suptitle('Histograma das Métricas')
    
    plt.tight_layout()  # Ajustar layout
    plt.show()  # Mostrar os gráficos

#------------------------Requisitos 5-------------------------  *(chatGPT)*

#Identificar correlações
def identificar_correlações(base):
    # Calcular a matriz de correlação
    corr_matrix = base.corr()

    # Exibir a matriz de correlação
    print("Matriz de Correlação:")
    print(corr_matrix)

    # Identificar pares de variáveis com correlação significativa com o valor do imóvel
    correlacao_valor = corr_matrix['ValorImovel'].drop('ValorImovel')  # Exclui a correlação com ele mesmo
    correlacao_significativa = correlacao_valor[abs(correlacao_valor) > 0.5]  # Filtrar correlações altas

    print("\nCorrelações significativas com o Valor do Imovel:")
    print(correlacao_significativa)
    

# Chamar funções
base = fetch_california_housing()
plotar_graficos(base)
metricas = calculo_metricas(base)
req4(base)  
identificar_correlações(base)  


#Errei fui moleque professor, pelo menos tentei no requesito 5.
