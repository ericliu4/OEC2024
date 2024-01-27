import pygame

global prev_mouse_state
prev_mouse_state = 0

def run_menu(game):
    
    global prev_mouse_state

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
    button_width = 300
    button_height = 80
    button_color = '#EECCFF' if mouse_state == 1 else '#FFCCFF'
    button_text_color = 'black'

    # Handle mouse cursor
    if prev_mouse_state == 0 and mouse_state == 1:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif prev_mouse_state == 1 and mouse_state == 0:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Play button
    screen.fill(button_color, (game.width/2 - button_width/2, 400, button_width, button_height))
    button_text = game.fonts['pt35'].render('Play', True, button_text_color)
    button_text_rect = button_text.get_rect(center=(game.width/2, 400 + button_height/2))
    screen.blit(button_text, button_text_rect)

    # Display score
    score_text = game.fonts['title'].render('Score: 100', True, 'black')
    score_text_rect = score_text.get_rect(center=(game.width*4/5, 540))
    screen.blit(score_text, score_text_rect)

    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            if mouse_state == 1:
                game.state = 1
        
        elif event.type == pygame.QUIT:
            
            return True
    
    # Update prev mouse state
    prev_mouse_state = mouse_state


def get_mouse_state(pos):
    
    if pos[0] > 250 and pos[0] < 550 and pos[1] > 400 and pos[1] < 480:
        return 1
    
    else:
        return 0