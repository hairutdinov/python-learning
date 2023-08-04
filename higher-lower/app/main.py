import random
from replit import clear
from operator import itemgetter
from art import logo, vs
from game_data import data

score = 0
options = [
    {
        "name": "A",
        "account": None
    },
    {
        "name": "B",
        "account": None
    },
    # {
    #     "name": "C",
    #     "account": None
    # },
]

def selected_accounts_list():
    return list(map(lambda opt: opt["account"], options))

def account_alreay_exists_in_list(account):
    return account in selected_accounts_list()

def fill_empty_options_account(account, options):
    for option in options:
        if option["account"] == None:
            rand_account = random.choice(account)
            while account_alreay_exists_in_list(rand_account):
                rand_account = random.choice(account)
            option["account"] = rand_account

def account_description(account):
    name, description, country = itemgetter('name', 'description', 'country')(account)
    return f"{name}, {description}, from {country}" 

def print_options():
    for index in range(0, len(options)):
        if index != 0:
            print(vs)
        print(f"Option {options[index]['name']}: {account_description(options[index]['account'])}")

def answer_is_correct(user_choice, options):
    user_choice_opt_idx = list(map(lambda o: o['name'], options)).index(user_choice)
    user_choice_option = options[user_choice_opt_idx]
    for option in options:
        if option['account'] != user_choice_option["account"]:
            if user_choice_option["account"]['follower_count'] < option['account']['follower_count']:
                return False
    return True

def shift_options(options):
    for idx in range(1, len(options)):
        options[idx-1]["account"] = options[idx]["account"]
    options[len(options)-1]["account"] = None

def options_names_list():
    return list(map(lambda o: f"'{o['name']}'", options))

def game():
    global score
    fill_empty_options_account(data, options)
    print(logo)
    print_options()
    option_names = " or ".join(options_names_list())
    user_choice = input(f"Who has more followers? Type {option_names}: ")
    clear()
    if user_choice not in list(map(lambda o: o['name'], options)):
        return game()
    
    if answer_is_correct(user_choice, options):
        score += 1
        shift_options(options)
        game()
    else:
        print(f"Sorry, that's wrong. Final score: {score}")

game()