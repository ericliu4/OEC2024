from classes.GameData import GameData
from pages.menu import run_menu

game = GameData()

while True:

    run_menu(game)

    game.update()