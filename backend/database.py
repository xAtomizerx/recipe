from sqlmodel import create_engine, SQLModel, Session
from typing import Generator
import os

sqlite_url = "sqlite:///./database.db"
DATABASE_URL = os.getenv("DATABASE_URL", sqlite_url)

# CRITICAL FIX: Ensure the protocol is correct for SQLAlchemy/SQLModel
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# SQLite needs 'check_same_thread', but Postgres does not
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Create database engine
engine = create_engine(
    DATABASE_URL, 
    connect_args=connect_args
)

#initialize the database
def init_db():
    SQLModel.metadata.create_all(engine)

#pass on the session
def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session