"""
Word guessing Game in Python
This program is a simple word-guessing game where the user has to guess the characters
in a randomly selected word within a limited number of attempts.
The program provides feedback after each guess,
helping the user to either complete the word or lose the game based on their guesses.
"""

import random

print("Welcome to the Word Guessing Game!")
name = input("Enter your name: ")
print(f"Good Luck, {name}")

words = [
    "guru",
    "krishna",
    "narayana",
    "madhava",
    "kamalanayana",
    "bahubali",
    "nataraj",
    "kali",
]

word = random.choice(words)
guesses = 10
word_length = len(word)
dashed_str = ["_"] * word_length
guessed_ltrs = []

print("Guess the characters of the word.")
print(" ".join(dashed_str))

while guesses > 0:
    user_guess = input("Enter a character: ")

    if len(user_guess) != 1 or not user_guess.isalpha():
        print("Please enter only one valid character.")
        continue

    if user_guess in guessed_ltrs:
        print("you already guessed this letter. Try another one.")
        continue

    guessed_ltrs.append(user_guess)

    if user_guess in word:
        print("✅ Correct guess")
        for i in range(word_length):
            if word[i] == user_guess:
                dashed_str[i] = user_guess
    else:
        guesses -= 1
        print(f"❌ Wrong guess! You have {guesses} guesses left.")

    print(" ".join(dashed_str))

    if "_" not in dashed_str:
        print(f"Congratulations {name}! You have guessed the word {word} correctly.")
        break
else:
    print(f"\n😢 Sorry {name}, you ran out of guesses. The word was '{word}'.")
