from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

SQLALCHEMY_DATABASE_URL = "postgres://dnelosexrgszoz:d0bcea04baf4cb598c261aea150aed55871cc7e65778b78c29b6201f98ddc98a@ec2-34-194-123-31.compute-1.amazonaws.com:5432/dcmlmhd3ipa6a5"

def get_database_url(database_url: str) -> str:
    uri = database_url
    if uri.startswith("postgres://"):
        return uri.replace("postgres://", "postgresql://", 1)
    return uri

engine = create_engine(get_database_url(SQLALCHEMY_DATABASE_URL))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
