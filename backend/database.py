import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool  # Import NullPool

# 1. Get the URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# 2. Fix the protocol for SQLAlchemy (postgres:// -> postgresql://)
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# 3. Configure the engine
# We use NullPool because Supabase Transaction Mode (port 6543) handles pooling for us.
engine = create_engine(
    DATABASE_URL,
    poolclass=NullPool, 
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    # Creates tables in Supabase if they don't exist
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()