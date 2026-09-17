from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = "sqlite:///./examination.db"

engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False}
)

sessionlocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

base = declarative_base()


def get_db():
    db = sessionlocal()

    try:
        yield db
    finally:
        db.close()