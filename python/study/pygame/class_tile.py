import pygame
import sys
import os
import objectlist as ol
import numpy as np
import gamevalue as gv

class tile(pygame.sprite.Sprite):
    def __init__(self, x, y, img, isblock, display):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.img = img
        self.isblock = isblock
        self.display = display
        self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
        

    def draw(self):
        self.display.blit(self.img, (self.x - gv.scroll[0], self.y - gv.scroll[1]))

        
    def update(self):
        self.draw()



