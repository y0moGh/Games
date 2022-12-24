import random
import argparse

# Dice faces
DICES = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DICE_ROWS = len(DICES[1])
DICE_COLUMNS = len(DICES[1][0])
DICE_FACE_SEPARATOR = " "

# Validating the user's input 
def validation(user_answer):
    
    parser = argparse.ArgumentParser()

    if user_answer.strip() in {'1', '2', '3', '4', '5', '6'}:
        return int(user_answer)

    else:
        parser.error("Your range must not be bigger than 6")

# Rolling the numbers
def calculation(input_range):

    roll_results = []

    for number in range(input_range):

        roll = random.randint(1, 6)
        roll_results.append(roll)
    
    return roll_results

def print_draws(dice_values):

    # Generate list for dice faces
    dice_faces = []
    for number in dice_values:
        dice_faces.append(DICES[number])
    
    # Generate lists for dice rows
    dice_rows = []
    for row in range(DICE_ROWS):
        dice_components = []
        for die in dice_faces:
            dice_components.append(die[row])
        dice_strings = DICE_FACE_SEPARATOR.join(dice_components)
        dice_rows.append(dice_strings)

    # Generate header with the word RESULTS centred
    width = len(dice_rows[0])
    header = " RESULTS ".center(width, "~")

    diagram = "\n".join([header] + dice_rows)
    return diagram

# ----------- App main block ---------------

# Get and validate the user's input
user_input = (input("Give a number range between 1-6: "))
input_parsed = validation(user_input)

# Rolling the dice
roll_results = calculation(input_parsed)

# Generate the ASCII diagram
final_diagram = print_draws(roll_results)

# Display the diagram
print(f"\n{final_diagram}")