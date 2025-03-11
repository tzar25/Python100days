import random

length = int(input("How many characters should your password contain? "))
specs = int(input("How many of them should be special characters? "))
numbers = int(input("How many numbers? "))
if length-specs-numbers < 0:
    print("You have given invalid arguments.")
    exit()

numbers_list = list("0123456789")
specs_list = list("#$!?+-~/=%&*")
letters_list = ""

for i in range(26):
    char = 'a'
    letters_list = letters_list + chr(ord(char)+i) + chr(ord(char)+i).upper()
letters_list = list(letters_list)

password = (random.choices(numbers_list, k=numbers) + random.choices(specs_list, k=specs) +
            random.choices(letters_list, k=length - specs - numbers))
random.shuffle(password)

print("Your password is " + "".join(password))
