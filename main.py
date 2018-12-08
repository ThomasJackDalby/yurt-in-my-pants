import pygame
from game.game import Game
from views.game_view import GameView
from views.console_view import ConsoleView
import console
import datetime
from spatial.vector2d import Vector2D

console.Write("Initialising application.")
pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
CONSOLE_HEIGHT = 100
 
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Yurt in my pants')

def game_intro():
    inLoop = True

    while inLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def game_main():
    clock = pygame.time.Clock() 
    console.Write("Entering main game loop.")
    game = Game()
    gameView = GameView(gameDisplay, game, Vector2D(0, 0), Vector2D(DISPLAY_WIDTH, DISPLAY_HEIGHT-CONSOLE_HEIGHT))
    consoleView = ConsoleView(gameDisplay, Vector2D(0, DISPLAY_HEIGHT-CONSOLE_HEIGHT) , Vector2D(DISPLAY_WIDTH, CONSOLE_HEIGHT))

    inLoop = True
    while inLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            game.MovePlayer(Vector2D(-1, 0))
        if keys[pygame.K_RIGHT]:
            game.MovePlayer(Vector2D(1, 0))
        if keys[pygame.K_UP]:
            game.MovePlayer(Vector2D(0, -1))
        if keys[pygame.K_DOWN]:
            game.MovePlayer(Vector2D(0, 1))

        game.map.updateTilesVisibility(game.player.position)


        gameView.screenCentre = game.player.position
        gameView.Render()
        consoleView.Render()
        pygame.display.flip()

        clock.tick(60)

# game_intro()
game_main()