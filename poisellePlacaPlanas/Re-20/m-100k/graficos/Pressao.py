import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Leia o arquivo CSV
df = pd.read_csv('../postProcessing/sampleUmax/2000/linhaCentral.csv')

# Extraia os dados das colunas 1 e 5
x = df.iloc[:, 0]  # Primeira coluna
y = df.iloc[:, 4]  # Quinta coluna

# Defina o intervalo de interesse
x_min = 3  # Valor mínimo de x para considerar
x_max = 5  # Valor máximo de x para considerar

# Filtrar os dados dentro do intervalo definido
mask = (x >= x_min) & (x <= x_max)
x_filtered = x[mask]
y_filtered = y[mask]

# Função para calcular a inclinação da reta
def calcular_inclinacao(x, y):
    # Ajuste linear (reta) usando a função linregress
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    return slope

# Calcular a inclinação da reta apenas no intervalo filtrado
inclinacao = calcular_inclinacao(x_filtered, y_filtered)
print(f'Inclinação da reta no intervalo definido: {inclinacao:.2f}')

# Criando o gráfico de linha para todos os dados, sem marcadores e em preto e branco
plt.plot(x, y, linestyle='--', color='k')  # Preto e branco

# Adicionar a linha de ajuste linear no intervalo filtrado
plt.plot(x_filtered, y_filtered, linestyle='-', color='r', label=f'dP/dx = {inclinacao:.2f} Pa.s')

# Adicionando títulos e rótulos
#plt.title('Gráfico da Primeira Coluna vs Segunda Coluna')
plt.xlabel('x (m)')
plt.ylabel('p ($m^2/s^2$)')

# Adicionando o grid
plt.grid(True)

# Ativar tics menores no eixo x
plt.minorticks_on()
plt.grid(which='both', linestyle='--', linewidth=0.5)  # Grid principal e menor

# Adicionando a legenda apenas para a linha de ajuste
plt.legend()

# Salvando o gráfico como um arquivo PNG
plt.savefig('Pressao.png')

# Fechar a plotagem para liberar memória
plt.close()

print(f'Gráfico salvo como Pressao.png.')

