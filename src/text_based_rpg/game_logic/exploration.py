import random
from text_based_rpg.crud.inventory import Inventory
from text_based_rpg.crud.enemy import Enemy

# List of possible room descriptions
room_descriptions = [
    "a dark and damp cave with strange markings on the walls",
    "a small clearing surrounded by tall trees",
    "an abandoned camp with remnants of a recent fire",
    "a narrow hallway with flickering torches",
    "a room filled with ancient statues covered in dust",
]

enemy_names = ["Goblin", "Orc", "Troll", "Skeleton", "Zombie", "Bandit", "Giant Spider"]

def random_room():
    """Selects a random room description."""
    return random.choice(room_descriptions)

def generate_random_enemy():
    """Generates and saves a random enemy with a name, health, and strength."""
    name = random.choice(enemy_names)
    health = random.randint(20, 50)  
    strength = random.randint(5, 15)  
    enemy = Enemy(name=name, health=health, strength=strength)
    enemy.save()
    return enemy

def explore_room(player):
    print("\n--- Exploration ---")
    print(f"You enter {random_room()}.")

    event_roll = random.randint(1, 10)
    
    if event_roll <= 4:
        item_name = "Health Potion"
        item = Inventory(player_id=player.id, item_name=item_name, quantity=1)
        item.save()
        print(f"You found a {item_name} and added it to your inventory.")
        
    elif event_roll <= 8:
        enemy = generate_random_enemy()
        print(f"You encountered a {enemy.name} with {enemy.health} health and {enemy.strength} strength! Prepare to fight.")
        return enemy  
        
    else:
        print("You found nothing of interest here.")
