import graficos, busca_remoteok

MENU_PROMPT ="""
Escolha uma das opções
1)Adicionar novos valores a tabela
2)Criar um gráfico das cinco posições mais requisitadas 
3)Criar um gráfico com a porcetagem de uso das linguagens de programação
4)Cria um gráfico com o salário Mínimo e máximo dos 10 Cargos Mais Comuns (Mensal)
5Criar um com a média de salário por linguagem
6)
7)Feche
"""

def menu():
    while (user_input :=input(MENU_PROMPT)) != "7":
        if user_input == '1':
            busca_remoteok.buscar()
        elif user_input == '2':
            graficos.position()
        elif user_input == '3':
            graficos.lin()
        elif user_input == '4':
            graficos.sal_cargo()
        elif user_input == '5':
            graficos.sal_lin()
        elif user_input == '6':
            print('teste')
        else:
            print('Input invalido, tente novamente')

menu()