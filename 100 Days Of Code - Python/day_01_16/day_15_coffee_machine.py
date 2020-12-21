import os

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def clear():
    os.system('cls')


def make_coffee():
    money = 0
    selection = get_selection()
    if selection == 'end':
        clear()
        return
    elif selection == 'report':
        print_report(money)
        make_coffee()
    elif selection == 'latte' or selection == 'espresso' or selection == 'cappuccino':
        ingredients = get_ingrediants(selection)
        payment = receive_payment(selection, ingredients)
        if payment == 0:
            return
        else:
            money += payment
    else:
        clear()
        print('Please choose a valid coffee.\n\n')
        get_selection()
    print(f'{selection.title()} made.  Enjoy!')


def get_ingrediants(coffee_type):
    '''Verifies required resources are available.  Returns ingredients or False'''
    ingredients = {}
    for ingredient, value in MENU[coffee_type]['ingredients'].items():
        try:
            if value > resources[ingredient]:
                print(
                    f'Not enough resources.  Required: {value} Available: {resources[ingredients]}')
                return False
            else:
                ingredients[ingredient] = value
                resources[ingredient] = resources[ingredient] - value
        except:
            print('Error verifying resources')
            return False
    return ingredients


def receive_payment(coffee_type, ingredients):
    total_required = round(MENU[coffee_type]["cost"], 2)
    print(
        f'Resources verified.  A {coffee_type.title()} costs ${total_required}')
    print('Please enter payment:')
    quarters = int(input('Insert Quarters: ')) * 0.25
    dimes = int(input('Insert Dimes: ')) * 0.1
    nickles = int(input('Insert nickles: ')) * 0.05
    pennies = int(input('Insert Pennies: ')) * 0.1
    total_entered = round(quarters + dimes + nickles + pennies, 2)
    if total_entered < total_required:
        print('Not enough money inserted.  Refunding money and resources.')
        for resource, val in ingredients.items():
            resources[resource] = resources[resource] + val
        return 0
    else:
        change = round(total_entered - total_required, 2)
        print(
            f'Payment accepted.  Payment: {total_entered} Cost: {total_required} .  Your change is {change}')
        return total_required


def print_report(money):
    clear()
    print('---------------- REPORT --------------------')
    for resource, val in resources.items():
        print(f'You currently have {val}ml of {resource}')
    print(f'There is currently ${money} stored in this machine')
    print('--------------------------------------------')
    print('\n\n')


def get_selection():
    print('Please make a selection:')
    print('--------------------------')
    selection = input('Latte, Espresso or Cappuccino: ').lower()
    return selection


def want_more_coffee():
    more = input('Would you like more coffee? ("Yes" or "No")').lower()
    if more == 'yes':
        return True
    else:
        return False


if __name__ == '__main__':
    want_coffee = True
    while want_coffee:
        make_coffee()
        want_coffee = want_more_coffee()
