import pygame
import console

pygame.init()

MAX_MESSAGES = 10
FONT_SIZE = 20
FONT = pygame.font.SysFont('Papyrus', FONT_SIZE)

class ConsoleView:

    def __init__(self, parentSurface, position):
        self.parentSurface = parentSurface
        self.position = position
        self.surface = pygame.Surface((position[2], position[3]))

    def Render(self):
        self.surface.fill((0, 0, 0))
        for i in range(0, len(console.messages)):
            message = console.messages[i]
            textsurface = FONT.render(message, True, (255, 255, 255))
            self.surface.blit(textsurface, (10, i*20+10))
        self.parentSurface.blit(self.surface, self.position)