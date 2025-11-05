"""
Word guessing Game in Python
This program is a simple word-guessing game where the user has to guess the characters
in a randomly selected word within a limited number of attempts.
The program provides feedback after each guess,
helping the user to either complete the word or lose the game based on their guesses.
"""

import random

print("Welcome to the word guessing game...!")
name = input("Enter your name: ")
print(f"Good luck! {name}")

words = [
    "hello",
    "krishna",
    "madhusudhana",
    "keshava",
    "narayana",
    "janardhana",
    "vasudeva",
]

word = random.choice(words)

guesses = 10

word_length = len(word)

dashed_str = ""
for i in range(word_length):
    dashed_str += "_"

dashed_str = list(dashed_str)

print("Guess the characters...")
print(dashed_str)
# while guesses > 0:
