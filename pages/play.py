import pygame
from easyocr import Reader
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

def run_play(game):

    # Register global variables
    global circles
    global is_pressed
    global prev_mouse_pos
    global prev_mouse_state

    screen = game.screen
    screen.fill('pink')
    mouse_pos = pygame.mouse.get_pos()
    mouse_state = get_mouse_state(mouse_pos)

    # Draw text
    instruction_text = game.fonts['pt24'].render('Draw the word: whale', True, 'black')
    instruction_text_rect = instruction_text.get_rect(center=(game.width/2, 50))
    screen.blit(instruction_text, instruction_text_rect)

    # Draw box
    box_width = 600
    box_height = 300
    screen.fill('white', (game.width/2 - box_width/2, 200, box_width, box_height))

    # Draw submit button
    button_width = 100
    button_height = 50
    button_color = '#EECCFF' if mouse_state == 1 else '#FFCCFF'
    button_text_color = 'black'
    screen.fill(button_color, (game.width/2 - button_width/2, 550, button_width, button_height))
    button_text = game.fonts['pt24'].render('Submit', True, button_text_color)
    button_text_rect = button_text.get_rect(center=(game.width/2, 550 + button_height/2))
    screen.blit(button_text, button_text_rect)

    # Handle mouse cursor
    if prev_mouse_state == 0 and mouse_state == 1:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif prev_mouse_state == 1 and mouse_state == 0:
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

            # Check if mouse is within submit button
            if mouse_state == 1:
                # Get grayscale pixel array from white drawing box
                detected_words = get_words_in_box(game)
                print(detected_words)
            
        # Mouse release
        elif event.type == pygame.MOUSEBUTTONUP:
            is_pressed = False

        elif event.type == pygame.QUIT:
            return True
    
    # Update prev mouse state
    prev_mouse_pos = mouse_pos
    prev_mouse_state = mouse_state
        

def get_mouse_state(pos):
    
    if pos[0] > 350 and pos[0] < 450 and pos[1] > 550 and pos[1] < 600:
        return 1
    
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