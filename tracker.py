"""
Name: character_tracker.py
Author: Pedro Presidio
Date: 1/23/2025
Purpose: Create a program to help players evolve in games by tracking stats per character.
"""

# TODO: Implement a system to reset stats if needed

def save_stats(filename, stats): #AI Assisted
    """Save the dictionary of stats to a specified file.
    The stats are stored in a single line, with each stat separated by a comma.
    """
    with open(filename, "w") as file:
        file.write(",".join(f"{stat}:{value}" for stat, value in stats.items()) + "\n")

def load_stats(filename): #AI Assisted 
    """Load the dictionary of stats from a specified file.
    If the file is missing or contains invalid data, default stats (0 values) are returned.
    """
    stats = {"Kills": 0, "Deaths": 0, "Assists": 0}
    try:
        with open(filename, "r") as file:
            line = file.readline().strip()
            for entry in line.split(","):
                key, value = entry.split(":")
                stats[key] = int(value)  # Convert value to integer
    except (FileNotFoundError, ValueError):
        pass  # Return default stats if file doesn't exist or has errors
    return stats

def set_stat(character_name, stat_type):
    """Set a single stat entry for the specified character.
    The new value replaces the previous one instead of stacking.
    """
    # Define filename based on character name
    filename = f"{character_name}_stats.txt"  
    stats = load_stats(filename)  
    
    user_input = input(f"Enter new {stat_type} value for {character_name}: ")
    try:
        # Convert input to integer
        number = int(user_input)  

        # Update the specific stat
        stats[stat_type] = number  

        # Save updated stats back to file
        save_stats(filename, stats)  
        print(f"{stat_type} for {character_name} set successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")  
    
# Main program execution

# Ask for character name
character_name = input("Enter the character's name: ")  
while True:

    # Ask for stat type
    stat_type = input("Enter the stat type (Kills, Deaths, Assists) or 'done' to finish: ")  
    if stat_type.lower() == 'done':  
        break

    # Update the chosen stat
    if stat_type in ["Kills", "Deaths", "Assists"]:
        set_stat(character_name, stat_type)  

    # Handle invalid stat type input
    else:
        print("Invalid stat type. Please enter Kills, Deaths, or Assists.")  
