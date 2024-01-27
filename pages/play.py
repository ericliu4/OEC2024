import pygame
from easyocr import Reader

from misc.generation import run_generation
from misc.similarities import similarity_words
from misc.updateMistakes import update_mistakes

import matplotlib.pyplot as plt

global circles
circles = set()

global is_pressed
is_pressed = False

global prev_mouse_pos
prev_mouse_pos = None

global prev_mouse_state
prev_mouse_state = 0

global reader
reader = Reader(['en'])

global score_screen
score_screen = False

global detected_word


def run_play(game):

    # Register global variables
    global circles
    global is_pressed
    global prev_mouse_pos
    global prev_mouse_state
    global score_screen
    global detected_word

    screen = game.screen
    mouse_pos = pygame.mouse.get_pos()
    mouse_state = get_mouse_state(mouse_pos)

    # Draw background as hard image
    screen.blit(game.images['bg_hard'], (0, 0))

    if not score_screen:
        # Draw instruction text
        instruction_text = game.fonts['pt35'].render('WRITE THE WORD BELOW', True, 'white')
        instruction_text_rect = instruction_text.get_rect(center=(game.width/2, 100))
        screen.blit(instruction_text, instruction_text_rect)

        instruction_text_2 = game.fonts['title'].render(game.goal_word, True, 'white')
        instruction_text_2_rect = instruction_text_2.get_rect(center=(game.width/2, 150))
        screen.blit(instruction_text_2, instruction_text_2_rect)
    else:
        # Draw result text
        result_text = game.fonts['pt35'].render(f'Score +{game.prev_score}', True, 'white')
        result_text_rect = result_text.get_rect(center=(game.width/2, 100))
        screen.blit(result_text, result_text_rect)

    # Draw total score in top right
    total_score_text = game.fonts['pt35'].render(f'Total Score: {game.score}', True, 'white')
    total_score_text_rect = total_score_text.get_rect(topright=(game.width - 15, 15))
    screen.blit(total_score_text, total_score_text_rect)

    # Draw difficulty text in top left corner
    difficulty_text = game.fonts['pt35'].render(f'Difficulty:', True, 'white')
    difficulty_text_rect = difficulty_text.get_rect(topleft=(15, 15))
    screen.blit(difficulty_text, difficulty_text_rect)

    # Draw the number of shell images in top left corner equal to difficulty
    shell_image = game.images['green_shell']
    shell_image_rect = shell_image.get_rect(topleft=(140, 10))
    for i in range(game.difficulty):
        screen.blit(shell_image, shell_image_rect)
        shell_image_rect.x += 50

    # Draw box
    box_width = 600
    box_height = 300
    screen.fill('white', (game.width/2 - box_width/2, 200, box_width, box_height))

    # Draw black border around box
    border_width = 5
    pygame.draw.rect(screen, 'black', (game.width/2 - box_width/2 - border_width, 200 - border_width, box_width + border_width * 2, box_height + border_width * 2), border_width)

    if not score_screen:
        # Draw submit and clear button side by side using images
        submit_button_image = game.images['button_submit']
        submit_button_image_rect = submit_button_image.get_rect(center=(game.width/2 + 130, 550))
        screen.blit(submit_button_image, submit_button_image_rect)
        clear_button_image = game.images['button_clear']
        clear_button_image_rect = clear_button_image.get_rect(center=(game.width/2 - 130, 550))
        screen.blit(clear_button_image, clear_button_image_rect)
    else:
        # Draw next and menu button side by side using images
        next_button_image = game.images['button_next']
        next_button_image_rect = next_button_image.get_rect(center=(game.width/2 + 130, 550))
        screen.blit(next_button_image, next_button_image_rect)
        menu_button_image = game.images['button_menu']
        menu_button_image_rect = menu_button_image.get_rect(center=(game.width/2 - 130, 550))
        screen.blit(menu_button_image, menu_button_image_rect)


    # Handle mouse cursor
    if prev_mouse_state == 0 and mouse_state:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif prev_mouse_state and mouse_state == 0:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Draw circles
    # Check mouse pressed & current mouse pos
    if not score_screen and is_pressed and (mouse_pos[0] > game.width/2 - box_width/2 and mouse_pos[0] < game.width/2 + box_width/2 and mouse_pos[1] > 200 and mouse_pos[1] < 200 + box_height):
        # Check prev mouse pos
        if prev_mouse_pos[0] > game.width/2 - box_width/2 and prev_mouse_pos[0] < game.width/2 + box_width/2 and prev_mouse_pos[1] > 200 and prev_mouse_pos[1] < 200 + box_height:
            # Interpolate for finer resolution
            INTERPOLATION_STEPS = 20
            for i in range(INTERPOLATION_STEPS):
                x = int(prev_mouse_pos[0] + (mouse_pos[0] - prev_mouse_pos[0]) * i / INTERPOLATION_STEPS)
                y = int(prev_mouse_pos[1] + (mouse_pos[1] - prev_mouse_pos[1]) * i / INTERPOLATION_STEPS)
                circles.add((x, y))
            circles.add(mouse_pos)
    for circle in circles:
        pygame.draw.circle(screen, '#444444', circle, 10)

    # Handle pygame events
    for event in pygame.event.get():

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_pressed = True

            if not score_screen:
                # Clear button
                if mouse_state == 1:
                    circles = set()
                
                # Submit button
                elif mouse_state == 2:
                    detected_words = get_words_in_box(game)
                    if len(detected_words) > 0:
                        _, detected_word, confidence = detected_words[0]
                        # detected_word = 'whalef'
                        # confidence = 0.63
                        game.prev_score = similarity_words(detected_word, game.goal_word)
                        game.score += game.prev_score
                    else:
                        detected_word = ''
                        game.prev_score = 0
                    if game.prev_score > 50:
                        game.streak += 1
                        if game.streak == 2:
                            game.difficulty = min(5, game.difficulty + 1)
                            game.streak = 0
                    else:
                        game.streak -= 1
                        if game.streak == -2:
                            game.difficulty = max(1, game.difficulty - 1)
                            game.streak = 0

                    update_mistakes(game, game.goal_word, detected_word)
                    score_screen = True

            else:
                # Menu button
                if mouse_state == 1:
                    game.state = 0
                    score_screen = False
                    circles = set()
                    is_pressed = False
                # Next button
                elif mouse_state == 2:
                    score_screen = False
                    circles = set()
                    goal_word = run_generation(game)
                    game.goal_word = goal_word
            
        # Mouse release
        elif event.type == pygame.MOUSEBUTTONUP:
            is_pressed = False

        elif event.type == pygame.QUIT:
            return True
    
    # Update prev mouse state
    prev_mouse_pos = mouse_pos
    prev_mouse_state = mouse_state
        

def get_mouse_state(pos):
    
    # Check if mouse is within clear button image
    if pos[0] > 150 and pos[0] < 390 and pos[1] > 527.5 and pos[1] < 572.5:
        return 1
    
    # Check if mouse is within submit button image
    elif pos[0] > 410 and pos[0] < 650 and pos[1] > 527.5 and pos[1] < 572.5:
        return 2
    
    else:
        return 0
    

def get_words_in_box(game):
        # Get pixel array from white drawing box
        w = 600
        h = 300
        area = pygame.Rect(game.width / 2 - w / 2, 200, w, h)
        sub_surface = game.screen.subsurface(area)
        pixel_data = pygame.surfarray.array3d(sub_surface)
        pixel_data = pixel_data.swapaxes(0, 1)

        # Retrieve text using OCR
        global reader
        result = reader.readtext(pixel_data)
        
        return result