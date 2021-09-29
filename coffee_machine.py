MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_enough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry! there is not enough {item}")
            return False
    return True

def process_coins():
    print("please insert coins")
    total = int(input("how many quarters?")) * 0.25
    total += int(input("how many dimes?")) * 0.10
    total += int(input("how many nickels?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        global profit
        refund = money_received - drink_cost
        print(f"{refund} is refunded and drink is served")
        profit += drink_cost
        return True
    elif money_received < drink_cost:
        print(" sorry there is not enough money for the drink")
        return False


is_on = True
while is_on:
    choice = input("what would you like to order (espresso/latte/cappucino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"money: {profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_enough_resources(drink['ingredients']):
            payment = process_coins()
            is_transaction_successful(payment, drink['cost'])


