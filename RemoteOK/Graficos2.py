import matplotlib.pyplot as plt
import pandas as pd
from database import engine

# Gera o dataframe com os dados do banco de dados
with engine.connect() as connection:
    df = pd.read_sql_table("job_rok", connection)

# Divida os salários por 12 para representá-los mensalmente
df['salary_min'] /= 12
df['salary_max'] /= 12

# Encontre os 10 cargos mais frequentes
top_10_cargos = df['position'].value_counts().head(10).index

# Filtrar o DataFrame para incluir apenas os 10 cargos mais frequentes
df_filtrado = df[df['position'].isin(top_10_cargos)]

# Agrupe por cargo e calcule o salário mínimo e máximo
salarios_por_cargo = df_filtrado.groupby('position').agg({'salary_min': 'min', 'salary_max': 'max'})

# Plote o gráfico de barras empilhadas
salarios_por_cargo.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.xlabel('Cargos')
plt.ylabel('Salário Mensal')
plt.title('Salário Mínimo e Máximo dos 10 Cargos Mais Comuns (Mensal)')
plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.legend(title='Tipo de Salário', labels=['Mínimo', 'Máximo'])
plt.tight_layout()
plt.show()