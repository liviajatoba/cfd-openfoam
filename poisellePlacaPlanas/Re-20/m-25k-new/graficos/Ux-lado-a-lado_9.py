import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Lista com os nomes dos arquivos CSV
arquivos_csv = ['../postProcessing/sampleU/1000/linhaA.csv', '../postProcessing/sampleU/1000/linhaB.csv', '../postProcessing/sampleU/1000/linhaC.csv', '../postProcessing/sampleU/1000/linhaD.csv']
etiquetas = ['x = 0.25 m', 'x = 0.5 m', 'x = 1.0 m', 'x = 1.5 m']

# Coeficientes da parábola: y = ax^2 + bx + c
a = -1.5
b = 0
c = 1.5

# Configurações do gráfico
fig, axes = plt.subplots(1, 4, figsize=(20, 6), gridspec_kw={'wspace': 0})

# Definindo a cor da linha para todos os gráficos
cor_linha = 'r'  # Vermelho

# Intervalos fixos para os eixos
x_lim = (0, 1.5)
y_lim = (0, 1)

# Iterar sobre os arquivos e plotar os dados
for i, (arquivo, ax) in enumerate(zip(arquivos_csv, axes)):
    df = pd.read_csv(arquivo)
    
    x = df.iloc[:, 0]  # Primeira coluna
    y = df.iloc[:, 1]  # Segunda coluna
    
    ax.plot(y, x, linestyle='-', color=cor_linha)  # Usar a cor vermelha para a linha
    ax.set_xlabel('$U_x$ (m/s)')
    if i == 0:
        ax.set_ylabel('y (m)')
    else:
        ax.yaxis.set_visible(False)  # Ocultar o eixo y nos subplots que não são o primeiro
    ax.set_title(etiquetas[i])

    ax.set_xlim(x_lim)
    ax.set_ylim(y_lim)

    # Remover as spines (linhas de moldura)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Configuração dos major ticks no eixo x
    ax.xaxis.set_major_locator(MultipleLocator(0.5))  # Define major ticks a cada 0.5 unidade

    # Adicionar grid apenas para o eixo x
    ax.xaxis.grid(True)  # Adiciona o grid no eixo x

# Criar dados para a parábola
x_parabola = np.linspace(x_lim[0], x_lim[1], 500)
y_parabola = a * x_parabola**2 + b * x_parabola + c

# Plotar a parábola apenas no último subplot
axes[-1].plot(y_parabola, x_parabola, color='k', linestyle='-', label='Solução Analítica')
axes[-1].legend()

plt.subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.15)

rect = plt.Rectangle((0, 0), 1, 1, transform=fig.transFigure, color='none', linewidth=2, edgecolor='black')
fig.patches.append(rect)

plt.savefig('Perfil_Ux_lado_a_lado.png')
plt.close()

print('Gráficos salvos como Perfil_Ux_lado_a_lado.png.')

