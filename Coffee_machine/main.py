MENU = {
    "espresso" : {
        "ingredients" : {
            "water" : 50,
            "coffee" : 18
        },
        "cost": 150,
    },
    "latte" : {
            "ingredients" : {
                "water" : 200,
                "milk" : 150,
                "coffee" : 24
            },
            "cost": 250,
    },
    "cappuccino" : {
                "ingredients" : {
                    "water" : 250,
                    "milk" : 100,
                    "coffee" : 24
                },
        "cost": 300,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def check_resource(drink_ing):
    for x in drink_ing:
        if drink_ing[x] >= resources[x]:
            print("Sorry there is not enough water")
            return False
    return True


def transaction_status(cost, q, d, n, p):
    quarter = 25
    dime = 10
    nickle = 5
    pennie = 1
    total = quarter*q + dime*d + nickle*n + pennie*p
    if total > cost:
        remaining = total - cost
        profit = cost
        print(f"Here is {remaining} dollars in change")
        print("Transaction is successful")
        return True
    elif total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        profit = cost
        print("Transaction is successful")
        return True


def make_drink(drink_ing):
    for x in drink_ing:
        resources[x] -= drink_ing[x]


machine = "on"

while machine == "on":
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        machine = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[user_choice]
        if check_resource(drink["ingredients"]):
            print("Process coins")
            quarters = int(input("Quarters: "))
            dimes = int(input("dimes : "))
            nickles = int(input("nickles : "))
            pennies = int(input("pennies " ))
            if transaction_status(drink["cost"], quarters, dimes, nickles, pennies):
                make_drink(drink["ingredients"])
                print("Here is your latte. Enjoy!")

