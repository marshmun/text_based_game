from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Player(Base):
    __tablename__ = 'Player'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, default=100)
    strength = Column(Integer, default=10)
    experience = Column(Integer, default=0)

class Inventory(Base):
    __tablename__ = 'Inventory'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('Player.id'))
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, default=1)

class Enemies(Base):
    __tablename__ = 'Enemies'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer)
    strength = Column(Integer)

class Rooms(Base):
    __tablename__ = 'Rooms'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)

class GameLogs(Base):
    __tablename__ = 'GameLogs'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('Player.id'))
    action = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)