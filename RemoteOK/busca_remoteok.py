from  dataclasses import dataclass
import httpx

url = "https://remoteok.com/api?api=1"

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
    job_list = httpx.get(url).json()[1:]
    return [job_b.job_json(job_post) for job_post in job_list]
