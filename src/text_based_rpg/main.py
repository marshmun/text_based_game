from text_based_rpg.player import Player
from text_based_rpg.database import create_tables

create_tables()
print("Database and tables initialized successfully.")

player = Player(name="Hero", health=120, strength=20, experience=15)
player.save()
print(f"Player {player.name} saved to the database.")

loaded_player = Player.load("Hero")
if loaded_player:
    print(f"Loaded player: {loaded_player.name}, Health: {loaded_player.health}, Strength: {loaded_player.strength}, Experience: {loaded_player.experience}")

loaded_player.experience += 10
loaded_player.save()
print(f"Updated player experience: {loaded_player.experience}")

loaded_player.delete()
