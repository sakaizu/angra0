import pygame
import sys
import os
import mymath as mm
import objectlist as ol

class Char(pygame.sprite.Sprite):
    def __init__(self, x, y, img, screen):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.isplayer = True
        self.img = img
        self.screen = screen
        self.movement = [0,0]
        self.char_speed = 5
        self.currentspeed = 1
        self.ismoving = False
        self.accel =[0,0] #accelation speed
        self.vel = [0,0]
        self.reserve_movement = [0,0]
        self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

        ol.obj_chars.add(self)

    def movement_accel(self):
        if self.ismoving:
            self.currentspeed += 0.05
        else:
            self.currentspeed -= 0.25

        self.currentspeed = mm.clamp(self.currentspeed, 0, 1)

    def gravity(self):
        self.accel[1] += 1

    def calc_Vel(self):
        self.gravity()

        self.vel[0] += self.accel[0]
        self.vel[1] += self.accel[1]

        self.vel[1] = mm.clamp(self.vel[1], -10, 5)

        self.accel = [0, 0]


    def move(self):
        # self.movement_accel()
        self.x += self.reserve_movement[0]
        self.y += self.reserve_movement[1]

        self.rect.x = self.x
        self.rect.y = self.y

    def set_reserve_movement(self):
        if self.isplayer:
            self.movement_accel()
        self.calc_Vel()
        # final movement = (input movement * Char_speed) * currentspeed + velocity
        self.reserve_movement[0] = (self.movement[0] * self.char_speed)* self.currentspeed + self.vel[0]
        self.reserve_movement[1] = (self.movement[1] * self.char_speed)* self.currentspeed + self.vel[1]


    def movecheck(self, tile_array):
        collision_types = {'top' : False, 'down' : False, 'left' : False, 'right' : False}

        self.set_reserve_movement()

        self.rect.x += self.reserve_movement[0]
        hitlist = mm.check_collision(self.rect, tile_array)[1]
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
        hitlist = mm.check_collision(self.rect, tile_array)[1]
        for hit_rect in hitlist:
            if self.reserve_movement[1] > 0:
                self.reserve_movement[1] = 0
                #self.rect.bottom = tile.top
                self.y = hit_rect.top - self.img.get_height()
                collision_types['down'] = True
                self.vel[1] = 0 #if onGround zerogravity

            if self.reserve_movement[1] < 0:
                self.reserve_movement[1] = 0
                #self.rect.top = tile.bottom
                self.y = hit_rect.bottom
                collision_types['top'] = True
                self.vel[1] = 0

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

    def dead(self):
        print("destroy!!")
        self.kill()
        ol.chars.remove(self)





class player(Char):
    def __init__(self, x, y, img, screen):
        super().__init__(x, y, img, screen)

        self.isplayer = True
        self.char_speed = 4
        ol.chars.append(self)

    def charcollision_check(self):
        result, monlist = mm.check_collision_char(self.rect, ol.chars)
        if result:
            if self.reserve_movement[1] > 0:
                return "attack", monlist
            else:
                return "hit", monlist
        else:
            return "none", monlist


class monster(Char):
    def __init__(self, x, y, img, screen):
        super().__init__(x, y, img, screen)

        self.isplayer = False
        self.char_speed = 1
        self.movement[0] = -1
        ol.chars.append(self)


