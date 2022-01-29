import os

SCORES_FILE_NAME = open("/Users/Rafi/PycharmProjects/WorldOfGames/World-of-games/Scores.txt", "w", encoding="utf-8")
BAD_RETURN_CODE = 400


def screen_cleaner():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
