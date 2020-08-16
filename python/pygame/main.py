import pygame
import os
import random
import math
from pygame.math import Vector2

pygame.font.init()
pygame.init()

screen_width, screen_height =  480, 640

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("mygame")

# Test image
testimage = pygame.image.load(os.path.join('python/pygame', 'asset/testImg.png'))

# background image
bgimage = pygame.transform.scale(pygame.image.load(os.path.join('python/pygame', 'asset/bg.png')), (screen_width, screen_height))

# Player image
pcimage = pygame.image.load(os.path.join('python/pygame', 'asset/pc.png'))
pc_size = pcimage.get_rect().size
pc_width = pc_size[0]
pc_height = pc_size[1]

# enemy image
enemyimage = pygame.image.load(os.path.join('python/pygame', 'asset/enemy.png'))

# projectile image
projectileEnemyimage = pygame.image.load(os.path.join('python/pygame', 'asset/projectile.png'))
projectileFriendimage = pygame.image.load(os.path.join('python/pygame', 'asset/projectile_f.png'))

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
# enemyList = []
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
        else:
            self.cool_down_counter += DeltaTime

    def fire(self, vel, dir_x, dir_y, isFoe):
        if self.cool_down_counter >= 1.0:
            projectileList.append(Projectile(self.x + (pc_width / 2), self.y, vel, dir_x, dir_y, isFoe))
            self.cool_down_counter = 0

    def multfire(self, vel, dir_x, dir_y, isFoe):
        if self.cool_down_counter >= 1.0:
            projectileList.append(Projectile(self.x + (pc_width / 2), self.y, vel, dir_x, dir_y, isFoe))

    def setcooltime(self):
        self.cool_down_counter = 0

    def checkhealth(self):
        if self.hp <= 0:
            print("death")
            return "Kill"
        else:
            print("notdeath")
            return None

    def damaged(self, damage):
        self.hp -= damage

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
        # rotateTest(self.charimg, self.x, self.y)
        screen.blit(self.charimg, (self.x, self.y))
            
    def update(self):
        self.draw()
        self.cooldown()
    
    def checkhealth(self):
        if self.hp <= 0:
            return True
        else:
            return None



class Projectile:
    def __init__(self, x, y, vel, dir_x, dir_y, isFoe):
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.img = projectileFriendimage
        self.vel = vel
        self.isFoe = isFoe
        self.boundcount = 3
        self.lifetime = 0
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self):
        imgcenter = self.img.get_rect().center
        rotateimg = pygame.transform.rotate(self.img, self.lifetime * 300)
        rotatePivot = rotateimg.get_rect(center = imgcenter)
        screen.blit(rotateimg, (self.x - imgcenter[0] + rotatePivot[0], self.y + rotatePivot[1]))

    def move(self):
        self.x += self.dir_x * self.vel * DeltaTime
        self.y += self.dir_y * self.vel * DeltaTime

    def collision(self, obj):
        return collide(self, obj)


    def changeSide(self):
        if self.isFoe:
            self.isFoe = False
            self.img = projectileFriendimage
        else:
            self.isFoe = True
            self.img = projectileEnemyimage


    def checkbounce(self):
        if self.y < 0 or self.y > screen_height:
            self.changeSide()
            if self.boundcount >= 0:
                self.dir_y *= -1
                self.boundcount -= 1
                return "bounce"
            else:
                return "kill"

    def update(self):
        self.lifetime += DeltaTime
        self.move()
        self.draw()


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (int(offset_x), int(offset_y))) != None

def spawnEnemyCool():
    global enemycooltime
    if enemycooltime >= 1:
        charList.append(Enemy(random.randrange(50, screen_width-50), random.randrange( -100, -50), 1, "1"))
        enemycooltime = 0
    else:
        enemycooltime += DeltaTime

def rotateTest(img, x, y):

    imgcenter = img.get_rect().center
    
    rotateimg = pygame.transform.rotate(img, pygame.time.get_ticks()/10)
    r = rotateimg.get_rect()
    print(r)

    newpivot = rotateimg.get_rect(center = imgcenter)

    a = screen.blit(rotateimg, (newpivot[0] + x, newpivot[1] + y))
    pygame.draw.circle(screen, (0, 255, 0), (newpivot[0]+ x,  newpivot[1]+ y), 7, 0)


# create player char
PlayerChar = Player(pc_pos_x, pc_pos_y, 10)
# charList.append(Enemy(screen_width/2, 50, 1, "1"))
charList.append(PlayerChar)



def updateDraw(): #Draw screen every tick
    screen.blit(bgimage, (0, 0))

    spawnEnemyCool()
    # rotateTest(enemyimage, 100 ,100)

    for char in charList:
        if char.isFoe:  # enemychar udpate
            char.move()
            char.update()
        else:
            char.update() # playerchar update

    for i in projectileList:
        i.update()
        if i.checkbounce() == "kill":
            projectileList.remove(i)

        for char in charList:
            if i.collision(char):
                if char.isFoe != i.isFoe:
                    projectileList.remove(i)
                    char.damaged(10)
                    if char.checkhealth() == True:
                        charList.remove(char)


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

        


# character Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and PlayerChar.x >= 0:
        PlayerChar.x -= PlayerChar.speed
    if keys[pygame.K_RIGHT] and PlayerChar.x + pc_width < screen_width:
        PlayerChar.x += PlayerChar.speed
    if keys[pygame.K_UP] and PlayerChar.y >= 0:
        PlayerChar.y -= PlayerChar.speed
    if keys[pygame.K_DOWN] and PlayerChar.y + pc_height < screen_height:
        PlayerChar.y += PlayerChar.speed

# character Fire
    if keys[pygame.K_SPACE]:
        PlayerChar.fire(200, 0, -1, False)

        # for i in range(1, 11):
        #     x = math.cos(float(i/10) * (math.pi * 2))
        #     y = math.sin(float(i/10) * (math.pi * 2))
        #     PlayerChar.multfire(200, x, y)
        # PlayerChar.setcooltime()




# game shut down
    if keys[pygame.K_ESCAPE]:
        running = False
        print(" game end")

    
    updateDraw()



pygame.quit()