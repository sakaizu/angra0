import pygame
import os
import random
import math
from pygame.math import Vector2

pygame.font.init()
pygame.init()

screen_width, screen_height =  500, 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("RotateTest")

# background image
bgimage = pygame.transform.scale(pygame.image.load(os.path.join('python/pygame', 'asset/bg.png')), (screen_width, screen_height))

# Player image
pcimage = pygame.image.load(os.path.join('python/pygame', 'asset/pc.png'))
pc_size = pcimage.get_rect().size
pc_width = pc_size[0]
pc_height = pc_size[1]

# enemy image
enemyimage = pygame.image.load(os.path.join('python/pygame', 'asset/enemy.png'))


# Initial PC position
pc_pos_x = screen_width / 2 - (pc_width/2)
pc_pos_y = screen_height - pc_height


# Global variable
running = True
FPS = 60.0
DeltaTime = 1/FPS
enemycooltime = 0
Clock = pygame.time.Clock()
font_main = pygame.font.SysFont("comicsans", 50)

projectileList = []
charList = []


class Char:

    FireRate = 5

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.charimg = None
        self.speed = speed
        self.hp = 100
        self.cool_down_counter = 0
        self.isFoe = False
    
    def draw(self):
        screen.blit(self.charimg, (self.x, self.y))

    def cooldown(self):
        self.cool_down_counter += DeltaTime * self.FireRate
        if self.cool_down_counter >= 1.0:
            self.cool_down_counter = 1.0

    def setcooltime(self):
        self.cool_down_counter = 0

    def update(self):
        self.draw()
        self.cooldown()


class Player(Char):
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed)
        self.charimg = pcimage
        self.mask = pygame.mask.from_surface(self.charimg)


class Enemy(Char):
    VARI_MAP = {
                "1": (enemyimage),
                "2": (enemyimage),
                "3": (enemyimage)
                }
    def __init__(self, x, y, speed, var):
        super().__init__(x, y, speed)
        self.charimg = self.VARI_MAP[var]
        self.mask = pygame.mask.from_surface(self.charimg)
        self.isFoe = True
    
    def move(self):
        self.y += self.speed

    def checkBottomFloor(self):
        if self.y > screen_height:
            pass

    def draw(self):
        rotateTest(self.charimg, self.x, self.y)
        # screen.blit(self.charimg, (self.x, self.y))
            
    def update(self):
        self.draw()
        self.cooldown()





def rotateTest(img, x, y):

    imgcenter = img.get_rect().center
    rotateimg = pygame.transform.rotate(img, pygame.time.get_ticks()/20)
    r = rotateimg.get_rect()

    newpivot = rotateimg.get_rect(center = imgcenter)

    scaleimg = pygame.transform.scale(rotateimg, (100, 100))

    newpivot = scaleimg.get_rect(center = imgcenter)

    r = scaleimg.get_rect()

    # screen.blit(rotateimg, (newpivot[0] + x, newpivot[1] + y))
    screen.blit(scaleimg, (x, y))
    # pygame.draw.circle(screen, (0, 255, 0), (newpivot[0]+ x,  newpivot[1]+ y), 7, 0)
    pygame.draw.circle(screen, (0, 255, 0), (x, y), 7, 0)


    pygame.draw.line(screen, (255,255,0), (x, y), (x, y + r.height), 5)
    pygame.draw.line(screen, (255,255,0), (x + r.width, y), (x + r.width, y + r.height), 5)
    pygame.draw.line(screen, (255,255,0), (x, y), (x + r.width, y), 5)
    pygame.draw.line(screen, (255,255,0), (x, y + r.height), (x + r.width, y + r.height), 5)

# create player char
PlayerChar = Player(pc_pos_x, pc_pos_y, 10)
charList.append(PlayerChar)



def updateDraw(): #Draw screen every tick

    screen.blit(bgimage, (0, 0))

    rotateTest(pcimage, bgimage.get_rect().centerx , bgimage.get_rect().centery)

    for char in charList:
        if char.isFoe:  # enemychar udpate
            char.move()
            char.update()
        else:
            char.update() # playerchar update



# draw ui
    HP_label = font_main.render(f"HP: {PlayerChar.hp}", 1, (255,0,0))
    Pos_label = font_main.render(f"data01: {len(projectileList)}", 1, (0, 255, 0))
    screen.blit(HP_label, (10, 10))
    screen.blit(Pos_label, (10, 50))

# update screen
    pygame.display.update()



while running:
    Clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("game end")


    updateDraw()



pygame.quit()