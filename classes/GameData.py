import pygame

class GameData:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.dt = None
        

    def update(self):

        pygame.display.flip()

        self.dt = self.clock.tick(60) / 1000

        # Check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True