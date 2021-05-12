import pygame
import os
import class_char


class particle(class_char.Sprite_Object):
    def __init__(self, x, y, img, screen):
        super().__init__(x, y, img, screen)