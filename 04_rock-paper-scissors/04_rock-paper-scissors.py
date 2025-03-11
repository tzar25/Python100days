from random import randint

symbols = {
    "r": "rock",
    "p": "paper",
    "s": "scissors"
}
games = 0
wins = 0
losses = 0

while True:
    choice = input("Pick (R)ock, (P)aper or (S)cissors to play or you may (Q)uit the game. ")[0].lower()
    if choice == 'q':
        print(f"Thank you for playing. You played {games} games, of which you won {wins} times, lost {losses} times "
              f"and the remaining {games-wins-losses} was a draw.")
        break
    if choice not in symbols.keys():
        print("Your choice is invalid.")
        continue
    computer = "rps"[randint(0, 2)]
    print(f"You chose {symbols[choice]}, computer chose {symbols[computer]}")
    if choice == computer:
        print("It's a draw!")
    elif (choice == 's' and computer == 'p') or choice < computer and not (choice == 'p' and computer == 's'):
        print("Congratulations! You win!")
        wins += 1
    else:
        print("Unfortunately, the computer wins this round.")
        losses += 1
    print("\n")
    games += 1
