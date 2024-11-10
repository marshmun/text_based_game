from text_based_rpg.crud.player import Player
from text_based_rpg.database import create_tables
from text_based_rpg.game_logic.combat import engage_combat
from text_based_rpg.game_logic.exploration import explore_room
from text_based_rpg.game_logic.inventory_logic import manage_inventory
from text_based_rpg.class_data import class_data


def create_character(name):
    """Creates a new character with a selected class."""
    print("\nChoose your class:")
    for idx, class_name in enumerate(class_data.keys(), start=1):
        print(f"{idx}. {class_name} - {class_data[class_name]['description']}")
    
    class_choice = int(input("Enter the number of your chosen class: "))
    selected_class = list(class_data.keys())[class_choice - 1]

    attributes = class_data[selected_class]
    print(f"\nYou have chosen the {selected_class} class.")

    player = Player(
        name=name,
        health=attributes["health"],
        strength=attributes["strength"],
        agility=attributes["agility"],
        experience=0,  
        level=1,      
        player_class=selected_class
    )
    return player


def main():
    create_tables()

    print("Welcome to the game!")
    player_name = input("Enter your character's name to log in (or create a new character): ")
    player = Player.load(player_name)
    
    if player:
        print(f"Welcome back, {player.name}!")
    else:
        print("Creating a new character...")
        player = create_character(player_name)
        player.save()
        print(f"Welcome, {player.name}!")

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
