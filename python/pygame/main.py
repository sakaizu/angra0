import pygame
import os
import random
import math

pygame.font.init()
pygame.init()

screen_width, screen_height =  480, 640

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("mygame")

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
projectileimage = pygame.image.load(os.path.join('python/pygame', 'asset/projectile.png'))

# Initial PC position
pc_pos_x = screen_width / 2 - (pc_width/2)
pc_pos_y = screen_height - pc_height


# Global variable
running = True
FPS = 60.0
DeltaTime = 1/FPS
Clock = pygame.time.Clock()
font_main = pygame.font.SysFont("comicsans", 50)
projectileList = []
enemyList = []
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
    
    def draw(self):
        screen.blit(self.charimg, (self.x, self.y))

    def cooldown(self):
        self.cool_down_counter += DeltaTime * self.FireRate
        if self.cool_down_counter >= 1.0:
            self.cool_down_counter = 1.0
        else:
            self.cool_down_counter += DeltaTime

    def fire(self, vel, dir_x, dir_y):
        if self.cool_down_counter >= 1.0:
            projectileList.append(Projectile(self.x + (pc_width / 2), self.y, vel, dir_x, dir_y))
            self.cool_down_counter = 0

    def multfire(self, vel, dir_x, dir_y):
        if self.cool_down_counter >= 1.0:
            projectileList.append(Projectile(self.x + (pc_width / 2), self.y, vel, dir_x, dir_y))

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
    
    def move(self):
        self.y += self.speed

    def checkBottomFloor(self):
        if self.y > screen_height:
            pass
            


class Projectile:
    def __init__(self, x, y, vel, dir_x, dir_y):
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.img = projectileimage
        self.vel = vel
        self.Maxboundcount = 0
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self):
        screen.blit(self.img, (self.x - (projectileimage.get_width() / 2), self.y))

    def move(self):
        self.x += self.dir_x * self.vel * DeltaTime
        self.y += self.dir_y * self.vel * DeltaTime

    def collision(self, obj):
        return collide(self, obj)

    def checkbound(self):
        if self.y < 0 or self.y > screen_height:
            self.dir_y *= -1

    def update(self):
        self.checkbound()
        self.move()
        self.draw()




# create player char
PlayerChar = Player(pc_pos_x, pc_pos_y, 10)
enemyList.append(Enemy(screen_width/2, 50, 1, "1"))



def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (int(offset_x), int(offset_y))) != None


def updateDraw(): #Draw screen every tick
    screen.blit(bgimage, (0, 0))
    PlayerChar.update()

    for enemy in enemyList:
        enemy.move()
        enemy.update()
    
    for i in projectileList:
        i.update()
        for enemy in enemyList:
            # print(i.collision(enemy))
            if i.collision(enemy):
                projectileList.remove(i)
                print(enemy)


# draw ui
    HP_label = font_main.render(f"HP: {PlayerChar.hp}", 1, (255,0,0))
    Pos_label = font_main.render(f"Pos: {PlayerChar.cool_down_counter}", 1, (0, 255, 0))
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
        PlayerChar.fire(200, 0, -1)

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