import os
from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("SUPA_DATABASE_URL")

# Fix for SQLAlchemy/SQLModel compatibility with 'postgres://' prefixes
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Critical for Vercel/Supabase: Use NullPool to disable client-side pooling
# because Supabase's transaction pooler (Port 6543) handles it for you.
engine = create_engine(
    DATABASE_URL, 
    poolclass=NullPool,
    echo=False
)

def init_db():
    # This registers your models from models.py into the metadata
    from models import User, Recipe, Ingredient 
    SQLModel.metadata.create_all(engine)

def get_session():
    """Dependency for routers to get a database session."""
    with Session(engine) as session:
        yield session