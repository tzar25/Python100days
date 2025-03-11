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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


def report():
    for item in resources:
        print(f"{item}: {resources[item]}")


def resource_check(resources_, drink_):
    (water_, coffee_, milk_) = MENU[drink_]["ing"]["water"], MENU[drink_]["ing"]["coffee"], MENU[drink_]["ing"]["milk"]
    if water_ > resources_["water"]:
        print("Sorry, not enough water")
        return False
    elif coffee_ > resources_["coffee"]:
        print("Sorry, not enough coffee")
        return False
    elif milk_ > resources_["milk"]:
        print("Sorry, not enough milk")
        return False
    else:
        return True


def coin_processor(money_):
    pennies = int(input("How many pennies? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    quarters = int(input("How many quarters? "))
    return 0.01 * pennies + 0.05 * dimes + 0.01 * nickels + 0.25 * quarters >= money_


while True:
    ans = input("What would you like to drink: (E)spresso, (C)appuccino or (L)atte? ").lower()[0]
    if ans == "o":
        print("Thank you for using the coffee machine!")
        break
    if ans == "r":
        report()
        continue
    if ans not in MENU.keys():
        print("Not supported.")
        continue
    price, drink = MENU[ans]["cost"], MENU[ans]["ing"]
    water, coffee, milk = drink["water"], drink["coffee"], drink["milk"]
    if resource_check(resources, ans):
        print("Please insert money.")
        if coin_processor(price):
            resources["money"] += price
            resources["water"] -= water
            resources["coffee"] -= coffee
            resources["milk"] -= milk
            print(f"Here you go, your {DICTIONARY[ans]}, enjoy!")
            continue
        else:
            print("Sorry, not enough money.")
            continue
    else:
        continue
