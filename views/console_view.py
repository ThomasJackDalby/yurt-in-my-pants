import pygame
import console

pygame.init()

MAX_MESSAGES = 10
FONT_SIZE = 20
FONT = pygame.font.SysFont('Papyrus', FONT_SIZE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class ConsoleView:

    def __init__(self, parentSurface, screenPosition, screenSize):
        self.parentSurface = parentSurface
        self.screenPosition = screenPosition
        self.screenSize = screenSize
        self.surface = pygame.Surface((screenSize.x, screenSize.y))

    def Render(self):
        self.surface.fill((0, 0, 0))
        pygame.draw.rect(self.surface, WHITE, (0, 0, self.screenSize.x, self.screenSize.y), 5)
        for i in range(0, len(console.messages)):
            message = console.messages[i]
            textsurface = FONT.render(message, True, WHITE)
            self.surface.blit(textsurface, (10, i*20+10))
        self.parentSurface.blit(self.surface, self.screenPosition.toTuple())