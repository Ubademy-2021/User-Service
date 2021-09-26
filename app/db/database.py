from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import DATABASE_URL


def get_session_factory():
    engine = create_engine(DATABASE_URL)
    return sessionmaker(bind=engine, autocommit=False, autoflush=False)
