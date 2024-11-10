from text_based_rpg.crud.player import Player
from text_based_rpg.crud.inventory import Inventory
from text_based_rpg.database.database import create_tables

# Initialize the database tables
create_tables()
print("Database and tables initialized successfully.")

# Create a player and save to the database
player = Player(name="Hero")
player.save()
print(f"Player {player.name} saved to the database.")

# Add items to the player's inventory
inventory_item = Inventory(player_id=1, item_name="Health Potion", quantity=3)
inventory_item.save()
print(f"Added {inventory_item.quantity} {inventory_item.item_name}(s) to inventory.")

# Load an item from the inventory
loaded_item = Inventory.load(player_id=1, item_name="Health Potion")
if loaded_item:
    print(f"Loaded item: {loaded_item.item_name}, Quantity: {loaded_item.quantity}")

# Delete an item from the inventory
loaded_item.delete()
