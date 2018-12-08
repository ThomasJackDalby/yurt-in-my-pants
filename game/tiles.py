import random
import math
from spatial.vector2d import Vector2D

class TileType:
    def __init__(self, name, isSolid, blocksLight):
        self.name = name
        self.isSolid = isSolid
        self.blocksLight = blocksLight

class Tile:
    def __init__(self, position, type):
        self.position = position
        self.type = type
        self.isDiscovered = False
        self.isVisible = False

FLOOR = TileType("Floor", False, False)
WALL = TileType("Wall", True, True)
ICE = TileType("Ice", False, False)
UNKNOWN = TileType("UNKNOWN", False, False)