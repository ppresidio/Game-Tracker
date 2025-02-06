"""
    Name: tracker.py
    Author: Pedro Presidio
    Date: 1/23/2025
    Purpose:Create a program to help players evolve on games
"""

# TODO: Implement a system to reset stats if needed

def save_numbers(filename, numbers):
    """Save the list of numbers to a specified file."""
    with open(filename, "w") as file:
        for number in numbers:
            file.write(f"{number}\n")

def load_numbers(filename):
    """Load the list of numbers from a specified file. Returns an empty list if the file is missing or invalid."""
    try:
        with open(filename, "r") as file:
            return [float(line.strip()) for line in file]
    except (FileNotFoundError, ValueError):
        return []

def calculate_average(stat_type):
    """Calculate and display the average of the specified stat type."""
    filename = f"{stat_type}.txt"
    numbers = load_numbers(filename)
    
    while True:
        user_input = input(f"Enter {stat_type} (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
            save_numbers(filename, numbers)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"The average {stat_type} is: {average}")
    else:
        print(f"No {stat_type} were entered.")

# TODO: Consider adding a feature to display all stored averages at the end
for stat in ["Kills", "Deaths", "Assists"]:
    calculate_average(stat)

