from menu import MENU
# from resources import resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
coffee_machine_is_working = True


def get_drinks_list():
    return list(MENU.keys())


def process_coins():
    """prompt the user to insert coins
    and returns the monetary value of the coins"""
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def not_enough_resources(order_ingredients):
    for ingredient in order_ingredients:
        need = order_ingredients[ingredient]
        if resources[ingredient] < need:
            print(f"Sorry there is not enough {ingredient}.")
            return True
    return False


def user_inserted_enough_money(order_cost, monetary_value):
    return monetary_value >= order_cost


def add_profit(profit, order_cost):
    return profit + order_cost


def deduct_resources(resources, order_ingredients):
    for ingredient in order_ingredients:
        need = order_ingredients[ingredient]
        resources[ingredient] -= need
    return resources



def change(order_cost, monetary_value):
    change = round(monetary_value - order_cost, 2)
    if change > 0:
        print(f"Here is ${change} dollars in change.")
    return change

while coffee_machine_is_working:
    cmd = input(f"What would you like? ({'/'.join(get_drinks_list())}): ")
    drink = None

    if cmd == "off":
        coffee_machine_is_working = False
        break
    elif cmd == "report":
        print_report()
        continue
    else:
        drink = cmd
        if drink not in MENU:
            print(f"There's no such a drink {drink} in coffee machine")
            continue

    order_ingredients = MENU[drink]["ingredients"]
    order_cost = MENU[drink]["cost"]

    if not_enough_resources(order_ingredients):
        continue

    print("Please insert coins.")
    monetary_value = process_coins()

    if not user_inserted_enough_money(order_cost, monetary_value):
        print(f"Sorry that's not enough money. Money refunded.")
        continue

    profit = add_profit(profit, order_cost)
    change(order_cost, monetary_value)
    resources = deduct_resources(resources, order_ingredients)
