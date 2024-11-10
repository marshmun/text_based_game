from text_based_rpg.crud.enemy import Enemy

def engage_combat(player):
    enemy_name = input("Enter the name of the enemy you wish to fight: ")
    enemy = Enemy.load(enemy_name)
    
    if not enemy:
        print("Enemy not found.")
        return

    print(f"You engage in combat with {enemy.name}!")
    
    # Basic turn-based combat loop
    while player.health > 0 and enemy.health > 0:
        player_attack = player.strength
        enemy.health -= player_attack
        print(f"You hit {enemy.name} for {player_attack} damage! Enemy health is now {enemy.health}.")

        if enemy.health <= 0:
            print(f"You defeated {enemy.name}!")
            player.experience += 10  
            player.save()
            return
        
        # Enemy attacks back
        enemy_attack = enemy.strength
        player.health -= enemy_attack
        print(f"{enemy.name} hits you for {enemy_attack} damage! Your health is now {player.health}.")

        if player.health <= 0:
            print("You have been defeated!")
            break
