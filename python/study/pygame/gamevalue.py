import pygame, sys
import os
import textures
import class_char
import class_tile
import extractImage
import objectlist as ol

# Main Values ---------------------------------------------


datapath = os.path.join(os.getcwd(), "data")
WINDOW_SIZE = (400, 400)
screen = pygame.display.set_mode(WINDOW_SIZE, 0 ,32) # set size
display = pygame.Surface((100, 100))
TickTime = 30
scroll = [0, 0]



class gamestate():
    def __init__(self):
        self.state = 'menu'
        self.init_setup = True

    def changestate(self, state):
        self.state = state
        self.init_setup = True #reset to Do_once in loop
        self.cleanup()
        print(ol.obj_chars, ol.obj_tiles)

    def setgamestate(self):
        if self.state == 'playstate':
            self.playstage()
        if self.state == 'menu':
            self.menu()

    def cleanup(self):
        print("cleanup object")
        ol.clean()




    def menu(self):
        if self.init_setup:
            print("press any key!")
            self.init_setup = False


        display.fill((200, 10, 10))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.changestate('playstate')






    def playstage(self):
        if self.init_setup:
# GetTilePixelData
            tileData = extractImage.getdatafrompixel(os.path.join(datapath, 'BG_test_01.png'))

# Spawn Tiles
            for y in range(10):
                for x in range(10):
                    if tileData[y][x][0] == 0:
                        ol.obj_tiles.add(class_tile.tile(x*10, y*10, textures.bg_moss_01, True, display))
                    elif tileData[y][x][0] == 255:
                        ol.obj_tiles.add(class_tile.tile(x*10, y*10, textures.bg_moss_02, False, display))

# Create Characters
            p1 = class_char.player(10, 10, img = textures.player_image_r, screen = display)
            m1 = class_char.monster(70, 10, img = textures.monster_image_1, screen = display)
            m2 = class_char.monster(65, 10, img = textures.monster_image_1, screen = display)
            m3 = class_char.monster(60, 10, img = textures.monster_image_1, screen = display)

            scroll[0] = 0
            self.init_setup = False

# Scroll Screen By Character Pos
        scroll[0] += (ol.player.rect.x - scroll[0] - 35)/10


# TileMap Update from tile array
        for i in ol.obj_tiles.sprites():
            i.update()

# debug draw all rect
        for tile in ol.obj_tiles.sprites():
            if tile.isblock:
                pygame.draw.rect(display, (255,0,0), tile.rect, 1)
        for char in ol.obj_chars.sprites():
            pygame.draw.rect(display, (0,0,255), char.rect, 1)

# Characters tick update
# moveCollisioncheck(previus Movement) -> Move -> Reset
        for char in ol.obj_chars.sprites():
            if char.isplayer:
                char.movecheck(ol.obj_tiles)
                char.update()
                char.movement = [0,0]

            else: #Monsters Update
                if char.movecheck(ol.obj_tiles)["left"]:
                    char.movement[0] = 1
                elif char.movecheck(ol.obj_tiles)["right"]:
                    char.movement[0] = -1

                char.update()





# event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ol.player.jump()

                if event.key == pygame.K_ESCAPE:
                    self.changestate('menu')


# Key binding
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if ol.player.x > 0 and ol.player.isdead == False:
                ol.player.movement[0] = -1
                ol.player.img = pygame.transform.flip((textures.player_image_r), True, False)
        if keys[pygame.K_RIGHT]:
            if ol.player.x < WINDOW_SIZE[0]/2 - ol.player.img.get_width() and ol.player.isdead == False:
                ol.player.movement[0] = 1
                ol.player.img =textures.player_image_r
        if keys[pygame.K_UP]:
            pass
        if keys[pygame.K_DOWN]:
            pass
        if keys[pygame.K_SPACE]:
            pass

        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            ol.player.ismoving = True
        else:
            ol.player.ismoving = False

