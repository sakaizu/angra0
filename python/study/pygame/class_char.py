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
        self.speed = 4
        self.currentspeed = 1
        self.ismoving = False
        self.accel =[0,0] #accelation speed
        self.vel = [0,0]
        self.reserve_movement = [0,0]
        self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

    def movement_accel(self):
        if self.ismoving:
            self.currentspeed += 0.05
            if self.currentspeed > 1:
                self.currentspeed = 1
        else:
            self.currentspeed -= 0.25
            if self.currentspeed < 0:
                self.currentspeed = 0

    def velocity(self):
        self.accel[1] += 1
        self.vel[0] += self.accel[0]
        self.vel[1] += self.accel[1]

        if self.vel[1] > 5:
            self.vel[1] = 5
        elif self.vel[1] < -5:
            self.vel[1] = -5

        self.accel = [0, 0]


    def move(self):
        # self.movement_accel()

        # self.final_movement[0] = (self.movement[0] * self.speed)* self.currentspeed + self.vel[0]
        # self.final_movement[1] = (self.movement[1] * self.speed)* self.currentspeed + self.vel[1]

        self.x += self.reserve_movement[0]
        self.y += self.reserve_movement[1]

        # self.x += (self.movement[0] * self.speed)* self.currentspeed + self.vel[0]
        # self.y += (self.movement[1] * self.speed)* self.currentspeed + self.vel[1]

        self.rect.x = self.x
        self.rect.y = self.y


    def movecheck(self, rectarray):
        collision_types = {'top' : False, 'down' : False, 'left' : False, 'right' : False}

        self.movement_accel()
        self.velocity()

        self.reserve_movement[0] = (self.movement[0] * self.speed)* self.currentspeed + self.vel[0]
        self.reserve_movement[1] = (self.movement[1] * self.speed)* self.currentspeed + self.vel[1]

        self.rect.x += self.reserve_movement[0]
        hitlist = self.checkcollide(rectarray)[0]
        for hit_rect in hitlist:
            if self.reserve_movement[0] > 0:
                self.reserve_movement[0] = 0
                #self.rect.right = tile.left
                self.x = hit_rect.left - self.img.get_width()
                collision_types['right'] = True
            elif self.reserve_movement[0] < 0:
                self.reserve_movement[0] = 0
                #self.rect.left = tile.right
                self.x = hit_rect.right
                collision_types['left'] = True

        self.rect.x = self.x #restore rect collision test

        self.rect.y += self.reserve_movement[1]
        hitlist = self.checkcollide(rectarray)[0]
        for hit_rect in hitlist:
            if self.reserve_movement[1] > 0:
                self.reserve_movement[1] = 0
                #self.rect.bottom = tile.top
                self.y = hit_rect.top - self.img.get_height()
                collision_types['down'] = True
            if self.reserve_movement[1] < 0:
                self.reserve_movement[1] = 0
                #self.rect.top = tile.bottom
                self.y = hit_rect.bottom
                collision_types['top'] = True

        self.rect.y = self.y #restore rect collision test        

        return collision_types

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))

    def update(self):
        self.move()
        self.draw()


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
        return hitlist, hit
        
