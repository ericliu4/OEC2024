import pygame

from misc.generation import run_generation

global timer
timer = 0

def run_instructions(game):

    global timer

    screen = game.screen
    screen.fill('black')

    instruction_text = [
        'Here are your rules...',
        'Draw the word that appears on the screen',
        'You will get a score up to 100',
        'The difficulty and word selection will adapt to your skill',
        'keep it to one line',
        'Good luck!!',
        '(hit space to continue)'  
    ]

    timer += 1
    adjusted_timer = timer // 2

    for i, blurb in enumerate(instruction_text):
        if adjusted_timer > 0:
            blurb = blurb[:adjusted_timer]
            text = game.fonts['pt35'].render(blurb, True, 'white')
            text_rect = text.get_rect(center=(game.width/2, 150 + i * 40))
            screen.blit(text, text_rect)
            adjusted_timer -= len(blurb)


    # Handle pygame events
    for event in pygame.event.get():

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_pressed = True
            
        # Check if space key is pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.state = 2
                goal_word = run_generation(game)
                game.goal_word = goal_word