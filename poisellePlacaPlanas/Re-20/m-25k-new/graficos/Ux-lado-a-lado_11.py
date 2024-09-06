import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Rectangle

# Lista com os nomes dos arquivos CSV e etiquetas
arquivos_csv = [
    '../postProcessing/sampleU/1000/linhaA.csv',
    '../postProcessing/sampleU/1000/linhaB.csv',
    '../postProcessing/sampleU/1000/linhaC.csv',
    '../postProcessing/sampleU/1000/linhaD.csv'
]
etiquetas = ['x = 0.25 m', 'x = 0.5 m', 'x = 1.0 m', 'x = 1.5 m']

# Coeficientes da parábola
a, b, c = -1.5, 0, 1.5

# Configurações do gráfico
fig, axes = plt.subplots(1, 4, figsize=(20, 6), gridspec_kw={'wspace': 0})
cor_linha = 'r'  # Vermelho
x_lim, y_lim = (0, 1.5), (0, 1)

for i, (arquivo, ax) in enumerate(zip(arquivos_csv, axes)):
    df = pd.read_csv(arquivo)
    x, y = df.iloc[:, 0], df.iloc[:, 1]

    ax.plot(y, x, linestyle='-', color=cor_linha)
    ax.set_xlabel('$U_x$ (m/s)')
    if i == 0:
        ax.set_ylabel('y (m)')
    else:
        ax.yaxis.set_visible(False)
    ax.set_title(etiquetas[i])
    ax.set_xlim(x_lim)
    ax.set_ylim(y_lim)

    # Remover as spines (linhas de moldura)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Definir o espaçamento dos ticks no eixo x
    ax.xaxis.set_major_locator(MultipleLocator(0.5))
    #ax.xaxis.grid(True)  # Apenas grid no eixo x

# Dados da parábola
x_parabola = np.linspace(x_lim[0], x_lim[1], 500)
y_parabola = a * x_parabola**2 + b * x_parabola + c

# Plotar a parábola no último subplot
axes[-1].plot(y_parabola, x_parabola, color='k', linestyle='-', label='Solução Analítica')
axes[-1].legend()

# Ajuste dos subplots
#fig.subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.25)  # Ajuste inferior para a régua
ruler_height = 0.005  # Altura da régua

# Adicionar régua horizontal na parte inferior da figura
rect = Rectangle(
    (0, -ruler_height), 1, ruler_height, transform=fig.transFigure, color='black', linestyle='--', linewidth=1
)
fig.patches.append(rect)

# Adicionar marcações e etiquetas na régua
graduacoes = int(2 / 0.25)  # Número de graduações principais (a cada 0.25 metros)
espaco_graduacao = 0.25 / 2  # Espaço entre as graduações principais

for i in range(graduacoes + 1):
    x_pos = i * espaco_graduacao
    plt.plot([x_pos, x_pos], [-ruler_height, -ruler_height*1.5], transform=fig.transFigure, color='black', linewidth=1)
    plt.text(x_pos, -ruler_height * 2, f'{i * 0.25:.2f}m', ha='center', va='top', transform=fig.transFigure, fontsize=8)

# Salvar a figura como PNG com fundo transparente
plt.savefig('Perfil_Ux_lado_a_lado_com_regua.png', transparent=True, bbox_inches='tight')
plt.close()

print('Gráficos salvos como Perfil_Ux_lado_a_lado_com_regua.png.')

