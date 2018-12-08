from game.map import Map
from game.player import Player
import console
import game.map
import random

class Game:

    def __init__(self):
        self.map = game.map.createRandomMap(4, 4)

        while True:
            tile = random.choice(self.map.tiles)
            if not tile.type.isSolid:
                self.player = Player(tile.position)
                break
        
        console.Write("Player starting at ({}, {})".format(self.player.position.x, self.player.position.y))

    def MovePlayer(self, movement):
        target = self.player.position + movement 
        if not self.map.limits.contains(target):
            return

        tile = self.map.getTile(target.x, target.y)
        if tile.type.isSolid:
            console.Write("Cannot move to {} {}".format(tile.position.x, tile.position.y))
        else:
            self.player.position += movement