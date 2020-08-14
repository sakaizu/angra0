import pygame
import os


pygame.init()

screen_width= 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("mygame")

#background image
bgimage = pygame.image.load(os.path.join('python/pygame', 'asset/bg.png'))

pcimage = pygame.image.load(os.path.join('python/pygame', 'asset/pc.png'))
pc_size = pcimage.get_rect().size

pc_width = pc_size[0]
pc_height = pc_size[1]
pc_x_pos = screen_width / 2 - (pc_width/2)
pc_y_pos = screen_height - pc_height

mv_x = 0
mv_y = 0

running = True
FPS = 60
Clock = pygame.time.Clock()

while running:
    Clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("game end")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mv_x -= 5
                print(mv_x)
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

    screen.blit(bgimage, (0, 0))
    screen.blit(pcimage,(pc_x_pos, pc_y_pos))

    pygame.display.update()

pygame.quit()