import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def evaluate_hand(hand: list) -> int:
    if 1 in hand and sum(hand) < 12:
        return sum(hand) + 10
    return sum(hand)


def show(player_, dealer_, opened=False):
    print(f"Your hand:     ", end="")
    for card in player_:
        print(str(card), end=" ")
    print(f"({evaluate_hand(player_)})")
    print("Dealer's hand: ", end="")
    if opened:
        for card in dealer_:
            print(card, end=" ")
        print(f"({evaluate_hand(dealer_)})")
    else:
        print(f"{dealer_[0]} ?")


while True:
    print("\n")
    dealer = [random.choice(deck) for _ in range(2)]
    player = [random.choice(deck) for _ in range(2)]

    # Case of a blackjack
    if evaluate_hand(dealer) == 21 or evaluate_hand(player) == 21:
        show(player, dealer, True)
        if evaluate_hand(dealer) == 21:
            if evaluate_hand(player) == 21:
                print("You both have Blackjacks! It's a draw!")
            else:
                print("The dealer has Blackjack! You lose!")
        else:
            print("Congratulations! You have Blackjack! You won!")
        if input("Would you like to play another game? (y/n) ").lower()[0] == 'y':
            continue
        else:
            break

    # Player's hand
    show(player, dealer)
    while input("Would you like to hit? (y/n) ").lower()[0] == 'y':
        player.append(random.choice(deck))
        show(player, dealer)
        if evaluate_hand(player) >= 21:
            break
    if evaluate_hand(player) > 21:
        print("Busted!\n")
        show(player, dealer, True)
        if input("Would you like to play another game? (y/n) ").lower()[0] == 'y':
            continue
        else:
            break

    # Dealer's hand
    while evaluate_hand(dealer) < 17 or evaluate_hand(dealer) == 17 and 1 in dealer:
        dealer.append(random.choice(deck))
    show(player, dealer, True)
    if evaluate_hand(dealer) > 21 or evaluate_hand(dealer) < evaluate_hand(player):
        print("Congratulations! You won!")
    elif evaluate_hand(dealer) == evaluate_hand(player):
        print("It's a draw!")
    else:
        print("You lose!")
    if input("Would you like to play another game? (y/n) ").lower()[0] == 'y':
        continue
    else:
        break
