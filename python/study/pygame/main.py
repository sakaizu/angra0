import pygame, sys
import sys
import os
from pygame.locals import *
import textures
import class_char
import class_tile
import extractImage


datapath = os.path.join(os.getcwd(), "data")

clock = pygame.time.Clock()

pygame.init()

#Display setting
WINDOW_SIZE = (400, 400)
screen = pygame.display.set_mode(WINDOW_SIZE, 0 ,32) # set size
display = pygame.Surface((100, 100))

#Image Load
#player_image = pygame.image.load(os.path.join(datapath, "player_02.png"))
player_image = textures.player_image_r

allrect = []
tiles = []

p1 = class_char.MyChar(10, 10, img = textures.player_image_r, screen = display)

allrect.append(p1.rect)


#GetTilePixelData
tileData = extractImage.getdatafrompixel(os.path.join(datapath, 'BG_test_01.png'))

#Spawn Tiles
for y in range(10):
    for x in range(10):
        if tileData[y][x][0] ==0:
            tiles.append(class_tile.tile(x*10, y*10, textures.bg_moss_01, True, display))
        else:
            tiles.append(class_tile.tile(x*10, y*10, textures.bg_moss_02, False, display))
for tile in tiles:
    tile.appendrect(allrect)




#Game Loop
while True:
    display.fill((10,10,10))
    display.blit(textures.bg_moss_01, (0,0))

    pygame.display.update()
    clock.tick(30)


#TileMap Update from tile array
    for i in tiles:
        i.update()

    for rect in allrect:
        pygame.draw.rect(display, (255,0,0), rect, 1)


# player tick update
# moveCollisioncheck(previus Movement) -> Move -> Reset
    p1.movecheck(allrect)
    print(p1.vel)
    p1.update()

# reset movement
    p1.movement = [0,0]


#set display to screen res
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


# Key binding
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if p1.x > 0:
            p1.movement[0] = -1
            p1.img = textures.player_image_l
    if keys[pygame.K_RIGHT]:
        if p1.x < WINDOW_SIZE[0]/2 - player_image.get_width():
            p1.movement[0] = 1
            p1.img = textures.player_image_r
    if keys[pygame.K_UP]:
        if p1.y > 0:
            p1.movement[1] = -1
    if keys[pygame.K_DOWN]:
        if p1.y + p1.img.get_height() <= WINDOW_SIZE[1]/2:
            p1.movement[1] = 1

    if keys[pygame.K_SPACE]:
        p1.accel[1] -= 3
        pass

    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
        p1.ismoving = True
    else:
        p1.ismoving = False

    if p1.checkcollide(allrect)[1]:
        print(p1.checkcollide(allrect))
        #print(p1.movecheck(allrect))





