import os

SCORES_FILE_NAME = "/World-of-games/files/Scores.txt"
BAD_RETURN_CODE = 800


def screen_cleaner():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
