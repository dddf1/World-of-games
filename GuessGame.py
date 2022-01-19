import random


def generate_number(difficulty):
    secret_number = int(random.randint(1, difficulty))
    return secret_number


def get_guess_from_user(difficulty):
    guess = int(input(f'Guess a number between 1 to {difficulty}: '))
    return guess


def compare_results(guess, secret_number):
    if guess == secret_number:
        print("Cool! You won!")
        return True
    else:
        print("Sorry, maybe next time...")
    print(f'Your guess number is {guess} and the secret number was {secret_number}')


def play(selected_difficulty):
    guess = get_guess_from_user(selected_difficulty)
    secret_number = generate_number(selected_difficulty)
    if compare_results(guess, secret_number):
        return True
    else:
        return False

