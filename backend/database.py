from sqlmodel import create_engine, SQLModel, Session
from typing import Generator
import os

# 1. Configuration & Protocol Handling
sqlite_url = "sqlite:///./database.db"
DATABASE_URL = os.getenv("DATABASE_URL", sqlite_url)

# Fix for SQLAlchemy 1.4+ / 2.0+ compatibility with Supabase/Postgres
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# 2. Engine Creation with Conditional Arguments
is_postgres = DATABASE_URL.startswith("postgresql")

connect_args = {"check_same_thread": False} if not is_postgres else {}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False 
)

# 3. Database Initialization
def init_db():
    SQLModel.metadata.create_all(engine)

# 4. Session Management
def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session