import pygame
import sys
import os
import mymath as mm
import objectlist as ol
import gamevalue

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, img, screen):
        super().__init__(x, y, img, screen)


class Char(pygame.sprite.Sprite):
    def __init__(self, x, y, img, screen):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.isplayer = True
        self.isdead = False
        self.img = img
        self.screen = screen
        self.movement = [0,0]
        self.char_speed = 5
        self.currentspeed = 1
        self.ismoving = False
        self.accel =[0,0] #accelation speed
        self.vel = [0,0]
        self.reserve_movement = [0,0]
        self.isblock = False
        self.collision_types = {'top' : False, 'down' : False, 'left' : False, 'right' : False}
        self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())



    def movement_accel(self):
        if self.ismoving:
            self.currentspeed += 0.05
        else:
            self.currentspeed -= 0.15

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
        self.reserve_movement[0] = round((self.movement[0] * self.char_speed)* self.currentspeed + self.vel[0])
        self.reserve_movement[1] = round((self.movement[1] * self.char_speed)* self.currentspeed + self.vel[1])


    def movecheck(self, Group):
        self.collision_types = {'top' : False, 'down' : False, 'left' : False, 'right' : False}

        self.set_reserve_movement()

        if self.isdead == False:
            self.rect.x += self.reserve_movement[0]
            hitlist = mm.check_collision_tileGroup(self.rect, Group)[1]
            for hit_obj in hitlist:
                if self.reserve_movement[0] > 0:
                    self.reserve_movement[0] = 0

                    self.x = hit_obj.rect.left - self.img.get_width()
                    self.collision_types['right'] = True

                elif self.reserve_movement[0] < 0:
                    self.reserve_movement[0] = 0

                    self.x = hit_obj.rect.right
                    self.collision_types['left'] = True

            self.rect.x = self.x #restore rect collision test


            self.rect.y += self.reserve_movement[1]
            hitlist = mm.check_collision_tileGroup(self.rect, Group)[1]
            for hit_obj in hitlist:
                if self.reserve_movement[1] > 0:
                    self.reserve_movement[1] = 0

                    self.y = hit_obj.rect.top - self.img.get_height()
                    self.collision_types['down'] = True
                    self.vel[1] = 0 #if onGround zerogravity

                if self.reserve_movement[1] < 0:
                    self.reserve_movement[1] = 0

                    self.y = hit_obj.rect.bottom
                    self.collision_types['top'] = True
                    self.vel[1] = 0

            self.rect.y = self.y #restore rect collision test

        return self.collision_types


    def draw(self):
        self.screen.blit(self.img, (self.x - gamevalue.scroll[0], self.y - gamevalue.scroll[1]))

    def update(self):
        self.move()
        self.draw()

    def dead(self):
        self.img = pygame.transform.flip(self.img, False, True)
        self.isdead = True
        print("destroy - %s" %self)
        #self.kill()





class player(Char):
    def __init__(self, x, y, img, screen):
        super().__init__(x, y, img, screen)

        self.isplayer = True
        self.isjumpable = True
        self.char_speed = 4
        self.jumpCount = 5
        ol.obj_chars.add(self)
        ol.player = self


    def charcollision_check(self):
        result, monlist = mm.check_collision_charGroup(self.rect, ol.obj_chars)
        if result:
            if self.reserve_movement[1] > 0:
                return "attack", monlist
            else:
                return "hit", monlist
        else:
            return "none", monlist

    def jump(self):
        if self.isjumpable:
            self.vel[1] = -7
            self.isjumpable = False

    def checkaction(self):
        if self.isdead == False:
            action, hitlist = self.charcollision_check()
            if action == "attack":
                self.vel[1] = -7
                for mon in hitlist:
                    mon.dead()
                    mon.vel[1] = -7
                    break
            elif action == "hit":
                self.vel[1] = -7
                self.isdead = True
                pygame.time.wait(300)

    def update(self):
        super().update()
        self.checkaction()

# jump reset
        if self.collision_types["down"] == True:
            self.isjumpable = True



class monster(Char):
    def __init__(self, x, y, img, screen):
        super().__init__(x, y, img, screen)

        self.isplayer = False
        self.char_speed = 1
        self.movement[0] = -1
        ol.obj_chars.add(self)
    
    def check_screenout(self):
        if self.x < 0 or self.x > gamevalue.WINDOW_SIZE[0] or self.y > gamevalue.WINDOW_SIZE[1]:
            self.kill()
    
    def update(self):
        super().update()
        self.check_screenout()

