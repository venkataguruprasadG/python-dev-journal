player1_name = input("Enter your name: ")
player2_name = input("Enter your name: ")


def input_player(player_name, played_numbers):
    while True:
        try:
            raw_input = input(
                f"{player_name}, enter up to three digits (e.g. 123): "
            ).strip()

            choice = input("if you want to quit the game. press (y/n).")
            if choice.lower() == "y":
                return None

            if not raw_input.isdigit():
                print("❌ Enter only digits without spaces. Example: 123")
                continue

            if len(raw_input) == 0 or len(raw_input) > 3:
                print("❌ You must enter between 1 and 3 digits.")
                continue

            numbers = [int(ch) for ch in raw_input]

            # Rule 1: Must be consecutive
            if any(numbers[i] != numbers[i - 1] + 1 for i in range(1, len(numbers))):
                print("❌ Digits must be consecutive. Try again.")
                continue

            # Rule 2: Must start from last played number + 1
            if played_numbers:
                expected_start = played_numbers[-1] + 1
                if numbers[0] != expected_start:
                    print(f"❌ You must start from {expected_start}. Try again.")
                    continue

            # Rule 3: No duplicates
            if any(num in played_numbers for num in numbers):
                print(
                    f"❌ One or more digits have already been played. {player_name}, try again."
                )
                continue

            return numbers

        except ValueError:
            print("❌ Something went wrong. Try again.")


played_numbers = []
turn = 0  # 0 for player 1 and 1 for player 2

while True:
    current_player = player1_name if turn == 0 else player2_name
    player_input = input_player(current_player, played_numbers)

    if player_input is None:
        print(f"{current_player} quit the game.")
        winner = player2_name if turn == 0 else player1_name
        print(f"{winner} wins the game by default.")
        break

    if 21 in player_input:
        print(f"{current_player} you lose the game. ")
        winner = player2_name if turn == 0 else player1_name
        print(f"🎉 {winner} wins the game!")
        break

    played_numbers.extend(player_input)
    print("played numbers so far: ", played_numbers)

    turn = 1 - turn
