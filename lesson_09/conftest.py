import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_config import DB_URL
from models import Base


@pytest.fixture(scope="session")
def engine():
    return create_engine(DB_URL, echo=False, future=True)


@pytest.fixture(scope="function")
def session(engine):
    """Сессия SQLAlchemy с автоматической очисткой изменений."""
    Session = sessionmaker(bind=engine, future=True)
    session = Session()
    try:
        yield session
    finally:
        session.rollback()
        session.close()
