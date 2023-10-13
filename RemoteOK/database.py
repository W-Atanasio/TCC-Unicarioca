from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql.functions import session_user
from contextlib import contextmanager


#Configurações do SQLalchemy
engine = create_engine("mysql+pymysql://root:r8lh5pq9ts@localhost:3306/teste1")  
class Base(DeclarativeBase):
    pass
Sessionl = sessionmaker(bind=engine)

#Abrir a sessão e fechar
@contextmanager
def get_session() -> Session:
    session = Sessionl()
    yield session
    session.close()



#Tabela
class job(Base):
    __tablename__ = "job_rok"
    id:Mapped[int] = mapped_column(primary_key=True,index=True)
    company:Mapped[str] = mapped_column(String(255),nullable=False)
    position:Mapped[str] = mapped_column(String(255),nullable=False)    
    tags:Mapped[str] = mapped_column(String(255),nullable=False)
    salary_min:Mapped[int] = mapped_column(nullable=False)
    salary_max:Mapped[int] = mapped_column(nullable=False)
    

def criar():
    print("teste lol")
    Base.metadata.create_all(bind=engine)