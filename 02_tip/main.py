
total = float(input("What is the total of the bill? "))
percent = int(input("How much tip would you like to give (%)? "))
people = int(input("How many of you are paying? "))

print(f"Everyone needs to pay ${total * (1 + percent/100) / people:.2f}.")
