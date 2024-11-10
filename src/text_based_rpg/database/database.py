# src/text_based_rpg/database/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from .models import Base

DATABASE_PATH = Path(__file__).parent / "game_data.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

def create_tables():
    """Create tables in the database based on the models."""
    Base.metadata.create_all(engine)
