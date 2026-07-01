import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Lista com os nomes dos arquivos CSV
arquivos_csv = [
    '../postProcessing/sampleU/1000/linhaA.csv',
    '../postProcessing/sampleU/1000/linhaB.csv', 
    '../postProcessing/sampleU/1000/linhaC.csv',
    '../postProcessing/sampleU/1000/linhaD.csv'
]

zonas = ['Zona A', 'Zona B', 'Zona C', 'Zona D']
cores = ['#f05039', '#eebab4', '#1f449c', '#a8b6cc']

# Lista para armazenar os DataFrames
dataframes = []

# Ler dados dos arquivos CSV
for i, arquivo in enumerate(arquivos_csv):
    try:
        # Tentar ler o arquivo
        df = pd.read_csv(arquivo, sep=None, engine='python', header=None)
        
        # Verificar se a primeira linha contém cabeçalhos
        if df.iloc[0, 0] in ['x', 'y', 'z', 'U_x', 'U_y', 'U_z']:
            df = pd.read_csv(arquivo, sep=None, engine='python', skiprows=1, header=None)
        
        # Extrair colunas (assumindo que y está na coluna 0 e U_x na coluna 1)
        y = df.iloc[:, 0].values
        U_x = df.iloc[:, 1].values
        
        # Criar DataFrame organizado
        df_organizado = pd.DataFrame({'y': y, 'U_x': U_x})
        dataframes.append(df_organizado)
        
        print(f"Arquivo {arquivo} lido com sucesso!")
        print(f"  - Número de pontos: {len(df_organizado)}")
        print(f"  - Velocidade máxima: {df_organizado['U_x'].max():.3f} m/s")
        
    except Exception as e:
        print(f"Erro ao ler {arquivo}: {e}")
        print("Criando dados de exemplo...")
        
        # Criar dados de exemplo se os arquivos não forem encontrados
        y_example = np.linspace(0, 1, 50)
        
        # Perfis de velocidade com desenvolvimento ao longo do canal
        if i == 0:  # Zona A - perfil mais pistona do
            U_x_example = np.ones_like(y_example) * 1.0
        elif i == 1:  # Zona B - início do desenvolvimento
            U_x_example = 1.2 * (1 - (2*y_example - 1)**4)
        elif i == 2:  # Zona C - perfil mais desenvolvido
            U_x_example = 1.5 * (1 - (2*y_example - 1)**2)
        else:  # Zona D - perfil totalmente desenvolvido
            U_x_example = 1.8 * (1 - (2*y_example - 1)**2)
        
        df_example = pd.DataFrame({'y': y_example, 'U_x': U_x_example})
        dataframes.append(df_example)

# Configurações
L = 5  # metros

# Deslocar cada perfil para sua posição correta no eixo X
deslocamento_A = 0.0      # 0 a 0.1L = 0 a 0.5m
deslocamento_B = 0.5      # 0.1L a 0.2L = 0.5 a 1.0m
deslocamento_C = 1.0      # 0.2L a 0.3L = 1.0 a 1.5m
deslocamento_D = 1.5      # 0.3L a 0.9L = 1.5 a 4.5m

deslocamentos = [deslocamento_A, deslocamento_B, deslocamento_C, deslocamento_D]

# Criar figura
plt.figure(figsize=(12, 8))

# Plotar cada perfil na posição correta
for i, (df, zona, cor, deslocamento) in enumerate(zip(dataframes, zonas, cores, deslocamentos)):
    plt.plot(df['U_x'] + deslocamento, df['y'], color=cor, linewidth=2, label=zona)

# Configurações do gráfico
plt.title('Perfis de Velocidade U_x em Diferentes Posições ao Longo do Domínio', fontsize=14)
plt.xlabel('X(m)', fontsize=12)
plt.ylabel('Y(m)', fontsize=12)
plt.legend(loc='lower right')  # Legenda no canto inferior direito
plt.grid(True, alpha=0.3)

# Adicionar linhas verticais para marcar as transições
plt.axvline(x=deslocamento_A, color='k', linestyle='--', alpha=0.5)
plt.axvline(x=deslocamento_B, color='k', linestyle='--', alpha=0.5)
plt.axvline(x=deslocamento_C, color='k', linestyle='--', alpha=0.5)
plt.axvline(x=deslocamento_D, color='k', linestyle='--', alpha=0.5)
plt.axvline(x=4.5, color='k', linestyle='--', alpha=0.5)

# Adicionar anotações
plt.text(0.25, 0.9, 'Zona A', ha='center', fontweight='bold', backgroundcolor='white')
plt.text(0.75, 0.9, 'Zona B', ha='center', fontweight='bold', backgroundcolor='white')
plt.text(1.25, 0.9, 'Zona C', ha='center', fontweight='bold', backgroundcolor='white')
plt.text(3.0, 0.9, 'Zona D', ha='center', fontweight='bold', backgroundcolor='white')

plt.xlim(-0.1, 5.0)
plt.ylim(0, 1.0)
plt.tight_layout()

# Salvando o gráfico como um arquivo PNG
plt.savefig('Perfil_Pistonado.png', dpi=300, bbox_inches='tight')
plt.show()


# Gráfico alternativo: sobreposição dos perfis para comparação
plt.figure(figsize=(10, 8))

for i, (df, zona, cor) in enumerate(zip(dataframes, zonas, cores)):
    plt.plot(df['U_x'], df['y'], color=cor, linewidth=2, label=zona)

plt.title('Comparação dos Perfis de Velocidade U_x (sobrepostos)', fontsize=14)
plt.xlabel('Velocidade U_x', fontsize=12)
plt.ylabel('Coordenada Y', fontsize=12)
plt.legend(loc='lower right')  # Legenda no canto inferior direito
plt.grid(True, alpha=0.3)
plt.xlim(0, max([df['U_x'].max() for df in dataframes]) * 1.1)
plt.ylim(0, 1.0)
plt.tight_layout()
plt.savefig('Perfis_Sobrepostos.png', dpi=300, bbox_inches='tight')
plt.show()