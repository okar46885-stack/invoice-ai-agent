from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("COPILOT_DATABASE_URL", "sqlite:///./copilot.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()


def init_db():
    # Create tables from models if they do not exist. In production use Alembic.
    from .models import Base
    Base.metadata.create_all(bind=engine)
