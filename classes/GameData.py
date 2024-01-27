import pygame
from collections import Counter
class GameData:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.dt = None

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.fonts = {
            'title': pygame.font.Font(None, 48),
            'pt24': pygame.font.Font(None, 24),
            'pt35': pygame.font.Font(None, 35),
            'pt20': pygame.font.Font(None, 20)
        }
        self.images = {
            'bg_settings': pygame.image.load('images/bg_settings.jpg'),
            'bg_hard': pygame.image.load('images/bg_hard.png'),
            'bg_medium': pygame.image.load('images/bg_medium.png'),
            'text_settings': pygame.image.load('images/text_settings.png'),
            'button_menu': pygame.image.load('images/button_menu.png'),
            'button_back': pygame.image.load('images/button_back.png'),
            'button_harder': pygame.image.load('images/button_harder.png'),
            'button_easier': pygame.image.load('images/button_easier.png'),
            'button_submit': pygame.image.load('images/button_submit.png'),
            'button_clear': pygame.image.load('images/button_clear.png'),
            'button_next': pygame.image.load('images/button_next.png'),
            'green_shell': pygame.image.load('images/green_shell.png')
        }
        
        #global variables
        #difficulty level up to 5
        self.score = 0
        self.state = 0
        self.difficulty = 3
        self.weaknesses = []
        self.strengths = []
        self.goal_word = 'whale'
        self.streak = 0


        #Track types of mistakes the user is more likely to make
        #Adjust word and difficulty depending on mistakes
        self.mistakes = Counter()


    def get_state(self):
        return self.state
    
    def get_score(self):
        return self.score

    def get_difficulty(self):
        return self.difficulty

    def draw_fps(self):
        fps = self.clock.get_fps()
        fps_text = self.fonts['pt24'].render(f'FPS: {fps:.2f}', True, 'black')
        fps_text_rect = fps_text.get_rect(topright=(self.width - 10, 10))
        self.screen.blit(fps_text, fps_text_rect)

    def update(self):

        self.draw_fps()
        pygame.display.flip()
        self.dt = self.clock.tick(60) / 1000
    