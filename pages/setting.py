import pygame

global mouse_state

def run_setting(game):
    global mouse_state

    screen = game.screen
    screen.blit(game.images['bg_settings'], (0, 0))
    screen.blit(game.images['text_settings'], (game.width/2 - game.images['text_settings'].get_width()/2, 50))
    screen.blit(game.images['button_menu'], (game.width/2 - game.images['button_menu'].get_width()/2, 500))

    # Handle pygame events
    for event in pygame.event.get():

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_pressed = True
            
        # Mouse release
        elif event.type == pygame.MOUSEBUTTONUP:
            is_pressed = False

        elif event.type == pygame.QUIT:
            return True