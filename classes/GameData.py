import pygame

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
            'pt24': pygame.font.Font(None, 24)
        }
        
        #glolal variables
        self.score = 0
        self.state = 0

    def get_state(self):
        return self.state


    def update(self):

        pygame.display.flip()

        self.dt = self.clock.tick(60) / 1000

        # Check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
    
    