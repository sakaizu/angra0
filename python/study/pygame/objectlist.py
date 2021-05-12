import pygame
import os
import sys

player = None
tiles = []
chars = []

obj_chars = pygame.sprite.Group()
obj_tiles = pygame.sprite.Group()

def clean():
    player = None
    obj_chars.empty()
    obj_tiles.empty()


