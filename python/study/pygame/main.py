import pygame, sys
import sys
import os
from pygame.locals import *
import images
import class_char

datapath = os.path.join(os.getcwd(), "data")

clock = pygame.time.Clock()

pygame.init()

WINDOW_SIZE = (400, 400)
screen = pygame.display.set_mode(WINDOW_SIZE, 0 ,32) # set size
display = pygame.Surface((100, 100))

#Image Load
#player_image = pygame.image.load(os.path.join(datapath, "player_02.png"))
player_image = images.player_image
'''
class Char:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = pygame.Rect(self.x,self.y,player_image.get_width(), player_image.get_height())
        allrect.append(self.rect)

    def move(self, x, y):
        self.x += x * self.speed
        self.y += y * self.speed
    def draw(self):
        screen.blit(player_image, (self.x, self.y))
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.draw()
    def create(self):
        f = open(os.path.join(datapath, "test.txt"), 'w')
        f.close()

    def checkcollide(self, rect):
        return self.rect.colliderect(rect)
'''
allrect = []

p1 = class_char.MyChar(10, 10, img = player_image, screen = display)
test_rect = pygame.Rect(100, 10, 50, 50)

allrect.append(test_rect)
allrect.append(p1.rect)

print(allrect)


#Game Loop
while True:
    display.fill((10,10,10))
    display.blit(images.bg_image, (0,0))

    for rect in allrect:
        pygame.draw.rect(display, (255,0,0), rect, 1)
    
    p1.update()
    
    if p1.checkcollide(test_rect):
        print("collide! - ", str(p1.x), str(p1.y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(30)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if p1.x > 0:
            p1.move(-1,0)
    if keys[pygame.K_RIGHT]:
        if p1.x < WINDOW_SIZE[0]/2 - player_image.get_width():
            p1.move(1,0)
    if keys[pygame.K_UP]:
        if p1.y > 0:
            p1.move(0,-1)
    if keys[pygame.K_DOWN]:
        p1.move(0,1)
    if keys[pygame.K_SPACE]:
        p1.create()


