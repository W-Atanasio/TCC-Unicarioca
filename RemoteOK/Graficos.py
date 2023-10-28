import matplotlib.pyplot as plt
import numpy as np
from database import engine
from sqlalchemy import text
import pandas as pd
  
#Pega os valores da tabela
with engine.connect() as connection:
    result = connection.execute(text("select position,count(position) from job_rok group by position"))



#criação da tabela
def tabelateste(result):
    x = []
    y = []

    for row in result:
      x.append(int(row[1]))
      y.append(str(row[0]))
    fig, ax = plt.subplots()
    ax.pie(x, labels=y)
    plt.show()


with engine.connect() as connection:
    df = pd.read_sql_table("job_rok",connection)

def position():
    df['position'].value_counts().head(5).plot(kind='barh',ylabel='')                                              
    plt.show()
    
position()