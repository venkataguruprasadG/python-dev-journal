import random


def game_Guess():
    game_guess = random.randint(1, 100)
    while True:
        try:
            user_guess_num = int(input("Enter the number: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if user_guess_num == game_guess:
            print(f"You have guessed the correct number")
            break
        elif user_guess_num < game_guess:
            print(f"The number you have guessed is less than the correct guess")
            print(f"Choose a bigger value.")
            continue
        elif user_guess_num > game_guess:
            print(f"The number you have guessed is more than the correct guess.")
            print(f"Choose a lesser value")


while True:
    print("Do you want to play again ? (yes/no)")
    play_again = input().lower()
    if play_again == "yes":
        game_Guess()
    else:
        break
