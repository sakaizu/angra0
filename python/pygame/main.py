import pygame
import os
import random

pygame.font.init()
pygame.init()

screen_width, screen_height =  480, 640

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("mygame")

#background image
bgimage = pygame.transform.scale(pygame.image.load(os.path.join('python/pygame', 'asset/bg.png')), (screen_width, screen_height))

pcimage = pygame.image.load(os.path.join('python/pygame', 'asset/pc.png'))
pc_size = pcimage.get_rect().size

pc_width = pc_size[0]
pc_height = pc_size[1]

# Initial PC position
pc_pos_x = screen_width / 2 - (pc_width/2)
pc_pos_y = screen_height - pc_height


class Pc:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        # self.pcimage = None
    
    def draw(self):
        screen.blit(pcimage, (self.x, self.y))

    def updatePos(self, x, y):
        self.x = x
        self.y = y



running = True
FPS = 60
Clock = pygame.time.Clock()
font_main = pygame.font.SysFont("comicsans", 10)
inputlist = []
CurrentMoveInput = ""

Player = Pc(pc_pos_x, pc_pos_y, 10)


def updateDraw(): #Draw screen every tick
    screen.blit(bgimage, (0, 0))
    # screen.blit(pcimage,(pc_pos_x, pc_pos_y))
    Player.draw()

    # draw ui
    main_label = font_main.render(f"Level: {keys}", 1, (255,0,0))
    screen.blit(main_label, (10, 10))

    pygame.display.update()


while running:
    Clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("game end")

# character Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and pc_pos_x >= 0:
        pc_pos_x -= Player.speed
    if keys[pygame.K_RIGHT] and pc_pos_x + pc_width < screen_width:
        pc_pos_x += Player.speed
    if keys[pygame.K_UP] and pc_pos_y >= 0:
        pc_pos_y -= Player.speed
    if keys[pygame.K_DOWN] and pc_pos_y + pc_height < screen_height:
        pc_pos_y += Player.speed

# game shut down
    if keys[pygame.K_ESCAPE]:
        running = False
        print(" game end")


    
    Player.updatePos(pc_pos_x, pc_pos_y)
    updateDraw()



pygame.quit()