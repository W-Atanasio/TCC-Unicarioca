import matplotlib.pyplot as plt
import numpy as np
from database import engine
from sqlalchemy import text
import pandas as pd
  
#Gera o dataframe com os dados do banco de dados
with engine.connect() as connection:
    df = pd.read_sql_table("job_rok",connection)


#Criar uma tabela com as 5 posiçoes mais requesitadas
def position():
    df['position'].value_counts().head(5).plot(kind='barh',ylabel='')                                              
    plt.show()
    
def linguagens():
    #Clona a dataframe
    dft = df
    #Filtro das linguagens
    li = ['java', 'go','python','javascript','ruby','php','c','c++','c#','css','sql']
    #Separa a string
    dft['tags'] = dft['tags'].str.split(r',')
    #Separa a lista em uma row
    dft = dft.explode('tags')
    # Group by e contagem
    dft = dft.groupby('tags', sort=True).size().reset_index(name='count')
    #Filtra a dataframe
    dft = dft[dft['tags'].isin(li)]
    #Cria o grafico
    dft['count'].plot(kind='pie', labels=dft['tags'], autopct='%1.1f%%', ylabel= ' ')
    plt.show()

linguagens()
