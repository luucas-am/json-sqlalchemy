from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.constants import DATABASE_URL

engine = create_engine(url=DATABASE_URL, echo=False, pool_pre_ping=True)

session = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
