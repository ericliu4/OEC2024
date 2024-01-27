import pygame
# from easyocr import Reader


global circles
circles = set()

global is_pressed
is_pressed = False

global prev_mouse_pos
prev_mouse_pos = None

global prev_mouse_state
prev_mouse_state = 0

global reader
# reader = Reader(['en'])

def run_play(game):

    # Register global variables
    global circles
    global is_pressed
    global prev_mouse_pos
    global prev_mouse_state

    screen = game.screen
    mouse_pos = pygame.mouse.get_pos()
    mouse_state = get_mouse_state(mouse_pos)

    # Draw background as hard image
    screen.blit(game.images['bg_hard'], (0, 0))


    # Draw instruction text
    instruction_text = game.fonts['pt35'].render('WRITE THE WORD BELOW', True, 'white')
    instruction_text_rect = instruction_text.get_rect(center=(game.width/2, 100))
    screen.blit(instruction_text, instruction_text_rect)

    instruction_text_2 = game.fonts['title'].render(game.goal_word, True, 'white')
    instruction_text_2_rect = instruction_text_2.get_rect(center=(game.width/2, 150))
    screen.blit(instruction_text_2, instruction_text_2_rect)

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

    # Draw submit and clear button side by side using images
    submit_button_image = game.images['button_submit']
    submit_button_image_rect = submit_button_image.get_rect(center=(game.width/2 + 130, 550))
    screen.blit(submit_button_image, submit_button_image_rect)
    clear_button_image = game.images['button_clear']
    clear_button_image_rect = clear_button_image.get_rect(center=(game.width/2 - 130, 550))
    screen.blit(clear_button_image, clear_button_image_rect)


    # Handle mouse cursor
    if prev_mouse_state == 0 and mouse_state:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif prev_mouse_state and mouse_state == 0:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Draw circles
    # Check mouse pressed & current mouse pos
    if is_pressed and (mouse_pos[0] > game.width/2 - box_width/2 and mouse_pos[0] < game.width/2 + box_width/2 and mouse_pos[1] > 200 and mouse_pos[1] < 200 + box_height):
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
        pygame.draw.circle(screen, 'black', circle, 3)

    # Handle pygame events
    for event in pygame.event.get():

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_pressed = True

            # Clear button
            if mouse_state == 1:
                circles = set()
            
            # Submit button
            elif mouse_state == 2:
                detected_words = get_words_in_box(game)
                _, detected_word, confidence = detected_words[0]
                print(_, detected_word, confidence)
            
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