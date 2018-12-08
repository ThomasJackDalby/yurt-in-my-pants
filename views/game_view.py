import pygame
import game.tiles
from spatial.vector2d import Vector2D
import operator

TILE_SIZE = 20
FLOOR_COLOUR = (110, 110, 110)
WALL_COLOUR = (60, 60, 60)
ICE_COLOUR = (0, 0, 255)
UNKNOWN_COLOUR = (255, 0, 0)
PLAYER_COLOUR = (0, 0, 255)

BLACK = (0, 0, 0)
DARKEN = (0.3, 0.3, 0.3)

class GameView:

    def __init__(self, parentSurface, game, screenPosition, screenSize):
        self.parentSurface = parentSurface
        self.game = game
        self.surface = pygame.Surface((screenSize.x, screenSize.y))
        self.screenPosition = screenPosition
        self.screenSize = screenSize
        self.screenCentre = Vector2D(0, 0)

    def Render(self):
        self.surface.fill(BLACK)
        self.renderMap()
        self.renderPlayer()
        self.parentSurface.blit(self.surface, self.screenPosition.toTuple())

    def renderPlayer(self):
        pos = self.transformToScreen(self.game.player.position)
        rect = (pos.x*TILE_SIZE, pos.y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(self.surface, PLAYER_COLOUR, rect)

    def renderMap(self):
        for y in range(self.game.map.height):
            for x in range(self.game.map.width):
                self.renderTile(x, y)

    def renderTile(self, x, y):
        tile = self.game.map.getTile(x, y)
        if tile.isVisible:
            fill = getTileFill(tile.type)
        elif tile.isDiscovered:
            fill = getTileFill(tile.type)
            fill = tuple(map(operator.mul, fill, DARKEN))
        else:
            fill = BLACK
        pos = self.transformToScreen(tile.position)
        rect = (pos.x*TILE_SIZE, pos.y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(self.surface, fill, rect)

    def transformToScreen(self, gamePosition):
        offset = self.screenCentre - self.screenSize / (TILE_SIZE * 2)
        return gamePosition - offset

def getTileFill(tileType):
    if tileType == game.tiles.FLOOR:
        return FLOOR_COLOUR
    elif tileType == game.tiles.WALL:
        return WALL_COLOUR
    elif tileType == game.tiles.ICE:
        return ICE_COLOUR
    else:
        return UNKNOWN_COLOUR