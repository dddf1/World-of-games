import sys

sys.path.append('/Users/Rafi/PycharmProjects/WorldOfGames/World-of-games/games')

from MemoryGame import clear_screen

SCORES_FILE_NAME = open("/Users/Rafi/PycharmProjects/WorldOfGames/World-of-games/Scores.txt", "w", encoding="utf-8")
BAD_RETURN_CODE = 400
Screen_cleaner = clear_screen()

