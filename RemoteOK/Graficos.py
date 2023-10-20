import matplotlib.pyplot as plt
import numpy as np
from database import engine
from sqlalchemy import text

  
#Pega os valores da tabela
with engine.connect() as connection:
    result = connection.execute(text("select company from job_rok"))
   

#Listas que recebem os valores da tabela
c = []
p = []

#Repetiçao para adicionar os itens na lista
for row in result:
    c.append(str(row[0]))
    
#testando se os valores foram adicionados na lista
print(c)

#criação da tabela