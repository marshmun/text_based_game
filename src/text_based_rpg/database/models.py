from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship

Base = declarative_base()

class Player(Base):
    __tablename__ = 'Player'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    health = Column(Integer, default=100)
    strength = Column(Integer, default=10)
    agility = Column(Integer, default=10)
    experience = Column(Integer, default=0)
    level = Column(Integer, default=1)
    player_class = Column(String, nullable=True)

    inventory_items = relationship("Inventory", back_populates="player")


class Inventory(Base):
    __tablename__ = 'Inventory'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('Player.id'))
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, default=1)

    player = relationship("Player", back_populates="inventory_items")

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

class CharacterClass(Base):
    __tablename__ = 'character_classes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    health = Column(Integer, nullable=False)
    strength = Column(Integer, nullable=False)
    agility = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    
    abilities = relationship("Ability", back_populates="character_class")

class Ability(Base):
    __tablename__ = 'abilities'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    effect = Column(String, nullable=False)
    power = Column(Integer, nullable=True)  
    character_class_id = Column(Integer, ForeignKey('character_classes.id'))
    
    character_class = relationship("CharacterClass", back_populates="abilities")
