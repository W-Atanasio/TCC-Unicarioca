from sqlalchemy.orm import Session
from database import job
from typing import Optional
#Salva informa��o no banco de dados
def save(session:Session, posts: list[job]) -> None:
    session.bulk_save_objects(posts)
    session.commit()

#Identifica o id do �ltimo item adicionado
def get_last(session: Session) -> Optional[job]:
    return session.query(job).order_by(job.id.desc()).first()