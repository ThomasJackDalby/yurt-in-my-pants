import random
import math

class Tile:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

class TileType:
    def __init__(self, name, isSolid):
        self.name = name
        self.isSolid = isSolid 

TILE_TYPES = [
    TileType("Floor", False),
    TileType("Wall", True),
    TileType("Ice", False),
]