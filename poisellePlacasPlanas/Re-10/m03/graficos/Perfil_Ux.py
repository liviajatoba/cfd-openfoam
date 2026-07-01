import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lista com os nomes dos arquivos CSV
arquivos_csv = ['../postProcessing/sampleU/1000/linhaA.csv', '../postProcessing/sampleU/1000/linhaB.csv', '../postProcessing/sampleU/1000/linhaC.csv', '../postProcessing/sampleU/1000/linhaD.csv']
etiquetas = ['x = 0.5 m', 'x = 1.0 m', 'x = 1.5 m', 'x = 4.5 m']  # Etiquetas para a legenda

# Coeficientes da parábola: y = ax^2 + bx + c
a = -1.5
b = 0
c = 1.5

# Configurações do gráfico
plt.figure(figsize=(10, 6))

# Estilos para cada arquivo
estilos = ['--', '^-', 'o-', 'x-']
cores = ['k', 'k', 'k', 'k']  # Preto para todas as linhas

# Iterar sobre os arquivos e plotar os dados
for i, (arquivo, estilo, cor) in enumerate(zip(arquivos_csv, estilos, cores)):
    # Ler o arquivo CSV
    df = pd.read_csv(arquivo)
    
    # Extraia os dados das colunas 1 e 2
    x = df.iloc[:, 0]  # Primeira coluna
    y = df.iloc[:, 1]  # Segunda coluna
    
    # Plotar os dados com o estilo e a cor apropriados
    plt.plot(x, y, estilo, color=cor, label=etiquetas[i])

# Criar dados para a parábola
x_parabola = np.linspace(min(df.iloc[:, 0]), max(df.iloc[:, 0]), 500)
y_parabola = a * x_parabola**2 + b * x_parabola + c

# Plotar a parábola com linha contínua e cor preta
plt.plot(x_parabola, y_parabola, color='k', linestyle='-', label='Solução Analítica')

# Adicionando títulos e rótulos
#plt.title('Gráfico da Primeira Coluna vs Segunda Coluna com Parábola')
plt.xlabel('y (m)')
plt.ylabel('$U_x$ (m/s)')

# Adicionando a legenda
plt.legend()

# Adicionando o grid
plt.grid(True, linestyle='--', linewidth=0.5)

# Salvando o gráfico como um arquivo PNG
plt.savefig('Perfil_Ux.png')

# Fechar a plotagem para liberar memória
plt.close()

print('Gráfico salvo como Perfil_Ux.png.')
