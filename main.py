from classes.GameData import GameData
from pages.menu import run_menu
import pages 

game = GameData()
while True:

    '''
    finite state machine:
    0 = menu  -> 1 or 2   
    1 = play  -> 3
    2 = setting  -> 0
    3 = words
    10 = word generation
    15 = user input
    20 = matching algorithm
    25 = calculation
    30 = exit game
    '''

    currstate = game.get_state()
    match currstate:
        case 0:
            pages.run_menu(game)
        case 1:
            pages.run_play(game)
        case 2: 
            pages.run_setting(game)
        case 3:
            pages.run_words(game)
        case 10:
            pages.run_generation(game)
        case 15:
            pages.run_user_input(game)
        case 20:
            pages.run_matching(game)
        case 25:
            pages.run_calculation(game)
        case 30:
            pages.run_exit(game)

    game.update()




