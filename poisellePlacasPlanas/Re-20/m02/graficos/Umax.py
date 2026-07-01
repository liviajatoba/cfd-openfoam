import pandas as pd
import matplotlib.pyplot as plt

# Defina a constante
constante_y = 1.485

# Leia o arquivo CSV
df = pd.read_csv('../postProcessing/sampleUmax/1000/linhaCentral.csv')

# Extraia os dados das colunas 1 e 2
x = df.iloc[:, 0]  # Primeira coluna
y = df.iloc[:, 1]  # Segunda coluna

# Filtra os dados onde a segunda coluna é maior ou igual à constante
x_filtered = x[y >= constante_y]
y_filtered = y[y >= constante_y]

# Encontrar o primeiro valor de x filtrado
if not x_filtered.empty:
    primeiro_valor_x = x_filtered.iloc[0]
else:
    primeiro_valor_x = None

# Criando o gráfico de linha para todos os dados, sem marcadores
plt.plot(x, y, linestyle='--', color='b')

# Adicionando os pontos filtrados no gráfico
if not x_filtered.empty:
    plt.scatter(x_filtered, y_filtered, color='r', label=f'Comprimento de entrada (0.99 Umax) = {primeiro_valor_x} m')

# Adicionando títulos e rótulos
#plt.title('Gráfico da Primeira Coluna vs Segunda Coluna')
plt.xlabel('x (m)')
plt.ylabel('Ux (m/s)')

# Adicionando o grid
plt.grid(True)

# Ativar tics menores no eixo x
plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)  # Grid principal e menor

# Adicionando a legenda somente para os pontos filtrados
plt.legend()

# Salvando o gráfico como um arquivo PNG
plt.savefig('Umax.png')

# Fechar a plotagem para liberar memória
plt.close()

print(f'Gráfico salvo como Umax.png.')

