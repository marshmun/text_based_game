from text_based_rpg.crud.inventory import Inventory

def explore_room(player):
    print("You explore the room...")
    # Randomly add an item as a reward for exploration
    item_name = "Health Potion"
    item = Inventory(player_id=1, item_name=item_name, quantity=1)
    item.save()
    print(f"You found a {item_name} and added it to your inventory.")
