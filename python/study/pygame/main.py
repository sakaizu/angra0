import pygame, sys
import os
from pygame.locals import *
import textures
import class_char
import class_tile
import extractImage
import objectlist as ol
import gamevalue

datapath = os.path.join(os.getcwd(), "data")

clock = pygame.time.Clock()

pygame.init()

gamestate = gamevalue.gamestate()

#Display setting
WINDOW_SIZE = gamevalue.WINDOW_SIZE
screen = gamevalue.screen
display = gamevalue.display





# Game Loop------------------------------------------------------------

while True:

    pygame.display.update()
    clock.tick(gamevalue.TickTime)
    
    display.fill((0, 0, 0))

    gamestate.setgamestate()

# set display to screen res and show
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0,0))

