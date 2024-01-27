import pygame

def run_menu(game):
    
    # Rename variables for convenience
    screen = game.screen
    pos = pygame.mouse.get_pos()
    mouse_state = get_mouse_state(pos)
    
    # Fill background
    BG_COLOR = '#CCE5FF'
    screen.fill(BG_COLOR)

    # Draw title
    title_text = game.fonts['title'].render('Dyslexia Disco', True, 'black')
    title_text_rect = title_text.get_rect(center=(game.width/2, 50))
    screen.blit(title_text, title_text_rect)

    # Draw buttons
    button_width = 200
    button_height = 50
    button_color = '#EECCFF' if mouse_state == 1 else '#FFCCFF'
    button_text_color = 'black'

    # Play button
    screen.fill(button_color, (game.width/2 - button_width/2, 150, button_width, button_height))
    button_text = game.fonts['pt24'].render('Play', True, button_text_color)
    button_text_rect = button_text.get_rect(center=(game.width/2, 150 + button_height/2))
    screen.blit(button_text, button_text_rect) 



    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            pass

def get_mouse_state(pos):
    
    if pos[0] > 300 and pos[0] < 500 and pos[1] > 150 and pos[1] < 200: # Play
        return 1
    
    else:
        return 0