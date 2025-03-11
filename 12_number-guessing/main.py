import random

number = random.randint(1, 100)


diff = input("Choose a difficulty. (E)asy for 15 guesses, (N)ormal for 10 and (H)ard for 7. ").lower()[0]
if diff == 'h':
    max_guess = 7
elif diff == 'n':
    max_guess = 10
else:
    max_guess = 15

print("The computer thought about a number between 1 and 100.")
while max_guess:
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"Congratulations! The number was indeed {guess}!")
        break
    if guess < number:
        print(f"Too low.")
    else:
        print("Too high")
    max_guess -= 1
    print(f"You have {max_guess} guesses left.")
else:
    print(f"Unfortunately, you didn't get the number in the allowed tries. It was {number} by the way.")
