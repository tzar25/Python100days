print("Welcome to treasure island. Your mission is to find the treasure.")
choice = input("You arrive at a crossroads. Do you want to go (L)eft or (R)ight? ")

if choice.lower()[0] == "l":
    choice = input("You arrive at a river. Do you want to (S))wim across, or go (D)ownwards? ")
    if choice.lower()[0] == "d":
        choice = input("You stumble upon a set of doors. Which do you want to go through? (R)ed, (Y)ellow or (B)lue? ")
        if choice.lower()[0] == "r":
            print("You were burned by fire. Game over.")
        elif choice.lower()[0] == "y":
            print("Congratulations! You found the treasure!")
        elif choice.lower()[0] == "b":
            print("You were eaten by wild beasts. Game over.")
        else:
            print("That is not a valid answer. Game over.")
    elif choice.lower()[0] == "s":
        print("In the river you are attacked by a trout. Game over.")
    else:
        print("That is not a valid answer. Game over.")
elif choice.lower()[0] == "r":
    print("You fell into a hole. Game over.")
else:
    print("That is not a valid answer. Game over.")
