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

# projectile image
projectileimage = pygame.image.load(os.path.join('python/pygame', 'asset/projectile.png'))

# Initial PC position
pc_pos_x = screen_width / 2 - (pc_width/2)
pc_pos_y = screen_height - pc_height

projectileList = []


class Char:

    COOLDOWN = FPS/5

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
        self.cool_down_counter += 1
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = self.COOLDOWN
        else:
            self.cool_down_counter += 1


    def fire(self, vel):
        if self.cool_down_counter == self.COOLDOWN:
            projectileList.append(Projectile(self.x + (pc_width / 2), self.y, vel, 0, -1))
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
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed)
        self.charimg = pcimage
        self.mask = pygame.mask.from_surface(self.charimg)
    
    def move(self):
        self.y += self.speed


class Projectile:
    def __init__(self, x, y, vel, dir_x, dir_y):
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.img = projectileimage
        self.vel = vel
        self.Maxboundcount = 0

    def draw(self):
        screen.blit(self.img, (self.x - (projectileimage.get_width() / 2), self.y))

    def move(self):
        self.x += self.dir_x * self.vel
        self.y += self.dir_y * self.vel

    def collision(self, obj):
        return collide(self, obj)

    def checkbound(self):
        if self.y < 0 or self.y > screen_height:
            self.dir_y *= -1

    def update(self):
        self.checkbound()
        self.move()
        self.draw()





running = True
FPS = 60
Clock = pygame.time.Clock()
font_main = pygame.font.SysFont("comicsans", 50)

# create player char
PlayerChar = Player(pc_pos_x, pc_pos_y, 10)
EnemyChar = Enemy(screen_width/2, 50, 1)


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2, (offset_x, offset_y)) != None


def updateDraw(): #Draw screen every tick
    screen.blit(bgimage, (0, 0))
    PlayerChar.update()
    EnemyChar.draw()
    EnemyChar.move()

# draw ui
    HP_label = font_main.render(f"HP: {PlayerChar.hp}", 1, (255,0,0))
    Pos_label = font_main.render(f"Pos: {PlayerChar.cool_down_counter}", 1, (0, 255, 0))
    screen.blit(HP_label, (10, 10))
    screen.blit(Pos_label, (10, 50))

    for i in projectileList:
        i.update()

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
    if keys[pygame.K_SPACE]:
        PlayerChar.fire(2)


# game shut down
    if keys[pygame.K_ESCAPE]:
        running = False
        print(" game end")

    
    updateDraw()



pygame.quit()