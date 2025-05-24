import time
import random

"""Initial agent status with energy, skill, and mental state"""
agent_status = {
    "energy": 40,
    "skill": 25,
    "mental_state": 40
}

weapons = {
    "vandal": {"power": 25, "accuracy": 20},
    "phantom": {"power": 20, "accuracy": 25},
    "operator": {"power": 35, "accuracy": 10}
}

enemies = {
    "bot": {"difficulty": 10},
    "bronze": {"difficulty": 30},
    "platinum": {"difficulty": 50},
    "radiant": {"difficulty": 80}
}

def show_status():
    """Display current agent status."""
    print("\nAgent Status:")
    for key, value in agent_status.items():
        print(f"{key.capitalize()}: {value}/100")
    print()

def rest():
    """Rest to recover energy and mental state."""
    print("Agent took a break.")
    agent_status["energy"] = min(100, agent_status["energy"] + 20)
    agent_status["mental_state"] = min(100, agent_status["mental_state"] + 10)

def degrade_status():
    """Decrease agent status values over time to simulate fatigue."""
    agent_status["energy"] -= 5
    agent_status["skill"] -= 3
    agent_status["mental_state"] -= 3

def check_game_over():
    """Check if any status has dropped to zero or below, ending the game."""
    if any(v <= 0 for v in agent_status.values()):
        print("Your agent is burned out. Game Over.")
        return True
    return False

def choose_weapon():
    """Prompt user to choose a weapon."""
    print("\nChoose your weapon:")
    for w in weapons:
        print(f"- {w.title()} (Power: {weapons[w]['power']}, Accuracy: {weapons[w]['accuracy']})")
    while True:
        choice = input("Enter weapon name: ").strip().lower()
        if choice in weapons:
            return choice
        else:
            print("Invalid weapon. Try again.")

def choose_enemy():
    """Prompt user to choose an enemy."""
    print("\nChoose your opponent:")
    for e in enemies:
        print(f"- {e.title()} (Difficulty: {enemies[e]['difficulty']})")
    while True:
        choice = input("Enter enemy name: ").strip().lower()
        if choice in enemies:
            return choice
        else:
            print("Invalid enemy. Try again.")

def battle():
    """Simulate a battle between the agent and chosen enemy with selected weapon."""
    weapon_choice = choose_weapon()
    enemy_choice = choose_enemy()

    weapon = weapons[weapon_choice]
    enemy = enemies[enemy_choice]

    print(f"\nEngaging with {enemy_choice.title()} using {weapon_choice.title()}...")
    time.sleep(1)

    base = agent_status["skill"] + weapon["power"] + weapon["accuracy"] + agent_status["mental_state"]
    difficulty = enemy["difficulty"] + 50 - agent_status["energy"]

    win_chance = max(10, min(90, base - difficulty + random.randint(-10, 10)))
    result = random.randint(1, 100)

    if result <= win_chance:
        print(f"Victory! You defeated the {enemy_choice.title()}!")
        agent_status["skill"] += 8
        agent_status["mental_state"] += 8
    else:
        print(f"Defeat. The {enemy_choice.title()} won.")
        agent_status["skill"] += 3
        agent_status["mental_state"] -= 10
        agent_status["energy"] -= 10

def main():
    """Main game loop"""
    print("Welcome to Valorant Combat Trainer!")
    while True:
        show_status()
        print("Choose an action:")
        print("battle / rest / quit")
        choice = input("Action: ").strip().lower()

        if choice == "battle":
            battle()
        elif choice == "rest":
            rest()
        elif choice == "quit":
            print("Training ended. Goodbye.")
            break
        else:
            print("Invalid action. Try again.")
            continue

        degrade_status()
        if check_game_over():
            break
        time.sleep(1)

if __name__ == "__main__":
    main()
