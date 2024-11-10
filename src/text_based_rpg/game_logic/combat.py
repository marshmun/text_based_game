import random
from text_based_rpg.crud.enemy import Enemy

def roll_dice(sides=20):
    """Simulate rolling a dice with a specified number of sides."""
    return random.randint(1, sides)

def engage_combat(player, enemy):
    """Engages the player in combat with a specified enemy."""
    print(f"You engage in combat with {enemy.name}!")

    while player.health > 0 and enemy.health > 0:
        action = input("Choose your action: (1) Attack (2) Defend: ")
        
        if action == "1":
            attack_roll = roll_dice()
            if attack_roll == 20:  
                damage = (player.strength + roll_dice(6)) * 2
                print(f"Critical hit! You hit {enemy.name} for {damage} damage!")
                enemy.health -= damage
            elif attack_roll > 5:  
                damage = player.strength + roll_dice(6)
                print(f"You hit {enemy.name} for {damage} damage.")
                enemy.health -= damage
            else:
                print("Your attack missed!")

            if enemy.health <= 0:
                print(f"You defeated {enemy.name}!")
                player.experience += 10
                player.save()
                return

        elif action == "2":
            print("You brace yourself to defend, reducing incoming damage.")

        enemy_attack_roll = roll_dice()
        if enemy_attack_roll > 3:  
            damage = enemy.strength + roll_dice(4)
            if action == "2":
                damage = max(0, damage - 3)  
            player.health -= damage
            print(f"{enemy.name} hits you for {damage} damage! Your health is now {player.health}.")
        else:
            print(f"{enemy.name}'s attack missed!")

        if player.health <= 0:
            print("You have been defeated!")
            break
