import pygame

global circles
circles = set()

global is_pressed
is_pressed = False

global prev_mouse_pos
prev_mouse_pos = None

def run_play(game):

    # Register global variables
    global circles
    global is_pressed
    global prev_mouse_pos

    screen = game.screen
    screen.fill('pink')

    mouse_pos = pygame.mouse.get_pos()

    # Draw text
    instruction_text = game.fonts['pt24'].render('Draw the word: whale', True, 'black')
    instruction_text_rect = instruction_text.get_rect(center=(game.width/2, 50))
    screen.blit(instruction_text, instruction_text_rect)

    # Draw box
    box_width = 600
    box_height = 300
    screen.fill('white', (game.width/2 - box_width/2, 200, box_width, box_height))

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
        pygame.draw.circle(screen, 'black', circle, 4)
        
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            is_pressed = True

        elif event.type == pygame.MOUSEBUTTONUP:
            is_pressed = False

        elif event.type == pygame.QUIT:
            return True
    
    # Update prev mouse state
    prev_mouse_pos = mouse_pos
        