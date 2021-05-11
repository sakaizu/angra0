import pygame, sys
import os
from pygame.locals import *
import textures
import class_char
import class_tile
import extractImage
import objectlist as ol

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



# GetTilePixelData
tileData = extractImage.getdatafrompixel(os.path.join(datapath, 'BG_test_01.png'))

# Spawn Tiles
for y in range(10):
    for x in range(10):
        if tileData[y][x][0] ==0:
            ol.tiles.append(class_tile.tile(x*10, y*10, textures.bg_moss_01, True, display))
        else:
            ol.tiles.append(class_tile.tile(x*10, y*10, textures.bg_moss_02, False, display))

# Create Characters
p1 = class_char.player(10, 10, img = textures.player_image_r, screen = display)
m1 = class_char.monster(70, 10, img = textures.monster_image_1, screen = display)
m2 = class_char.monster(65, 10, img = textures.monster_image_1, screen = display)
m3 = class_char.monster(60, 10, img = textures.monster_image_1, screen = display)

p1.isplayer = True


# Save external list





# Game Loop------------------------------------------------------------

while True:
    display.fill((10,10,10))
    display.blit(textures.bg_moss_01, (0,0))

    pygame.display.update()
    clock.tick(30)


# TileMap Update from tile array
    for i in ol.tiles:
        i.update()

# debug draw all rect
    for tile in ol.tiles:
        if tile.isblock:
            pygame.draw.rect(display, (255,0,0), tile.rect, 1)
    for char in ol.chars:
        pygame.draw.rect(display, (0,0,255), char.rect, 1)


# Characters tick update
# moveCollisioncheck(previus Movement) -> Move -> Reset
    for char in ol.chars:
        if char.isplayer:
           char.movecheck(ol.tiles)
           char.update()
           char.movement = [0,0]
        else:
            if char.movecheck(ol.tiles)["left"]:
                char.movement[0] = 1
            elif char.movecheck(ol.tiles)["right"]:
                char.movement[0] = -1
            char.update()



    if p1.charcollision_check()[0] == "attack":
        p1.vel[1] = -7
        for mon in p1.charcollision_check()[1]:
            #ol.chars.remove(mon)
            mon.dead()
            break


    #print(ol.obj_chars.sprites().isplayer)
# !!!!!!!!!!! Groups !!!!!!!!!!!!!!
    print(ol.obj_chars)
    print(ol.obj_tiles)
    for i in ol.obj_chars.sprites():
        print(i.isplayer)

#set display to screen res
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))

#event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # p1.accel[1] += -7
                p1.vel[1] = -7

            if event.key == pygame.K_ESCAPE:
                pygame.quit()


# Key binding`
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
        pass
        # if p1.y > 0:
        #     p1.movement[1] = -1
    if keys[pygame.K_DOWN]:
        pass
        # if p1.y + p1.img.get_height() <= WINDOW_SIZE[1]/2:
        #     p1.movement[1] = 1

    if keys[pygame.K_SPACE]:
        # p1.accel[1] -= 3
        pass

    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
        p1.ismoving = True
    else:
        p1.ismoving = False





