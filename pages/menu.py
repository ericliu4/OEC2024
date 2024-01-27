import pygame
from classes.GameData import GameData 

global prev_mouse_state
prev_mouse_state = 0

global width_state, height_state
width_state, height_state = 0, 0

global button_width, button_height
button_width = 240
button_height = 45

global button_size_factor
button_size_factor = 1

def run_menu(game):
    
    global prev_mouse_state
    global width_state, height_state
    global game_width, game_height
    
    game_width = game.width
    game_height = game.height

    # Rename variables for convenience
    screen = game.screen
    pos = pygame.mouse.get_pos()
    mouse_state = get_mouse_state(pos)
    
    # Fill background
    bg = pygame.image.load('images/bg2.png')
    bg = pygame.transform.scale(bg, (game.width, game.height))
    screen.blit(bg, (0, 0))

    # Draw title
    #title_text = game.fonts['title'].render('Dyslexia Disco', True, 'black')
    #title_text_rect = title_text.get_rect(center=(game.width/2, 50))
    title_text = pygame.image.load('images/mario_title.png')
    title_text_rect = (game.width/2-616//2, 50)
    screen.blit(title_text, title_text_rect)
    
    # Cool Sprite Animation
    mario_width = 436
    mario_height = 433
    speed_factor = 10
    x_pos = (mario_width//11)*(7+width_state//speed_factor)
    y_pos = (mario_height//11)*(6+height_state)
    
    mario_animation = pygame.image.load('images/spritesheet1.png')
    cropped_region = (x_pos, y_pos, mario_width//11, mario_height//11)
    cropped_image = mario_animation.subsurface(cropped_region)
    cropped_image = pygame.transform.scale(cropped_image, (100,100))
    screen.blit(cropped_image, (150, 400))
    if width_state//speed_factor <= 3:
        width_state += 1
    else:
        width_state = 0
        height_state += 1
        if height_state >= 1:
            height_state = 0

    # Draw buttons
    play_button_color = '#EECCFF' if mouse_state == 1 else '#FFCCFF'
    settings_button_color = '#344ceb' if mouse_state == 2 else '#7434eb'
    button_text_color = 'black'

    # Handle mouse cursor
    if prev_mouse_state == 0 and mouse_state:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif prev_mouse_state and mouse_state == 0:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    # Play button
    
    global button_size_factor
    max_factor = 1.1
    if mouse_state == 1:
        play_button_image = pygame.image.load('images/-PLAY.png')
        play_button_image = pygame.transform.scale(play_button_image, (button_width*button_size_factor, button_height*button_size_factor))
        screen.blit(play_button_image, (game.width/2 - button_width*button_size_factor/2, 275))
        if button_size_factor < max_factor:
            button_size_factor += 0.01
        else:
            button_size_factor = max_factor
    else:
        play_button_image = pygame.image.load('images/-PLAY.png')
        screen.blit(play_button_image, (game.width/2 - button_width/2, 275))
        
    #screen.fill(play_button_color, (game.width/2 - button_width/2, 200, button_width, button_height))
    #button_text = game.fonts['pt35'].render('Play', True, button_text_color)
    #button_text_rect = button_text.get_rect(center=(game.width/2, 200 + button_height/2))
    #screen.blit(button_text, button_text_rect)

    # setting button
    if mouse_state == 2:
        settings_button_image = pygame.image.load('images/-SETTINGS.png')
        settings_button_image = pygame.transform.scale(settings_button_image, (button_width*button_size_factor, button_height*button_size_factor))
        screen.blit(settings_button_image, (game.width/2 - button_width*button_size_factor/2, 350))
        if button_size_factor < max_factor:
            button_size_factor += 0.01
        else:
            button_size_factor = max_factor
    else:
        settings_button_image = pygame.image.load('images/-SETTINGS.png')
        screen.blit(settings_button_image, (game.width/2 - button_width/2, 350))
    
    if mouse_state == 0:
        button_size_factor = 1
    #screen.fill(settings_button_color, (game.width/2 - button_width/4, 320, button_width/2, button_height/2))
    #button_text = game.fonts['pt20'].render('Setting', True, button_text_color)
    #button_text_rect = button_text.get_rect(center=(game.width/2, 300 + button_height/2))
    #screen.blit(button_text, button_text_rect)

    # Display score
    score = game.get_score()
    line = 'Score: ' + str(score)
    score_text = game.fonts['title'].render(line, True, 'white')
    score_text_rect = score_text.get_rect(center=(game.width*4/5, 540))
    screen.blit(score_text, score_text_rect)

    #display image
    #image = pygame.image.load('images/handwriting_image.jpg')
    #scaled_image = pygame.transform.scale(image, (250, 250))
    #screen.blit(scaled_image, (game.width/2 - scaled_image.get_width()/2, 100))

    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            if mouse_state == 1:
                game.state = 1
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if mouse_state == 2:
                game.state = 3
            
            if mouse_state == 3:
                game.set_score(0)
        
        elif event.type == pygame.QUIT:
            
            return True
    
    # Update prev mouse state
    prev_mouse_state = mouse_state


def get_mouse_state(pos):
    global button_width, button_height
    global game_width, game_height
    # Check if mouse is within "Play" button
    if pos[0] > game_width/2-button_width/2 and pos[0] < game_width/2+button_width/2 and pos[1] < 275+button_height and pos[1] > 275:
        return 1
    #Check if mouse is within "Setting" button
    if pos[0] > game_width/2-button_width/2 and pos[0] < game_width/2+button_width/2 and pos[1] < 350+button_height and pos[1] > 350:
        return 2
    # Check if mouse i within "Score" button
    if pos[0] > game_width*4/5-100 and pos[0] < game_width*4/5+100 and pos[1] < 540+50 and pos[1] > 540:
        return 3
    else:
        return 0