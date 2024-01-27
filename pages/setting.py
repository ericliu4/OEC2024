import pygame

global mouse_state

def run_setting(game):
    global mouse_state

    screen = game.screen
    screen.blit(game.images['bg_settings'], (0, 0))

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