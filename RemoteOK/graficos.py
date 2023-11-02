import matplotlib.pyplot as plt
from database import engine
import pandas as pd
  
#Gera o dataframe com os dados do banco de dados
with engine.connect() as connection:
    #Esse replace serve para mudar os valores de que são iguais a 0 dos salarios para null
    df = pd.read_sql_table("job_rok",connection).replace(0,float('Nan'))
    
#Filtro das linguagens
li = ['java', 'go','python','javascript','ruby','php','c','c++','c#','css','sql']
#Criar uma tabela com as 5 posiçoes mais requesitadas
def position():
    df['position'].value_counts().head(5).plot(kind='barh',ylabel='')                                              
    plt.show()
    
def lin():
    #Clona a dataframe
    dft = df.copy()
    #Separa a string array 
    dft['tags'] = dft['tags'].str.split(r',')
    #Transforma cada elemento dentro da coluna tags em uma nova row
    dft = (dft.explode('tags')
           #Agrupa todas as tags e conta a quantidade de cada tipo
           .groupby('tags').size().reset_index(name='count'))
    #Filtra a dataframe
    dft = dft[dft['tags'].isin(li)]
    #Cria o gráfico
    dft['count'].plot(kind='pie', labels=dft['tags'], autopct='%1.1f%%', ylabel= ' ', title="Porcentagem das linguagens mais utilizadas")
    plt.show()

def sal_cargo():    
    #Clona a dataframe
    dft = df.copy()
    # Divida os salários por 12 para representá-los mensalmente
    dft['salary_min'] /= 12
    dft['salary_max'] /= 12
    
    # Encontre os 10 cargos mais frequentes
    top_10_cargos = dft['position'].value_counts().head(10).index
    # Filtrar o DataFrame para incluir apenas os 10 cargos mais frequentes
    df_filtrado = dft[dft['position'].isin(top_10_cargos)]
    
    # Agrupe por cargo e calcule o salário mínimo e máximo
    salarios_por_cargo = df_filtrado.groupby('position').agg({'salary_min': 'min', 'salary_max': 'max'})
    # Plote o gráfico de barras empilhadas
    salarios_por_cargo.plot(kind='bar', stacked=True, figsize=(10, 6),
                            xlabel='Cargos',
                            ylabel='Salário Mensal',
                            title='Salário Mínimo e Máximo dos 10 Cargos Mais Comuns (Mensal)',
                            )
    plt.xticks(rotation=35)  # Rotaciona os rótulos do eixo x para melhor legibilidade
    plt.legend(title='Tipo de Salário', labels=['Mínimo', 'Máximo'])
    plt.tight_layout()
    plt.show()
    
def sal_lin():
    #Clona a dataframe
    dft = df.copy()
    dft['tags'] = dft['tags'].str.split(r',')
    dft = dft.explode('tags')
    dft = dft[dft['tags'].isin(li)]
    media = []
    #Loop para calcular a media de cada linguagem, primeiro faz a media do min e max de cada linha e depois a media do resultado de cada linha
    for i in li:
        media.append(dft[(dft['tags'] == i)][['salary_min', 'salary_max']].mean().mean())
    #Cria o gráfico de barras
    cores = ['orange', 'skyblue', 'lightgreen', 'gold', 'red', 'steelblue', 'gray', 'tan', 'lightgray', 'blue', 'lightgreen']
    plt.figure(figsize=(9, 6))
    plt.bar(li, media, color=cores)
    plt.xlabel('Linguagens')
    plt.ylabel('Média de salário')
    plt.title('Média de salário por linguagem')
    plt.show()
