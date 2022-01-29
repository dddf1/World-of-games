import sys

sys.path.append('/Users/Rafi/PycharmProjects/WorldOfGames/World-of-games/games')

import MemoryGame
import GuessGame
import CurrencyRouletteGame


def welcome(name):
    player = str(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
    return player


def load_game():
    number_of_games = 3
    try:
        main_menu = """
    Please choose a game to play:
    1. Memory Game - A sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - Guess a number and see if you chose like the computer
    3. Currency Roulette - Try and guess the value of a random amount of USD in ILS
                """
        difficulty_level_msg = "Please choose game difficulty from 1 to 5 : "
        selected_game = int(input(main_menu))

        while selected_game < 1 or selected_game > number_of_games:
            print("Something went wrong. Please chose 1-3")
            selected_game = int(input())

        selected_difficulty = int(input(difficulty_level_msg))

        while selected_difficulty < 1 or selected_difficulty > 5:
            print("Something went wrong. Please chose 1-5")
            selected_difficulty = int(input())

        if selected_game == 1:
            MemoryGame.play(selected_difficulty)
        elif selected_game == 2:
            GuessGame.play(selected_difficulty)
        elif selected_game == 3:
            CurrencyRouletteGame.play(selected_difficulty)

    except ValueError:
        print("No.. Please enter a number")
        load_game()
