import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lista com os nomes dos arquivos CSV
arquivos_csv = ['../postProcessing/sampleU/1000/linhaA.csv', 
                '../postProcessing/sampleU/1000/linhaB.csv', 
                '../postProcessing/sampleU/1000/linhaC.csv', 
                '../postProcessing/sampleU/1000/linhaD.csv']
etiquetas = ['x = 0.25 m', 'x = 0.5 m', 'x = 1.0 m', 'x = 1.5 m']  # Etiquetas para a legenda

# Coeficientes da parábola: y = ax^2 + bx + c
a, b, c = -1.5, 0, 1.5

# Definindo a cor para todas as curvas
cor_curva = 'b'  # Azul

# Configurações do intervalo dos eixos
x_lim = (0, 1.5)
y_lim = (0, 1)

# Iterar sobre os arquivos e gerar gráficos individuais
for i, (arquivo, etiqueta) in enumerate(zip(arquivos_csv, etiquetas)):
    # Ler o arquivo CSV
    df = pd.read_csv(arquivo)
    
    # Extraia os dados das colunas 1 e 2
    x = df.iloc[:, 0]  # Primeira coluna
    y = df.iloc[:, 1]  # Segunda coluna
    
    # Configurações do gráfico para cada curva
    plt.figure(figsize=(10, 6))
    plt.plot(y, x, linestyle='-', color=cor_curva, label=etiqueta)

    # Adicionando títulos e rótulos
    plt.xlabel('$U_x$ (m/s)')
    plt.ylabel('y (m)')
    plt.xlim(x_lim)
    plt.ylim(y_lim)
    plt.grid(True, linestyle='--', linewidth=0.5)

    # Remover molduras e eixos
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    
    plt.gca().xaxis.set_visible(False)
    plt.gca().yaxis.set_visible(False)

    # Adicionar a solução analítica apenas no último gráfico
    if i == len(arquivos_csv) - 1:
        x_parabola = np.linspace(x_lim[0], x_lim[1], 500)
        y_parabola = a * x_parabola**2 + b * x_parabola + c
        plt.plot(y_parabola, x_parabola, color='k', linestyle='-', label='Solução Analítica')
    
    # Adicionando a legenda na parte superior externa ao gráfico
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), frameon=False)

    # Salvando o gráfico como um arquivo PNG
    plt.savefig(f'Perfil_Ux_{etiqueta.replace(" ", "_")}.png', transparent=True, bbox_inches='tight')

    # Fechar a plotagem para liberar memória
    plt.close()

    print(f'Gráfico salvo como Perfil_Ux_{etiqueta.replace(" ", "_")}.png.')

