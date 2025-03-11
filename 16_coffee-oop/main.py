MENU = {
    "e": {
        "ing": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5
    },
    "l": {
        "ing": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5
    },
    "c": {
        "ing": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.0
    }
}
DICTIONARY = {
    "c": "cappuccino",
    "l": "latte",
    "e": "espresso"
}


def payment_needed(drink: str) -> float:
    return MENU[drink]["cost"]


def ask_payment(required: float):
    print(f"A total of ${required} is needed.")
    pennies = int(input("How many pennies? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    quarters = int(input("How many quarters? "))
    return 0.01 * pennies + 0.05 * dimes + 0.1 * nickels + 0.25 * quarters >= required


class CoffeeMachine:
    def __init__(self, money: int, ingredients: dict):
        self.money = money
        self.ingredients = ingredients

    def report(self):
        for ing in self.ingredients.keys():
            print(f"{ing: <10}{self.ingredients[ing]}")
        print(f"money     ${self.money:.2f}")

    def make_drink(self, drink: str):
        self.money += payment_needed(drink)
        for ing in resources.keys():
            self.ingredients[ing] -= MENU[drink]["ing"][ing]


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

coffee_machine = CoffeeMachine(0.0, resources)

print("Welcome to the coffee machine.")
while True:
    choice = input("\nWhat would you like to drink? (E)spresso, (L)atte, or (C)apuccino? ").lower()[0]
    if choice == 'o':
        print("Thank you for using the coffee machine! Have a nice day!")
        break
    if choice == 'r':
        coffee_machine.report()
        continue
    if choice not in MENU.keys():
        print("Invalid drink.")
        continue

    if ask_payment(MENU[choice]["cost"]):
        for ing in coffee_machine.ingredients:
            coffee_machine.ingredients[ing] -= MENU[choice]["ing"][ing]
        coffee_machine.money += MENU[choice]["cost"]
        print(f"Here you go, your {DICTIONARY[choice]}. Enjoy!")
    else:
        print("Not enough money.")
        continue
