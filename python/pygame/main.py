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
bgimage = pygame.image.load(os.path.join('python/pygame', 'asset/bg.png')).convert()

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

# particle image
particleimg = pygame.image.load(os.path.join('python/pygame', 'asset/particle.png'))

# Initial PC position
pc_pos_x = screen_width / 2 - (pc_width/2)
pc_pos_y = screen_height - pc_height


# Global variable
running = True
FPS = 60.0
DeltaTime = 1/FPS
GameTime = 0
enemycooltime = 0
Clock = pygame.time.Clock()
isGameover = False
font_main = pygame.font.SysFont("comicsans", 25)

bgpos = 0 - bgimage.get_rect().center[1]

Gameover_label = font_main.render("GAME OVER", 1, (0, 255, 0))

projectileList = []
charList = []
particleList = []




class Char:

    FireRate = 5

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.charimg = None
        self.speed = speed
        self.hp = 100
        self.cool_down_counter = 0
        self.cool_down_Max = 1
        self.isFoe = False

    def reset(self):
        self.hp = 100
    
    def draw(self):
        screen.blit(self.charimg, (self.x, self.y))

    def cooldown(self):
        self.cool_down_counter += DeltaTime * self.FireRate
        if self.cool_down_counter >= self.cool_down_Max:
            self.cool_down_counter = self.cool_down_Max
        else:
            self.cool_down_counter += DeltaTime

    def fire(self, vel, dir_x, dir_y, isFoe):
        if self.cool_down_counter >= 1.0:
            projectileList.append(Projectile(self.x + self.charimg.get_rect().center[0], self.y, vel, dir_x, dir_y, isFoe))
            self.cool_down_counter = 0

    def multfire(self, vel, dir_x, dir_y, isFoe):
        if self.cool_down_counter >= 1.0:
            projectileList.append(Projectile(self.x + (pc_width / 2), self.y, vel, dir_x, dir_y, isFoe))

    def setcooltime(self):
        self.cool_down_counter = 0

    def checkhealth(self):
        if self.hp <= 0:
            return True
        else:
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

    def __init__(self, x, y, speed, var, hp):
        super().__init__(x, y, speed)
        self.charimg = self.VARI_MAP[var]
        self.mask = pygame.mask.from_surface(self.charimg)
        self.isFoe = True
        self.cool_down_Max = 5
        self.hp = hp
    
    def move(self):
        self.y += self.speed


    def lockfire(self, vel):
        if isGameover == False:
            if self.cool_down_counter >= self.cool_down_Max and self.y > 10:
                normalizeddir = pygame.math.Vector2(PlayerChar.x - PlayerChar.charimg.get_rect().center[0] - self.x, PlayerChar.y - self.y).normalize()
                self.fire(vel, normalizeddir[0], normalizeddir[1], True)
                self.cool_down_counter = 0


    def checkBottomFloor(self):
        if self.y > screen_height:
            pass

    def drawhp(self):
        EnemyHp_label = font_main.render(f"{self.hp}", 1, (0, 255, 0))
        screen.blit(EnemyHp_label, (self.x + self.charimg.get_rect().center[0], self.y + self.charimg.get_rect().center[1]))

    def draw(self):
        # rotateTest(self.charimg, self.x, self.y)
        screen.blit(self.charimg, (self.x, self.y))
            
    def update(self):
        self.draw()
        self.drawhp()
        self.cooldown()
        self.lockfire(200)


class Projectile:
    def __init__(self, x, y, vel, dir_x, dir_y, isFoe):
        self.x = x
        self.y = y
        self.dir_x = float(dir_x)
        self.dir_y = float(dir_y)
        self.img = projectileFriendimage
        self.vel = float(vel)
        self.isFoe = isFoe
        self.boundcount = 3
        self.age = 0
        self.mask = pygame.mask.from_surface(self.img)
        self.kill = False

    def draw(self):
        if self.isFoe:
            self.img = projectileEnemyimage

        imgcenter = self.img.get_rect().center
        rotateimg = pygame.transform.rotate(self.img, self.age * 300)
        rotatePivot = rotateimg.get_rect(center = imgcenter)
        screen.blit(rotateimg, (self.x - imgcenter[0] + rotatePivot[0], self.y + rotatePivot[1]))

    def move(self):
        self.x += self.dir_x * self.vel * DeltaTime
        self.y += self.dir_y * self.vel * DeltaTime

    def collision(self, obj):
        return collide(self, obj)

    def changeSide(self):
        spawnparticle(self.x, self.y, enemyimage, 0.5, 50)
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
            else:
                return True
        if self.x < 0 or self.x > screen_width:
            self.changeSide()
            if self.boundcount >= 0:
                self.dir_x *= -1
                self.boundcount -= 1
            else:
                return True

    def update(self):
        self.age += DeltaTime
        self.move()
        self.draw()




class particle:
    def __init__(self, x, y, img, lifetime, size, dir_x, dir_y, vel):
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.vel = vel
        self.img = img
        self.lifetime = lifetime
        self.age = 0.0
        self.normalizeage = 0
        self.size = size
        self.kill = False
        self.scalebias = 0
        self.scaletype = 1

    def timer(self):
        self.age += DeltaTime
        self.normalizeage = self.age / self.lifetime

    def calcscale(self):
        if self.scaletype == 0:
            if self.normalizeage < 0.5:
                self.scalebias  = self.normalizeage * 2
            else:
                self.scalebias = (1 - self.normalizeage) * 2
                if self.scalebias < 0:
                    self.scalebias = 0
        elif self.scaletype == 1:
            self.scalebias = 1 - self.normalizeage
            if self.scalebias < 0:
                    self.scalebias = 0

    def move(self):
        self.x += self.dir_x * DeltaTime * self.vel * (1 - self.normalizeage)
        self.y += self.dir_y * DeltaTime * self.vel * (1 - self.normalizeage)

    def draw(self):
       scaleimg = pygame.transform.scale(self.img, (int(self.scalebias * self.size), int(self.scalebias * self.size)))
       screen.blit(scaleimg, (self.x - scaleimg.get_rect().center[0], self.y - scaleimg.get_rect().center[1]))

    def checklifetime(self):
        if self.age > self.lifetime:
            self.kill = True

    def update(self):
        self.timer()
        self.move()
        self.calcscale()
        self.draw()
        self.checklifetime()




def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (int(offset_x), int(offset_y))) != None

def spawnEnemyCool():
    global enemycooltime
    if enemycooltime >= 1:
        charList.append(Enemy(random.randrange(50, screen_width-50), random.randrange( -150, -100), 1, "1", random.randint(10, 100)))
        enemycooltime = 0
    else:
        enemycooltime += DeltaTime

def scrollbg():
    global bgpos
    if bgpos >= 0:
        bgpos = 0 - bgimage.get_rect().center[1]
    else:
        bgpos += 0.5

    screen.blit(bgimage, (0, bgpos))

def rotateTest(img, x, y):

    imgcenter = img.get_rect().center
    
    rotateimg = pygame.transform.rotate(img, pygame.time.get_ticks()/10)
    r = rotateimg.get_rect()
    print(r)

    newpivot = rotateimg.get_rect(center = imgcenter)

    a = screen.blit(rotateimg, (newpivot[0] + x, newpivot[1] + y))
    pygame.draw.circle(screen, (0, 255, 0), (newpivot[0]+ x,  newpivot[1]+ y), 7, 0)




def spawnparticle(x, y, img, lifetime, size):
    dir_x = 0
    dir_y = 0
    vel = 0

    particleList.append(particle(x, y, img, lifetime, size, dir_x, dir_y, vel))

def burstparticles(x, y, img, count, vel, size):
    for i in range(1, count + 1):
        dir_x = math.cos(float(i/count) * (math.pi * 2)) * 100
        dir_y = math.sin(float(i/count) * (math.pi * 2)) * 100

        particlelifetime = random.random() * 3
        particlevel = vel * random.random()
        particlesize = size
        particleList.append(particle(x, y, img, particlelifetime , particlesize, dir_x, dir_y, particlevel))

def checkgameover():
    global isGameover
    if PlayerChar in charList:
        pass
    else:
        isGameover = True
        screen.blit(Gameover_label, (screen_height/2, screen_width/2))

def resetgame():
    global isGameover
    charList.clear()
    projectileList.clear()
    charList.append(PlayerChar)
    PlayerChar.reset()
    isGameover = False



# create player char
PlayerChar = Player(pc_pos_x, pc_pos_y, 5)
# charList.append(Enemy(screen_width/2, 50, 1, "1"))
charList.append(PlayerChar)



def updateDraw(): #Draw screen every tick

    global GameTime
    GameTime += DeltaTime
    scrollbg()
    spawnEnemyCool()

    for char in charList:
        if char.isFoe:  # enemychar udpate
            char.move()
            char.update()
        else:
            char.update() # playerchar update


    for i in projectileList:
        i.update()
        for char in charList:
            if i.collision(char):
                if char.isFoe != i.isFoe:
                    spawnparticle(i.x, i.y, particleimg, 0.35, 50)
                    burstparticles(i.x, i.y, particleimg, 20, 1, 5)
                    i.kill = True
                    char.damaged(10)
                    if char.checkhealth() == True:
                        charList.remove(char)
                        burstparticles(char.x + char.charimg.get_rect().center[0], char.y + char.charimg.get_rect().center[1], particleimg, 100, 5, 20)

        if i.checkbounce():
            i.kill = True

        if i.kill:
            projectileList.remove(i)


    for p in particleList:
        p.update()
        if p.kill:
            particleList.remove(p)


# draw ui
    HP_label = font_main.render(f"HP: {PlayerChar.hp}", 1, (255,0,0))
    Pos_label = font_main.render(f"data01: {len(projectileList)}", 1, (0, 255, 0))
    Particle_label = font_main.render(f"data02: {len(particleList)}", 1, (0, 255, 0))
    screen.blit(HP_label, (10, 10))
    screen.blit(Pos_label, (10, 50))
    screen.blit(Particle_label, (10, 100))

# Check Player Dead
    checkgameover()

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


# reset
    if keys[pygame.K_SPACE]:
        if isGameover:
            resetgame()



# game shut down
    if keys[pygame.K_ESCAPE]:
        running = False
        print(" game end")

    
    updateDraw()



pygame.quit()