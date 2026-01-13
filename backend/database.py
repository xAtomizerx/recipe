import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool 

load_dotenv()
# 1. Get the URL from environment variable
DATABASE_URL = os.getenv("SUPA_DATABASE_URL")

# 2. Ensure DATABASE_URL is set
if not DATABASE_URL:
    raise ValueError("SUPA_DATABASE_URL environment variable is not set")

# 3. Fix the protocol for SQLAlchemy (postgres:// -> postgresql://)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# 4. Configure the engine
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