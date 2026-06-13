def get_winner(user, computer):
    if user == computer:
        return "It's a Draw!"

    if (
        (user == "stone" and computer == "scissors") or
        (user == "paper" and computer == "stone") or
        (user == "scissors" and computer == "paper")
    ):
        return "You Win!"

    return "Computer Wins!"