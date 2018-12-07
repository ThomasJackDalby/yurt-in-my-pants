
from game.map import Map
from game.player import Player
import console

class Game:

    def __init__(self):
        self.map = Map(100, 100)
        self.player = Player(5, 5)

    def MovePlayer(self, movement):
        target = (self.player.x, self.player.y) + movement 
        tile = self.map.GetTile(target[0], target[1])

        if tile.type.isSolid:
            console.Write("Cannot move to {} {}".format(tile.x, tile.y))
        else:
            self.player.x += movement[0]
            self.player.y += movement[1]