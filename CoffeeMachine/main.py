from coffeeMachineInfo import MENU, resources


QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01


def operate():
    end_operate = False
    balance = 0.0

    while not end_operate:
        user_input = (input("What would you like? (espresso/latte/cappuccino): ")).lower()
        if user_input in MENU.keys():

            required_water = MENU[user_input]['ingredients']['water']

            if user_input == "espresso":
                required_milk = 0
            else:
                required_milk = MENU[user_input]['ingredients']['milk']

            required_coffee = MENU[user_input]['ingredients']['coffee']

            if check_resources(required_water, required_milk, required_coffee):
                beverage_cost = MENU[user_input]['cost']

                print(f"The cost is ${beverage_cost}\nPlease insert coins.")
                num_quarters = float(input("How many quarters?: "))
                num_dimes = float(input("How many dimes?: "))
                num_nickles = float(input("How many nickels?: "))
                num_pennies = float(input("How many pennies? "))

                refund_amount = process_coins(num_quarters, num_dimes, num_nickles, num_pennies, beverage_cost)
                if refund_amount == -1:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    print(f"Here is ${refund_amount} in change.\nHere is your ☕, enjoy~")
                    balance += beverage_cost
                    update_resources(required_water, required_milk, required_coffee)

            else:
                print("Sorry, No sufficient resources.")
        elif user_input == "off":
            end_operate = True

        elif user_input == "report":
            print_report(balance)


def print_report(money):
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")


def check_resources(required_water, required_milk, required_coffee):
    if required_water > resources['water'] or required_milk > resources['milk'] or required_coffee > resources['coffee']:
        return False
    else:
        return True


def process_coins(in_quarter, in_dime, in_nickle, in_penny, total_cost):
    in_total = round(in_quarter * QUARTER + in_dime * DIME + in_nickle * NICKLE + in_penny * PENNY, 2)
    print(f"In money: {in_quarter * QUARTER}, change: {in_total - total_cost}")
    if in_total >= total_cost:
        return in_total - total_cost
    return -1


def update_resources(required_water, required_milk, required_coffee):
    resources['water'] -= required_water
    resources['milk'] -= required_milk
    resources['coffee'] -= required_coffee


operate()
