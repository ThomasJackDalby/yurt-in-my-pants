import pygame

pygame.init()

MAX_MESSAGES = 10
FONT_SIZE = 20
FONT = pygame.font.SysFont('Papyrus', FONT_SIZE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class HudView:

    def __init__(self, parentSurface, game, screenPosition, screenSize):
        self.parentSurface = parentSurface
        self.game = game
        self.surface = pygame.Surface((screenSize.x, screenSize.y))
        self.screenPosition = screenPosition
        self.screenSize = screenSize

    def Render(self):
        self.surface.fill(BLACK)
        pygame.draw.rect(self.surface, WHITE, (0, 0, self.screenSize.x, self.screenSize.y), 5)
        self.surface.blit(FONT.render("Health", True, WHITE), (10, 10))
        self.surface.blit(FONT.render("FPS: {}".format(int(self.clock.get_fps())), True, WHITE), (10, 30))


        self.parentSurface.blit(self.surface, self.screenPosition.toTuple())
