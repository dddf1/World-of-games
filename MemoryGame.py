import random
import time
import os


def generate_sequence(difficulty):
    sequence = []
    for number in range(0, difficulty):
        sequence.append(random.randint(1, 101))
    print(sequence)
    time.sleep(0.7)
    clear_screen()
    return sequence


def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def get_list_from_user(difficulty):
    user_numbers = []
    for user_number in range(0, difficulty):
        print(f'Give us the {user_number + 1} number :')
        user_numbers.append(int(input()))
    return user_numbers


def is_list_equal(sequence, user_numbers):
    if sequence == user_numbers:
        print("Cool! You won!")
        return True
    else:
        print("Sorry, lets try again...")


def play(selected_difficulty):
    sequence = generate_sequence(selected_difficulty)
    user_numbers = get_list_from_user(selected_difficulty)
    if is_list_equal(sequence, user_numbers):
        return True
    else:
        return False

