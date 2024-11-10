from text_based_rpg.crud.player import Player
from text_based_rpg.crud.enemy import Enemy
from text_based_rpg.crud.inventory import Inventory
from text_based_rpg.database import create_tables
from text_based_rpg.game_logic.combat import engage_combat
from text_based_rpg.game_logic.exploration import explore_room
from text_based_rpg.game_logic.inventory_logic import manage_inventory

def main():
    # Initialize the database and tables
    create_tables()

    # Create a player
    player_name = input("Enter your character's name: ")
    player = Player.load(player_name)
    if not player:
        print("Creating a new character...")
        player = Player(name=player_name)
        player.save()
        print(f"Welcome, {player.name}!")

    # Create a test enemy (only if it doesn't already exist)
    enemy_name = "Goblin"
    enemy = Enemy.load(enemy_name)
    if not enemy:
        print(f"Creating a new enemy: {enemy_name}")
        enemy = Enemy(name=enemy_name, health=50, strength=8)
        enemy.save()

    # Main game loop
    while True:
        print("\n--- Main Menu ---")
        print("1. Explore")
        print("2. Engage in combat")
        print("3. Manage inventory")
        print("4. Save and quit")

        choice = input("Choose an action: ")

        if choice == "1":
            explore_room(player)
        elif choice == "2":
            engage_combat(player)
        elif choice == "3":
            manage_inventory(player)
        elif choice == "4":
            player.save()
            print(f"Game saved. Goodbye, {player.name}!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()