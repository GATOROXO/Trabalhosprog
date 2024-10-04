```markdown
# Trabalho de Amostragem e Manipulação de Dados com Python

## BACHARELADO EM CIÊNCIAS DA COMPUTAÇÃO - UFMT 2024
**Professor:** Ivairton M. Santos  
**Aluno 1:** João Paulo Alves Campos  
**Aluno 2:** Endley Moraes  

## Descrição do Projeto
Este projeto consiste em uma análise exploratória da base de dados de imóveis da Califórnia, utilizando Python e bibliotecas como Pandas, NumPy, Seaborn e Matplotlib. O objetivo é importar a base de dados, calcular métricas estatísticas, visualizar informações e identificar correlações significativas entre variáveis.

## Estrutura do Código

### 1. Importação de Bibliotecas
O código começa importando as bibliotecas necessárias:
```python
import numpy as np  
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
```

### 2. Requisitos 1: Importar Base de Dados
A função `fetch_california_housing()` é responsável por importar a base de dados dos imóveis e realizar uma descrição inicial:
```python
def fetch_california_housing():
    from sklearn.datasets import fetch_california_housing
    imoveis = fetch_california_housing()

    x = imoveis.data
    y = imoveis.target
    imoveisC_colunas = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
    base = pd.DataFrame(x, columns=imoveisC_colunas)
    base['ValorImovel'] = y  # Adicionando o valor do imóvel ao DataFrame

    describe = base.describe()
    print(describe)
    return base
```

### 3. Requisitos 2: Amostragem de Gráficos
A função `plotar_graficos(base)` gera gráficos de dispersão para visualizar a relação entre longitude e latitude:
```python
def plotar_graficos(base):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=base, x='Longitude', y='Latitude', alpha=0.5)
    plt.title('Gráficos Latitude e Longitude')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.show()
```

### 4. Requisitos 3: Cálculo das Métricas
A função `calculo_metricas(base)` calcula várias métricas estatísticas:
```python
def calculo_metricas(base):
    colunas = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude', 'ValorImovel']
    metricas = {}
    
    for coluna in colunas:
        quantis = base[coluna].quantile([0.25, 0.5, 0.75]).round(2).to_dict()
        metricas[coluna] = {
            'media': round(base[coluna].mean(), 2),
            'mediana': round(base[coluna].median(), 2),
            'moda': base[coluna].mode()[0],
            'variancia': round(base[coluna].var(), 2),
            'desvio_padrao': round(base[coluna].std(), 2),
            'quantis': quantis,
            'IQR': round(base[coluna].quantile(0.75) - base[coluna].quantile(0.25), 2)
        }
    
    metricasDT = pd.DataFrame(metricas).T  
    print(metricasDT)  
    return metricasDT  
```

### 5. Requisitos 4: Boxplot e Histogramas
A função `req4(base)` gera boxplots e histogramas para visualizar a distribuição das variáveis:
```python
def req4(base):
    plt.figure(figsize=(12, 10))
    sns.boxplot(data=base)
    plt.title('Boxplot das Métricas')
    plt.xticks(rotation=45)
    plt.show()
    
    base.hist(bins=30, figsize=(12, 10), layout=(3, 3), edgecolor='black')
    plt.suptitle('Histograma das Métricas')
    plt.tight_layout()
    plt.show()
```

### 6. Requisitos 5: Identificar Correlações
A função `identificar_correlações(base)` calcula e exibe a matriz de correlação:
```python
def identificar_correlações(base):
    corr_matrix = base.corr()
    print("Matriz de Correlação:")
    print(corr_matrix)

    correlacao_valor = corr_matrix['ValorImovel'].drop('ValorImovel')
    correlacao_significativa = correlacao_valor[abs(correlacao_valor) > 0.5]
    print("\nCorrelações significativas com o Valor do Imóvel:")
    print(correlacao_significativa)
```

## Execução do Código
As funções são chamadas na seguinte ordem para executar a análise:
```python
base = fetch_california_housing()
plotar_graficos(base)
metricas = calculo_metricas(base)
req4(base)  
identificar_correlações(base)  
```

## Conclusão
Este projeto proporciona uma análise abrangente da base de dados de imóveis da Califórnia, incluindo importação de dados, visualização, cálculo de métricas e identificação de correlações.

