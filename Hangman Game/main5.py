import random

# Hangman stages for visual feedback
hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]

# Word selection
some_words = "apple banana mango strawberry orange grape pineapple apricot lemon"
word = random.choice(some_words.split())
chances = len(hangman_stages) - 1
wrong_guesses = 0
dashed_str = ["_"] * len(word)
user_guessed_chars = []

print("🎯 Guess the letters of the word. It's a fruit name!")
print(" ".join(dashed_str))

# Game loop
while True:
    user_input = input("Enter a character of the guessed word: ").lower()

    if len(user_input) != 1 or not user_input.isalpha():
        print("⚠️ Enter a valid single alphabet character.")
        continue
    elif user_input in user_guessed_chars:
        print("🔁 You have already guessed this character.")
        continue

    user_guessed_chars.append(user_input)

    if user_input in word:
        print("✅ Correct guess.")
        for i in range(len(word)):
            if word[i] == user_input:
                dashed_str[i] = user_input
    else:
        wrong_guesses += 1
        chances -= 1
        print(hangman_stages[wrong_guesses])
        print(f"❌ Wrong guess. You have {chances} chances left.")

    print(" ".join(dashed_str))

    if "_" not in dashed_str:
        print(f"\n🎉 Congratulations! You guessed the word '{word}' correctly.")
        break

    if chances == 0:
        print(hangman_stages[-1])
        print(f"\n😢 Sorry. You ran out of guesses. The word was '{word}'.")
        break
