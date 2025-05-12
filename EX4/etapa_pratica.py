import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('penguins.csv')

print("""
    1) Quais atributos são categóricos e quais atributos são numéricos? 
    Apenas com as informações dadas é possível identificar dentre os 
    atributos numéricos quais são os tipos?
""")
# Ignorar colunas de metadata irrelevante
df_limpo = df.drop(columns=['studyName', 'Sample Number', 'Individual ID', 'Comments'])

# Identificar os tipos de dados
atributos_categoricos = df_limpo.select_dtypes(include=['object']).columns.tolist()
atributos_numericos = df_limpo.select_dtypes(include=['float64', 'int64']).columns.tolist()

print("Atributos categóricos:", atributos_categoricos)
print("Atributos numéricos:", atributos_numericos)

########################################################################################

print("""
    2) Existem dados faltantes no conjunto de dados? Quantos e em quais features?
""")

dados_faltantes = df.isnull().sum()
dados_faltantes = dados_faltantes[dados_faltantes > 0]
print("Colunas com dados faltantes:")
print(dados_faltantes)

########################################################################################

print("""
    3) Quais espécies de pinguim existem no conjunto de dados? As classes estão balanceadas?
""")

contador_especies = df['Species'].value_counts()
print(contador_especies)

# Verificar balanceamento
porcentagem_especies = contador_especies / contador_especies.sum() * 100
print("\nDistribuição percentual:")
print(porcentagem_especies)

########################################################################################

print("""
    4) Pesquise como plotar um boxplot usando a biblioteca Seaborn. 
    Escreva o código necessário para criar o gráfico mostrado a seguir. 
    Escreva uma pequena análise sobre o gráfico gerado.
""")

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Island', y='Culmen Length (mm)', hue='Species', palette='Set1')
plt.title('Comprimento do Bico vs. Espécie por Ilha')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("boxplot.png")
plt.show()

print("Análise: O boxplot mostra que a espécie Gentoo tem, em média, o maior comprimento de bico, seguida da Chinstrap e da Adelie. Há sobreposição entre Adelie e Chinstrap.")

########################################################################################

print("""
    5) Faça o mesmo para o seguinte scatter plot.
""")

# Scatterplot: Comparação entre comprimento e profundidade do bico por espécie
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Culmen Length (mm)', y='Culmen Depth (mm)', hue='Species', palette='Set1')
plt.title('Comprimento vs. Profundidade do Bico por Espécie')
plt.tight_layout()
plt.savefig("scatterplot.png")
plt.show()

print("Análise: O scatter plot mostra que as espécies se distribuem em regiões distintas. A Gentoo possui bicos mais longos e menos profundos, enquanto a Adelie tem bicos mais curtos e profundos.")
