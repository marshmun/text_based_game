from ..database import Session
from ..database.models import Player as PlayerModel

class Player:
    def __init__(self, name, health=100, strength=10, experience=0, id=None):
        self.id = id  # Add id as an instance attribute
        self.name = name
        self.health = health
        self.strength = strength
        self.experience = experience

    def save(self):
        """Save or update the player in the database."""
        with Session() as session:
            player = session.query(PlayerModel).filter_by(name=self.name).first()
            if player:
                player.health = self.health
                player.strength = self.strength
                player.experience = self.experience
            else:
                player = PlayerModel(
                    name=self.name,
                    health=self.health,
                    strength=self.strength,
                    experience=self.experience
                )
                session.add(player)
                session.flush()  # This assigns an id to the new player object.
                self.id = player.id  # Set the id from the database record
            session.commit()

    @classmethod
    def load(cls, name):
        """Load a player by name from the database and return a Player instance."""
        with Session() as session:
            player = session.query(PlayerModel).filter_by(name=name).first()
            if player:
                return cls(
                    id=player.id,  # Pass the id to the Player instance
                    name=player.name,
                    health=player.health,
                    strength=player.strength,
                    experience=player.experience
                )
            else:
                print("Player not found.")
                return None

    def delete(self):
        """Delete the player from the database."""
        with Session() as session:
            player = session.query(PlayerModel).filter_by(name=self.name).first()
            if player:
                session.delete(player)
                session.commit()
                print(f"Player {self.name} deleted from the database.")
            else:
                print("Player not found.")
