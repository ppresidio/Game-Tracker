"""
Name: character_tracker.py
Author: Pedro Presidio
Date: 1/23/2025
Purpose: Create a program to help players evolve in games by tracking stats per character.
"""

# TODO: Implement a system to reset stats if needed

LEAGUE_CHARACTERS = [
    "Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol",
    "Azir", "Bard", "Bel'Veth", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath",
    "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks",
    "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger",
    "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "Kai'Sa", "Kalista",
    "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled",
    "Kog'Maw", "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite",
    "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus",
    "Neeko", "Nidalee", "Nocturne", "Nunu & Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke",
    "Qiyana", "Quinn", "Rakan", "Rammus", "Rek'Sai", "Rell", "Renekton", "Rengar", "Riven", "Rumble",
    "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed",
    "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench", "Taliyah",
    "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch",
    "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vex", "Vi", "Viego", "Viktor", "Vladimir",
    "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick", "Yuumi",
    "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"
]

def save_stats(filename, stats):
    """Save the dictionary of stats to a specified file."""
    with open(filename, "w") as file:
        file.write(",".join(f"{stat}:{value}" for stat, value in stats.items()) + "\n")

def load_stats(filename):
    """Load the dictionary of stats from a specified file."""
    stats = {"Kills": 0, "Deaths": 0, "Assists": 0}
    try:
        with open(filename, "r") as file:
            line = file.readline().strip()
            for entry in line.split(","):
                key, value = entry.split(":")
                stats[key] = int(value)
    except (FileNotFoundError, ValueError):
        pass
    return stats

def set_stat(character_name, stat_type):
    """Set a single stat entry for the specified character."""
    filename = f"{character_name}_stats.txt"
    stats = load_stats(filename)
    
    user_input = input(f"Enter new {stat_type} value for {character_name}: ")
    try:
        number = int(user_input)
        stats[stat_type] = number
        save_stats(filename, stats)
        print(f"{stat_type} for {character_name} set successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main program execution
print("Available League of Legends characters:")
print(", ".join(LEAGUE_CHARACTERS))

character_name = ""
while character_name.title() not in LEAGUE_CHARACTERS:
    character_name = input("Enter the character's name (choose from the list above): ").title()
    if character_name.title() not in LEAGUE_CHARACTERS:
        print("Invalid character name. Please choose a name from the list.")

while True:
    stat_type = input("Enter the stat type (Kills, Deaths, Assists) or 'done' to finish: ")
    if stat_type.lower() == 'done':
        break
    if stat_type in ["Kills", "Deaths", "Assists"]:
        set_stat(character_name, stat_type)
    else:
        print("Invalid stat type. Please enter Kills, Deaths, or Assists.")
