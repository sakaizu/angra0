import pygame
import sys
import os
import numpy as np

class tile:
    def __init__(self, x, y, img, isblock, display):
        self.x = x
        self.y = y
        self.img = img
        self.isblock = isblock
        self.display = display
        self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())

    def draw(self):
        self.display.blit(self.img, (self.x, self.y))

    def appendrect(self, rectarray):
        if self.isblock:
            rectarray.append(self.rect)
        
    def update(self):
        self.draw()



