"""
Name: character_tracker.py
Author: Pedro Presidio
Date: 1/23/2025
Purpose: Create a program to help players evolve in games by tracking stats per character.
"""

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

def save_match(filename, date, kills, deaths, assists):
    """Append a new match record to the character's stats file."""
    with open(filename, "a") as file:
        file.write(f"{date} - Kills: {kills}, Deaths: {deaths}, Assists: {assists}\n")

def display_match_history(filename):
    """Display the match history for the character."""
    try:
        with open(filename, "r") as file:
            print("\nMatch History:")
            print(file.read())
    except FileNotFoundError:
        print("No match history found yet.")

def get_valid_number(prompt):
    """Prompt the user until a valid integer is provided."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def count_matches(filename):
    """Count the number of matches recorded in the file."""
    try:
        with open(filename, "r") as file:
            return sum(1 for line in file if line.strip())
    except FileNotFoundError:
        return 0

# Main program execution
print("Available League of Legends characters:")
print(", ".join(LEAGUE_CHARACTERS))

character_name = ""
while character_name.title() not in LEAGUE_CHARACTERS:
    character_name = input("Enter the character's name (or type 'exit' to quit): ").title()
    if character_name.lower() == "Exit":
        print("Exiting program.")
        exit()
    elif character_name not in LEAGUE_CHARACTERS:
        print("Invalid character name. Please choose a name from the list.")

filename = f"{character_name}_stats.txt"

while True:
    date = input("\nEnter the date of the match (e.g., 2025-04-10 or April 10): ")
    kills = get_valid_number("Enter number of Kills: ")
    deaths = get_valid_number("Enter number of Deaths: ")
    assists = get_valid_number("Enter number of Assists: ")

    save_match(filename, date, kills, deaths, assists)
    print(f"Match saved successfully! Total matches recorded: {count_matches(filename)}")

    display_match_history(filename)

    again = input("Would you like to add another match? (yes/no): ").lower()
    if again != "yes":
        print("Good luck on the Rift!")
        break
