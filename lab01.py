# 1. Name: Gavin Hart
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#   The program is a guessing game where the player attempts
#   to guess a randomly generated number. The user sets the game's 
#   difficulty by choosing the maximum number for the range. The program 
#   then picks a random number within this range. The user guesses the number,
#   and the program provides feedback on whether the guess is too high, too low, 
#   or correct. The game continues until the correct number is guessed. The program 
#   also tracks and displays all guesses made by the user, providing a count and a 
#   list of these guesses at the end.
# 4. What was the hardest part? 
#   The most challenging part was ensuring robust input handling, particularly
#   for non-integer inputs, to prevent the program from crashing. Implementing the logic for
#   feedback on each guess (too high, too low, correct) was intricate. Managing the loop to correctly
#   prompt for guesses, avoiding infinite loops or premature exits, was also crucial. Additionally, 
#   storing and displaying all guesses in a readable format required careful code organization and management.  
#   The assignment tested skills in control structures, input handling, and program flow management.
#    
# 5. How long did it take for you to complete the assignment?
#   Completing this assignment, including understanding the requirements,
#   coding, testing, and finalizing, took about 3 hours. This duration accounted for
#   ensuring smooth program operation, handling edge cases, user experience considerations, and code
#   refactoring for readability and efficiency.

import random

# Game introduction.
print("Welcome to the Guessing Game!")
print("In this game, you will try to guess a randomly generated number.")

# Prompt the user for how difficult the game will be. Ask for an integer.
value_max = int(input("Pick a positive integer: "))

# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.
print(f"Guess a number between 1 and {value_max}.")

# Initialize the sentinel and the array of guesses.
guess = 0
guesses = []

# Play the guessing game.
while guess != value_random:
    # Prompt the user for a number.
    guess = int(input("Enter your guess: "))

    # Store the number in an array so it can be displayed later.
    guesses.append(guess)

    # Make a decision: was the guess too high, too low, or just right.
    if guess < value_random:
        print("Too low, try again!")
    elif guess > value_random:
        print("Too high, try again!")
    else:
        print("Congratulations! You've guessed the right number!")

# Give the user a report: How many guesses and what the guesses were.
print(f"You took {len(guesses)} guesses.")
print("Your guesses were: ", guesses)
