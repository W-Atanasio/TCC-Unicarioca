from  dataclasses import dataclass
import httpx
from database import job, get_session
import sessions
from sqlalchemy.orm import Session

url = "https://remoteok.com/api"
#Classe para armazenar jobs
@dataclass(frozen=True)
class job_b:
    id: int
    company: str
    position: str 
    location: str
    tags: list[str]
    salary_min: int
    salary_max: int
    @staticmethod
    def job_json(json):
        #Recebe os valores em json e os coloca em variaveis 
        return job_b(
        id=int(json['id']),
        company=json['company'],
        position=json['position'],
        location=json['location'],
        tags=json['tags'],
        salary_min=int(json['salary_min']),
        salary_max=int(json['salary_max'])
        )

def busca_job() -> list[job_b]:
    #Pega os dados em formato json
    job_list = httpx.get(url).json()[1:]
    return [job_b.job_json(job_post) for job_post in job_list]


def converter(jp: job_b) -> job:
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
    job_list = busca_job()
    job_list = [converter(job_post) for job_post in job_list]
    with get_session() as session:
        #Pega o id do ultimo job adicionado
        last_job = sessions.get_last(session)
        #Somente adiciona valores maiores que o ultimo id adicionado para evitar jobs duplicados
        if last_job is not None:
            job_list = [job_post for job_post in job_list if job_post.id > last_job.id]
        sessions.save(session, job_list)
    print("Banco de dados atualizado")

