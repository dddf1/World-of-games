import random
from currency_converter import CurrencyConverter


def get_money_interval(difficulty):
    random_number = random.randint(1,101)
    c = CurrencyConverter()
    usd_to_ils = int(c.convert(1, 'USD', 'ILS'))
    total_value = random_number * usd_to_ils
    print(f"What do you thinks is the value of {random_number} USD in ILS ?")
    interval = range(total_value - (5 - difficulty), total_value + (5 - difficulty))
    return interval


def get_guess_from_user():
    user_ils = int(input("Give us your guess now : "))
    return user_ils


def play(selected_difficulty):
    interval = get_money_interval(selected_difficulty)
    user_ils = get_guess_from_user()
    if user_ils in interval:
        print("Well done !!!")
        return True
    else:
        print("Wrong answer...")
        return False

