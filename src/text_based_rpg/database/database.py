from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from .models import Base

# Define the path for the SQLite database file
DATABASE_PATH = Path(__file__).parent / "game_data.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory bound to this engine
Session = sessionmaker(bind=engine)

def create_tables():
    """Create tables in the database based on the models."""
    Base.metadata.create_all(engine)
