from sqlmodel import create_engine, SQLModel, Session
from typing import Generator
import os

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL", "sqlite:///./recipes.db")
# Create database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

#initialize the database
def init_db():
    SQLModel.metadata.create_all(engine)

#pass on the session
def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session