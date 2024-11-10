import random
from text_based_rpg.crud.enemy import Enemy
from text_based_rpg.class_data import class_data 

def roll_dice(sides=20):
    """Simulate rolling a dice with a specified number of sides."""
    return random.randint(1, sides)

def engage_combat(player, enemy):
    """Engages the player in combat with a specified enemy, allowing ability use."""
    print(f"You engage in combat with {enemy.name}!")

    while player.health > 0 and enemy.health > 0:
        print("\n--- Combat Menu ---")
        print("1. Attack")
        print("2. Defend")
        print("3. Use Ability")

        action = input("Choose your action: ")

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

        elif action == "2":
            print("You brace yourself to defend, reducing incoming damage.")

        elif action == "3":
            use_ability(player, enemy)  

        if enemy.health > 0:
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
        elif enemy.health <= 0:
            print(f"You defeated {enemy.name}!")
            xp_gained = 50
            player.add_experience(xp_gained)
            player.save()
            return

def use_ability(player, enemy):
    """Allows the player to select and use an ability."""
    player_class = player.player_class
    abilities = class_data[player_class]["abilities"]

    print("\nChoose an ability:")
    for idx, ability in enumerate(abilities, start=1):
        print(f"{idx}. {ability['name']} - {ability['description']}")

    ability_choice = int(input("Enter the number of the ability you want to use: ")) - 1
    selected_ability = abilities[ability_choice]
    print(f"You used {selected_ability['name']}!")

    effect = selected_ability["effect"]
    if effect == "reduce_damage":
        print("You block incoming damage, reducing it by half on the next attack.")

    elif effect == "increased_damage":
        damage = player.strength + roll_dice(6)
        print(f"Power Strike! You deal {damage} damage to {enemy.name}.")
        enemy.health -= damage

    elif effect == "defense_boost":
        print("Your defense is temporarily raised!")
        

    elif effect == "taunt":
        print(f"{enemy.name} is forced to attack you!")

    elif effect == "critical_hit":
        damage = player.strength * 2 + roll_dice(6)
        print(f"Backstab! You deal a critical hit of {damage} damage.")
        enemy.health -= damage

    elif effect == "poison":
        poison_damage = roll_dice(6)
        print(f"{enemy.name} is poisoned, taking {poison_damage} damage over time.")
        enemy.health -= poison_damage  

    elif effect == "dodge":
        print("You prepare to dodge the next attack.")

    elif effect == "escape":
        print("You use Smoke Bomb to escape combat!")

    elif effect == "aoe_damage":
        damage = player.strength + roll_dice(8)
        print(f"Fireball! You deal {damage} area damage.")
        enemy.health -= damage  

    elif effect == "damage_absorption":
        print("You create a shield that absorbs damage.")
        

    elif effect == "trap_enemy":
        print(f"You set a trap! {enemy.name} is immobilized for one turn.")
       

    elif effect == "teleport_escape":
        print("You teleport to a safe distance, avoiding the next attack.")

    elif effect == "strength_boost":
        player.strength += 5
        print(f"Your strength is boosted by 5! Current strength: {player.strength}")

    elif effect == "health_steal":
        drain_amount = roll_dice(8)
        print(f"You drain {drain_amount} health from {enemy.name}.")
        player.health += drain_amount
        enemy.health -= drain_amount

    elif effect == "stun_enemy":
        print(f"{enemy.name} is stunned and cannot act next turn.")
        

    elif effect == "instant_kill":
        if enemy.health < 10:  
            print(f"You assassinate {enemy.name} instantly!")
            enemy.health = 0
        else:
            print("The enemy is too strong to be assassinated instantly.")

    else:
        print("Ability effect not implemented.")

