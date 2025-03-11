
print("Welcome to the blind auction!")
bids = {}
max_bid = 0
winner = ""

while True:
    name = input("What is your name? ")
    bid = int(input("How much do you want to bid (in $)? "))
    bids[name] = bid
    if bid > max_bid:
        max_bid = bid
        winner = name
    if input("Is there another bidder? (y/n) ").lower()[0] == 'y':
        print("\n" * 20)
    else:
        break

print("\n" * 20)
print(f"The winner is {winner} with a bid of ${max_bid}.")
