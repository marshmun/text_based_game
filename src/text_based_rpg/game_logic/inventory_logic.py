from text_based_rpg.crud.inventory import Inventory

def manage_inventory(player):
    print("\n--- Inventory Management ---")
    print("1. View Inventory")
    print("2. Use Item")
    print("3. Drop Item")
    choice = input("Choose an action: ")

    if choice == "1":
        print("Your inventory:")
        # Assuming player_id is 1 for now; adjust based on actual player setup
        items = Inventory.load(player_id=1, item_name=None)
        for item in items:
            print(f"{item.item_name} x{item.quantity}")
    
    elif choice == "2":
        item_name = input("Enter the name of the item to use: ")
        item = Inventory.load(player_id=1, item_name=item_name)
        if item and item.quantity > 0:
            item.quantity -= 1
            item.save()
            print(f"Used one {item_name}. Remaining: {item.quantity}")
        else:
            print("Item not found or out of stock.")
    
    elif choice == "3":
        item_name = input("Enter the name of the item to drop: ")
        item = Inventory.load(player_id=1, item_name=item_name)
        if item:
            item.delete()
            print(f"{item_name} removed from inventory.")
        else:
            print("Item not found.")
