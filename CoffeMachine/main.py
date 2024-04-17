MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def report():
    print(f"water:{resources['water']}\nmilk:{resources['milk']}\ncoffe:{resources['coffee']}\nmoney: ${resources['money']}")


def make_coffee(coffee):
    global resources
    resources['water'] -= MENU[coffee]['ingredients']['water']
    resources['milk'] -= MENU[coffee]['ingredients']['milk']
    resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
    resources['money'] += MENU[coffee]['cost']


def is_enough_material(coffee):
    if resources['water'] < MENU[coffee]['ingredients']['water'] or resources['milk'] < MENU[coffee]['ingredients']["milk"] or resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
        return False
    else:
        return True


def is_enough_money(total_money, coffee):
    if total_money >= MENU[coffee]['cost']:
        return True
    else:
        return False


def coffe_machine():
    works = True
    total_money = 0
    change = 0

    while works:
        prompt = input("What would you like? (espresso/latte/cappuccino)(type 'report' for off or type 'off' for turn off the machine.): ")

        if prompt == "report":
            report()

        if prompt == "off":
            works = False

        if prompt == "latte" or prompt == "espresso" or prompt == "cappuccino":
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            total_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

            if is_enough_money(total_money, prompt):
                if is_enough_material(prompt):
                    make_coffee(prompt)
                    change = total_money - MENU[prompt]['cost']
                    print(f"Here is {change} your change.")
                    print(f"Here is your {prompt}☕. Enjoy!!")
                else:
                    print("Sorry there is no enough material.")
            else:
                print("Sorry there is no enough money.")


coffe_machine()
