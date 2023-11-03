from sqlalchemy import Column, Integer, String,create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager


#Configurações do SQLalchemy
engine = create_engine("mysql+pymysql://root:r8lh5pq9ts@localhost:3306/teste1")  
class Base(DeclarativeBase):
    pass
Sessionl = sessionmaker(bind=engine)

#
@contextmanager
def get_session() -> Session:
    session = Sessionl()
    yield session
    session.commit()
    session.close()
    
    
#Tabela
class job(Base):
    __tablename__ = "job_rok"
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(255), nullable=False)
    position = Column(String(255), nullable=False)
    location = Column(String(255), nullable=True)
    tags = Column(String(255), nullable=False)
    salary_min = Column(Integer, nullable=False)
    salary_max = Column(Integer, nullable=False)
    


def criar():
    Base.metadata.create_all(bind=engine)
    
