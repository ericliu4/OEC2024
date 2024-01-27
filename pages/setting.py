import pygame

global prev_mouse_state
prev_mouse_state = 0

global button_size_factor
button_size_factor = 1

def run_setting(game):
    global prev_mouse_state
    global button_size_factor

    pos = pygame.mouse.get_pos()
    mouse_state = get_mouse_state(pos)

    # Draw to screen
    screen = game.screen
    screen.blit(game.images['bg_settings'], (0, 0))
    screen.blit(game.images['text_settings'], (game.width/2 - game.images['text_settings'].get_width()/2, 100))
    # Draw back, easier, harder buttons from images dictionary in vertical order
    max_factor = 1.1
    if mouse_state == 1:
        button_back = game.images['button_back']
        button_back = pygame.transform.scale(button_back, (int(button_back.get_width()*button_size_factor), int(button_back.get_height()*button_size_factor)))
        screen.blit(button_back, (game.width/2 - button_size_factor*game.images['button_back'].get_width()/2, 250))
        button_size_factor = min(max_factor, button_size_factor + 0.01)
    else:
        button_back = game.images['button_back']
        screen.blit(button_back, (game.width/2 - game.images['button_back'].get_width()/2, 250))
        
    if mouse_state == 2:
        button_easier = game.images['button_easier']
        button_easier = pygame.transform.scale(button_easier, (int(button_easier.get_width()*button_size_factor), int(button_easier.get_height()*button_size_factor)))
        screen.blit(button_easier, (game.width/2 - button_size_factor*game.images['button_easier'].get_width()/2, 325))
        button_size_factor = min(max_factor, button_size_factor + 0.01)
    else:
        button_easier = game.images['button_easier']
        screen.blit(button_easier, (game.width/2 - game.images['button_easier'].get_width()/2, 325))
    
    if mouse_state == 3:
        button_harder = game.images['button_harder']
        button_harder = pygame.transform.scale(button_harder, (int(button_harder.get_width()*button_size_factor), int(button_harder.get_height()*button_size_factor)))
        screen.blit(button_harder, (game.width/2 - button_size_factor*game.images['button_harder'].get_width()/2, 400))
        button_size_factor = min(max_factor, button_size_factor + 0.01)
    else:
        button_harder = game.images['button_harder']
        screen.blit(button_harder, (game.width/2 - game.images['button_harder'].get_width()/2, 400))
    
    if mouse_state == 0:
        button_size_factor = 1

     # Handle mouse cursor
    if prev_mouse_state == 0 and mouse_state:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif prev_mouse_state and mouse_state == 0:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Handle pygame events
    for event in pygame.event.get():

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_state == 1:
                game.state = 0
            elif mouse_state == 2:
                game.difficulty = max(1, game.difficulty - 1)
            elif mouse_state == 3:
                game.difficulty = min(3, game.difficulty + 1)

        # Mouse release
        elif event.type == pygame.MOUSEBUTTONUP:
            is_pressed = False

        elif event.type == pygame.QUIT:
            return True
        
    prev_mouse_state = mouse_state

def get_mouse_state(pos):
    # Check if mouse is within back button image
    if pos[0] > 280 and pos[0] < 520 and pos[1] > 250 and pos[1] < 295:
        return 1
    # Check if mouse is within easier button image
    elif pos[0] > 280 and pos[0] < 520 and pos[1] > 325 and pos[1] < 370:
        return 2
    # Check if mouse is within harder button image
    elif pos[0] > 280 and pos[0] < 520 and pos[1] > 400 and pos[1] < 445:
        return 3
    else:
        return 0