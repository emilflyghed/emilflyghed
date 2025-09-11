import random
import sys


# Function to use colored text
def colorize(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "reset": "\033[0m",
    }
    return f"{colors.get(color, colors['reset'])}{text}{colors['reset']}"


# Settings for character
print(
    "Welcome to Emil's RPG Game.\nIn this game you will have to gain enough strength to face the dragon at the end.\n\n"
)
player_name = input("What's your name?\n")
player_class = ""
player_health = 0
MAX_HEALTH = 0
player_min_damage = 0
player_max_damage = 0
health_potions = 4

# Level function
player_level = 1
player_exp = 0
exp_level_up = 100


def level_up():
    global player_level
    if player_level < 20:
        player_level += 1
        global MAX_HEALTH
        MAX_HEALTH += 10
        global player_health
        player_health = MAX_HEALTH
        global player_min_damage
        player_min_damage += 5
        global player_max_damage
        player_max_damage += 5
        global player_exp
        global exp_level_up
        player_exp -= exp_level_up
        exp_level_up += 20
        print("Level up!")


# Function for drinking health potions
def drink_health_potion():
    global player_health, health_potions
    if health_potions > 0:
        player_health += 50
        player_health = min(player_health, MAX_HEALTH)
        health_potions -= 1
        return True
    else:
        print("You are out of Health Potions.")
        return False


# Class settings
while player_class not in ["mage", "warrior", "rogue"]:
    player_class = str(
        input(
            "\nWhich class will you play as?\nA warrior have more health but make less damage.\nA Rogue have balanced health and damage\nA Mage have less health but make more damage\n\nType your choice:\n"
        )
    ).lower()
    if player_class == "mage":
        MAX_HEALTH += 50
        player_health += 50
        player_health = min(player_health, MAX_HEALTH)
        player_min_damage += 35
        player_max_damage += 75
        break
    elif player_class == "warrior":
        MAX_HEALTH += 100
        player_health += 100
        player_health = min(player_health, MAX_HEALTH)
        player_min_damage += 25
        player_max_damage += 50
        break
    elif player_class == "rogue":
        MAX_HEALTH += 75
        player_health += 75
        player_health = min(player_health, MAX_HEALTH)
        player_min_damage += 30
        player_max_damage += 60
        break
    else:
        print("\nWrong input. Try again.\n")


# The combat function
def combat(enemy_name, enemy_health, enemy_min_damage, enemy_max_damage):
    global player_health
    gained_exp = enemy_health / 2
    print(
        f"\nA wild {colorize(enemy_name, 'red')} appears with {colorize(enemy_health, 'red')} HP!"
    )

    while enemy_health > 0 and player_health > 0:
        print(
            f"\n{player_name} HP: {colorize(player_health, 'green')}/{colorize(MAX_HEALTH, 'green')} | {colorize(enemy_name, 'red')} HP: {colorize(enemy_health, 'red')}"
        )
        player_turn = True
        while player_turn is True:
            action = input("Do you want to (a)ttack or (d)rink potion? ").lower()

            if action == "a":  # Attack
                damage = random.randint(player_min_damage, player_max_damage)
                enemy_health -= damage
                print(
                    f"You strike the {colorize(enemy_name, 'red')} for {colorize(damage, 'red')} damage!"
                )
                player_turn = False

            elif action == "d" and health_potions >= 1: # Drink potion
                if drink_health_potion():
                    print(
                        f"You drank a potion. Your HP is now {colorize(player_health, 'green')}/{colorize(MAX_HEALTH, 'green')}."
                    )
                    player_turn = False

            elif action == "d" and health_potions <= 0:  # Out of potions
                if drink_health_potion():
                    print(
                        "You're out of potions!"
                    )

            else:
                print("Invalid action!")

            # If enemy is still alive, it attacks back
        if enemy_health > 0:
            enemy_damage = random.randint(enemy_min_damage, enemy_max_damage)
            player_health -= enemy_damage
            print(
                f"The {colorize(enemy_name, 'red')} hits you for {colorize(enemy_damage, 'red')} damage!"
            )

    # Combat outcome
    if player_health <= 0:
        print("You were defeated...")
        input("Press Enter to quit the game...")
        sys.exit()
    else:
        print(f"You defeated the {colorize(enemy_name, 'red')}!")
        global player_exp
        player_exp += gained_exp
        while player_exp >= exp_level_up:
            level_up()

    input("\nPress Enter to continue...")


combat("Goblin", 50, 10, 25)
print(exp_level_up)
print(player_exp)
combat("Wolf1", 50, 5, 10)
print(exp_level_up)
print(player_exp)
combat("Wolf2", 50, 5, 10)
print(exp_level_up)
print(player_exp)
combat("Wolf3", 50, 5, 10)
print(exp_level_up)
print(player_exp)
combat("Wolf4", 50, 5, 10)
print(exp_level_up)
print(player_exp)
combat("Wolf5", 50, 5, 10)
print(exp_level_up)
print(player_exp)

print("\nGame Over")
print("Test")