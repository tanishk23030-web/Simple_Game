import random
from game.utils import get_winner

def play_game():
    options = ["stone", "paper", "scissors"]

    while True:
        print("\n--- Stone Paper Scissors ---")
        user = input("Enter stone/paper/scissors (or 'back' to menu): ").lower()

        if user == "back":
            break

        if user not in options:
            print("Invalid input!")
            continue

        computer = random.choice(options)
        print(f"Computer chose: {computer}")

        result = get_winner(user, computer)
        print(result)