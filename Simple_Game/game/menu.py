from game.logic import play_game

def start_game():
    while True:
        print("\n===== SIMPLE GAME MENU =====")
        print("1. Stone-Paper-Scissors")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Exiting game...")
            break
        else:
            print("Invalid choice! Try again.")