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
pc_x_pos = screen_width / 2 - (pc_width/2)
pc_y_pos = screen_height - pc_height

mv_x = 0
mv_y = 0



running = True
FPS = 60
Clock = pygame.time.Clock()
font_main = pygame.font.SysFont("comicsans", 40)


def updateDraw(): #Draw screen every tick
    screen.blit(bgimage, (0, 0))
    screen.blit(pcimage,(pc_x_pos, pc_y_pos))

    # draw ui
    main_label = font_main.render(f"Level: {Clock}", 1, (255,0,0))
    screen.blit(main_label, (10, 10))

    pygame.display.update()


while running:
    Clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("game end")

# character Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                print(" game end")

            if event.key == pygame.K_LEFT:
                mv_x -= 5
            elif event.key == pygame.K_RIGHT:
                mv_x += 5
            elif event.key == pygame.K_UP:
                mv_y -= 2
            elif event.key == pygame.K_DOWN:
                mv_y += 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                mv_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                mv_y = 0

    pc_x_pos += mv_x
    pc_y_pos += mv_y

    if pc_x_pos < 0:
        pc_x_pos = 0
    elif pc_x_pos > screen_width - pc_width:
        pc_x_pos = screen_width - pc_width

    if pc_y_pos < 0:
        pc_y_pos = 0
    elif pc_y_pos + pc_height > screen_height:
        pc_y_pos = screen_height - pc_height
    

    updateDraw()



pygame.quit()