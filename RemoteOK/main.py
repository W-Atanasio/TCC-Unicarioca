import busca_remoteok
from database import job, get_session
import sessions
from sqlalchemy.orm import Session
from Graficos import *

MENU_PROMPT ="""
Escolha uma das opções
1)Adicionar novos valores a tabela
2)Criar um gráfico das linguagens mais utilizadas
3)
4)Feche
"""
def converter(jp: busca_remoteok.job_b) -> job:
    return job(
        id=jp.id,
        company=jp.company,
        position=jp.position,
        location=jp.location,
        tags=",".join(jp.tags),
        salary_min=jp.salary_min,
        salary_max=jp.salary_max,
        )

def buscar():
    job_list = busca_remoteok.busca_job()
    job_list = [converter(job_post) for job_post in job_list]
    with get_session() as session:
        last_job = sessions.get_last(session)
        if last_job is not None:
            job_list = [job_post for job_post in job_list if job_post.id > last_job.id]
        sessions.save(session, job_list)
    print("Banco de dados atualizado")
    
def menu():
    while (user_input :=input(MENU_PROMPT)) != "4":
        if user_input == '1':
            buscar()
        elif user_input == '2':
            lin()
        elif user_input == '3':
            sal_lin()
        else:
            print('Input invalido, tente novamente')
menu()