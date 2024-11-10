from text_based_rpg.crud.player import Player
from text_based_rpg.database import create_tables
from text_based_rpg.game_logic.combat import engage_combat
from text_based_rpg.game_logic.exploration import explore_room
from text_based_rpg.game_logic.inventory_logic import manage_inventory


def main():
    # Initialize the database and tables
    create_tables()

    # Create or load a player
    player_name = input("Enter your character's name: ")
    player = Player.load(player_name)
    if not player:
        print("Creating a new character...")
        player = Player(name=player_name)
        player.save()
        print(f"Welcome, {player.name}!")

    # Main game loop
    while True:
        print("\n--- Main Menu ---")
        print("1. Explore")
        print("2. Manage inventory")
        print("3. Save and quit")

        choice = input("Choose an action: ")

        if choice == "1":
            enemy = explore_room(player)
            if enemy:
                engage_combat(player, enemy)  
        elif choice == "2":
            manage_inventory(player)
        elif choice == "3":
            player.save()
            print(f"Game saved. Goodbye, {player.name}!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
