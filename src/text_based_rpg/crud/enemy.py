from ..database.database import Session
from ..database.models import Enemies as EnemyModel

class Enemy:
    def __init__(self, name, health=50, strength=5):
        self.name = name
        self.health = health
        self.strength = strength

    def save(self):
        """Save or update the enemy in the database."""
        with Session() as session:
            enemy = session.query(EnemyModel).filter_by(name=self.name).first()
            if enemy:
                enemy.health = self.health
                enemy.strength = self.strength
            else:
                enemy = EnemyModel(
                    name=self.name,
                    health=self.health,
                    strength=self.strength
                )
                session.add(enemy)
            session.commit()

    @classmethod
    def load(cls, name):
        """Load an enemy by name from the database and return an Enemy instance."""
        with Session() as session:
            enemy = session.query(EnemyModel).filter_by(name=name).first()
            if enemy:
                return cls(
                    name=enemy.name,
                    health=enemy.health,
                    strength=enemy.strength
                )
            else:
                print("Enemy not found.")
                return None

    def delete(self):
        """Delete the enemy from the database."""
        with Session() as session:
            enemy = session.query(EnemyModel).filter_by(name=self.name).first()
            if enemy:
                session.delete(enemy)
                session.commit()
                print(f"Enemy {self.name} deleted from the database.")
            else:
                print("Enemy not found.")
