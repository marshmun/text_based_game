from ..database import Session
from ..database.models import Player as PlayerModel
from text_based_rpg.class_data import level_requirements

class Player:
    def __init__(self, name, health=100, strength=10, agility=10, experience=0, level=1, player_class=None, id=None):
        self.id = id
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.experience = experience
        self.level = level
        self.player_class = player_class

    def add_experience(self, xp):
        """Add experience points and check for level-up."""
        self.experience += xp
        print(f"{self.name} gained {xp} XP. Total XP: {self.experience}.")
        self.check_level_up()

    def check_level_up(self):
        """Check if the player qualifies for a level-up."""
        while self.level < len(level_requirements) and self.experience >= level_requirements[self.level + 1]["xp_threshold"]:
            self.level_up()

    def level_up(self):
        """Increase level and improve stats based on level requirements."""
        self.level += 1
        self.health += level_requirements[self.level]["health_increase"]
        self.strength += level_requirements[self.level]["strength_increase"]
        print(f"{self.name} leveled up to Level {self.level}!")
        print(f"Health increased to {self.health}, Strength increased to {self.strength}.")

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
