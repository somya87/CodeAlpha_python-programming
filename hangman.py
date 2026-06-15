# Hangman Game
# CodeAlpha Python Internship Task
# Created by: Aditya Saxena

import random

# List of words
words = ["python", "laptop", "github", "coding", "intern"]

# Randomly select a word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong attempts allowed
attempts = 6

print("===== Welcome to Hangman Game =====")

# Game loop
while attempts > 0:

    display_word = ""

    # Show guessed letters and hide others
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player has guessed the word
    if "_" not in display_word:
        print("\n Congratulations! You guessed the word.")
        break

    # Take input from user
    guess = input("Enter a letter: ").lower()

    # Check if letter already entered
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    # Add letter to guessed list
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print(" Correct Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Remaining Attempts:", attempts)

# If attempts become 0
if attempts == 0:
    print("\n Game Over!")
    print("The correct word was:", secret_word)

print("\nThanks for Playing!")