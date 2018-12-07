from game.tile import Tile
from game.tile import TILE_TYPES
import random

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [Tile(x, y, random.choice(TILE_TYPES)) for y in range(0, height) for x in range(0, width)]

    def GetTile(self, x, y):
        index = self.getIndex(x, y)
        return self.tiles[index]

    def getIndex(self, x, y):
        return x + y * self.width