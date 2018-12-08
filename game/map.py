from game.tiles import Tile
from PIL import Image
import game.tiles
import random
import math
from spatial.vector2d import Vector2D
from spatial.limits2d import Limits2D
import game.ray_tracing as ray_tracing

CHUNK_SIZE = 20

class Map:

    def __init__(self, width, height):
        self.limits = Limits2D(Vector2D(0, 0), Vector2D(width, height))
        self.width = width
        self.height = height
        self.tiles = [Tile(Vector2D(x, y), game.tiles.UNKNOWN)
                      for y in range(0, height) for x in range(0, width)]
        self.flag = 0

    def getTile(self, x, y):
        index = self.getIndex(x, y)
        return self.tiles[index]

    def getIndex(self, x, y):
        return x + y * self.width

    def checkTileAllowsLight(self, position):
        if self.limits.contains(position):
            tile = self.getTile(position.x, position.y)
            return not tile.type.blocksLight
        else:
            return False

    def updateTilesVisibility(self, position):
        visibileTiles = ray_tracing.getVisiblePoints(position, self.checkTileAllowsLight)

        for i in range(0, len(self.tiles)):
            self.tiles[i].isVisible = False

        for tilePosition in visibileTiles:
            if self.limits.contains(tilePosition):
                tile = self.getTile(tilePosition.x, tilePosition.y)
                tile.isVisible = True
                tile.isDiscovered = True

class MapChunk:

    def __init__(self, pixels, cx, cy):
        self.tiles = [getType(pixels[cx * CHUNK_SIZE + x, cy * CHUNK_SIZE + y])
                      for y in range(0, CHUNK_SIZE) for x in range(0, CHUNK_SIZE)]

    def getTile(self, x, y):
        index = self.getIndex(x, y)
        return self.tiles[index]

    def setTile(self, x, y, tile):
        index = self.getIndex(x, y)
        self.tiles[index] = tile

    def getIndex(self, x, y):
        return x + y * CHUNK_SIZE


def loadMapChunks(filePath):
    print("Loading map chunks from [{}].".format(filePath))
    image = Image.open(filePath)
    pixels = image.load()
    return [MapChunk(pixels, cx, cy) for cx in range(0, math.floor(image.size[0] / CHUNK_SIZE)) for cy in range(0, math.floor(image.size[1] / CHUNK_SIZE))]

def getType(rgb):
    if rgb == (0, 0, 0):
        return game.tiles.WALL
    elif rgb == (255, 255, 255):
        return game.tiles.FLOOR
    else:
        return game.tiles.UNKNOWN

def createRandomMap(chunksWide, chunksHigh):
    print("Creating random map of size ({}, {}).".format(chunksWide, chunksHigh))
    map = Map(chunksWide * CHUNK_SIZE, chunksHigh * CHUNK_SIZE)
    mapChunks = loadMapChunks('map_tiles.bmp')

    print("Populating map with chunks..")
    for cx in range(0, chunksWide):
        for cy in range(0, chunksHigh):
            # Pick a random chunk
            chunk = random.choice(mapChunks)
            for y in range(0, CHUNK_SIZE):
                for x in range(0, CHUNK_SIZE):
                    tileType = chunk.getTile(x, y)
                    tile = map.getTile(cx*CHUNK_SIZE+x, cy*CHUNK_SIZE+y)
                    tile.type = tileType

    return map


