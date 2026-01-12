from sqlmodel import create_engine, SQLModel, Session
from typing import Generator
import os

SQLALCHEMY_DATABASE_URL = os.getenv("POSTGRES_URL", "postgres://postgres.gokvsygolwnixgyodtsi:fl7yPRbYoxi8Hj14@aws-1-us-east-1.pooler.supabase.com:6543/postgres?sslmode=require&supa=base-pooler.x")
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