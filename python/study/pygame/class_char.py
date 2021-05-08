import pygame
import sys
import os

class MyChar:
    def __init__(self, x, y, img, screen):
        self.x = x
        self.y = y
        self.img = img
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

    def construct(self):
        allrect.append(self.rect)

    def move(self, x, y):
        self.x += x * 5
        self.y += y * 5
    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.draw()
    def create(self):
        f = open(os.path.join(datapath, "test.txt"), 'w')
        f.close()

    def checkcollide(self, rect):
        return self.rect.colliderect(rect)
