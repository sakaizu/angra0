import pygame
import sys
import os

class MyChar:
    def __init__(self, x, y, img, screen):
        self.x = x
        self.y = y
        self.img = img
        self.screen = screen
        self.movement = [0,0]
        self.speed = 2
        self.currentspeed = 1
        self.ismoving = False
        self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

    def moveaccel(self):
        if self.ismoving:
            self.currentspeed += 0.05
            if self.currentspeed > 1:
                self.currentspeed = 1
        else:
            self.currentspeed -= 0.25
            if self.currentspeed < 0:
                self.currentspeed = 0

    def move(self):

        self.moveaccel()
        self.x += self.movement[0] * self.speed * self.currentspeed
        self.y += self.movement[1] * self.speed * self.currentspeed

        self.rect.x = self.x
        self.rect.y = self.y

    def movecheck(self, rectarray):
        collision_types = {'top' : False, 'down' : False, 'left' : False, 'right' : False}

        self.rect.x += self.movement[0] *self.speed
        hitlist = self.checkcollide(rectarray)
        for tile in hitlist:
            if self.movement[0] > 0:
                self.movement[0] = 0
                #self.rect.right = tile.left
                #self.x = tile.left - self.img.get_width() - 1
                collision_types['right'] = True
            elif self.movement[0] < 0:
                self.movement[0] = 0
                #self.rect.left = tile.right
                #self.x = tile.right + 1
                collision_types['left'] = True

        self.rect.x = self.x #restore rect collision test

        self.rect.y += self.movement[1] * self.speed
        hitlist = self.checkcollide(rectarray)
        for tile in hitlist:
            if self.movement[1] > 0:
                self.movement[1] = 0
                #self.rect.bottom = tile.top
                #self.y = tile.top
                collision_types['down'] = True
            if self.movement[1] < 0:
                self.movement[1] = 0
                #self.rect.top = tile.bottom
                #self.y = tile.bottom
                collision_types['top'] = True

        self.rect.y = self.y #restore rect collision test        

        return collision_types

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))

    def update(self):
        self.move()
        self.draw()

    def create(self):
        pass

    def checkcollide(self, rectarray):
        colcount = 0
        hitlist = []
        hit = False
        for rect in rectarray:
            if self.rect.colliderect(rect):
                if rect == self.rect:
                    pass #Ignore Myself
                else:
                    colcount += 1
                    hitlist.append(rect)
        if colcount > 0:
            hit = True
        return hitlist
