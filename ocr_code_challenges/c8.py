import random
import json

# Define possible options
CLASSES = ["Warrior", "Mage", "Rogue", "Paladin", "Archer", "Monk"]
GENDERS = ["Male", "Female", "Non-binary"]
ABILITIES = [
    "Fireball", "Stealth", "Healing", "Berserk", "Archery", "Alchemy",
    "Sword Mastery", "Shield Block", "Lightning Strike", "Animal Taming"
]
TRADES = ["Blacksmith", "Herbalist", "Merchant", "Hunter", "Cook", "Miner"]

def get_user_rules():
    print("Set stat rules (press Enter for defaults):")
    min_stat = int(input("Minimum stat value (default 5): ") or 5)
    max_stat = int(input("Maximum stat value (default 20): ") or 20)
    num_abilities = int(input("Number of abilities (default 2): ") or 2)
    num_trades = int(input("Number of trades (default 1): ") or 1)
    return min_stat, max_stat, num_abilities, num_trades

def generate_character(min_stat, max_stat, num_abilities, num_trades):
    character = {
        "Class": random.choice(CLASSES),
        "Gender": random.choice(GENDERS),
        "Stats": {
            "Strength": random.randint(min_stat, max_stat),
            "Magic": random.randint(min_stat, max_stat),
            "Dexterity": random.randint(min_stat, max_stat)
        },
        "Abilities": random.sample(ABILITIES, num_abilities),
        "Trades": random.sample(TRADES, num_trades)
    }
    return character

def save_character(character, filename):
    with open(filename, "w") as f:
        json.dump(character, f, indent=4)
    print(f"Character saved to {filename}")

def main():
    min_stat, max_stat, num_abilities, num_trades = get_user_rules()
    character = generate_character(min_stat, max_stat, num_abilities, num_trades)
    print("\nGenerated Character:")
    print(json.dumps(character, indent=4))
    filename = input("Enter filename to save character (default: character.json): ") or "character.json"
    save_character(character, filename)

if __name__ == "__main__":
    main()