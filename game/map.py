from game.tile import Tile
from game.tile import TILE_TYPES
import random
from PIL import Image

CHUNK_SIZE = 20

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

class MapChunk:

    def __init__(self):


def loadMapChunks():
    im = Image.open('map_tiles.bmp') # Can be many different formats.
    pix = im.load()

    chunks_wide = im.size.width / CHUNK_SIZE
    chunks_high = im.size.height / CHUNK_SIZE

    for cx in range(0, chunks_wide):
        for cy in range(0, chunks_wide):

            for x in range(0, CHUNK_SIZE):
                for y in range(0, CHUNK_SIZE):
                    v = pix[cx * CHUNK_SIZE + x, cy * CHUNK_SIZE + y]
                

def getType(rgb):
    if v is 0:
        TILE_TYPES[0]

    print pix[x,y]  