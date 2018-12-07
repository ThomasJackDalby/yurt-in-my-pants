import pygame
from game.tile import TILE_TYPES 

TILE_SIZE = 20
FLOOR_COLOUR = (19, 173, 31)
WALL_COLOUR = (158, 62, 10)

class GameView:

    def __init__(self, parentSurface, game, position):
        self.parentSurface = parentSurface
        self.position = position
        self.game = game
        self.surface = pygame.Surface((position[2], position[3]))

    def Render(self):
        self.renderMap()
        self.renderPlayer()
        self.parentSurface.blit(self.surface, self.position)

    def renderPlayer(self):
        pygame.draw.rect(self.surface, (0, 0, 255), (self.game.player.x*TILE_SIZE, self.game.player.y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def renderMap(self):
        for y in range(self.game.map.height):
            for x in range(self.game.map.width):
                tile = self.game.map.GetTile(x, y)
                if tile.type == TILE_TYPES[0]:
                    fill = GRASS_COLOUR
                else:
                    fill = WALL_COLOUR
                pygame.draw.rect(self.surface, fill, (tile.x*TILE_SIZE, tile.y*TILE_SIZE, TILE_SIZE, TILE_SIZE))