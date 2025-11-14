player1_name = input("Enter your name: ")
player2_name = input("Enter your name: ")


def input_player(player_name, played_numbers):
    while True:
        try:
            raw_input = input(f"{player_name}, enter upto three digits.")

            if not raw_input.isdigit():
                print("Enter only digits without spaces.")
                continue

            if len(raw_input) == 0 or len(raw_input) > 3:
                print(f"Invalid you have entered the wrong numbers.")
                continue

            numbers = [int(ch) for ch in raw_input]

            if any(numbers[i] != numbers[i - 1] + 1 for i in range(1, len(numbers))):
                print("First the numbers must be consectuvie. Try again.")
                continue

            if any(num in played_numbers for num in numbers):
                print(f"One or more numbers have been played. {player_name} try again.")
                continue
            """for num in numbers:
                if num in played_numbers:
                    print(
                        f"This number {num} is already played. player {player_name} enter valid numbers again."
                    )
                    break
            else:"""
            return numbers
        except ValueError:
            print("Enter only integers")


played_numbers = []
turn = 0  # 0 for player 1 and 1 for player 2

while True:
    current_player = player1_name if turn == 0 else player2_name
    player_input = input_player(current_player, played_numbers)

    if 21 in player_input:
        print(f"{current_player} you lose the game. ")
        winner = player2_name if turn == 0 else player1_name
        print(f"🎉 {winner} wins the game!")
        break

    played_numbers.extend(player_input)
    print("played numbers so far: ", played_numbers)

    turn = 1 - turn
