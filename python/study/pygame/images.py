import pygame
import sys
import os

datapath = os.path.join(os.getcwd(), "data")

#player image
player_image = pygame.image.load(os.path.join(datapath, "player_02.png"))

bg_image = pygame.image.load(os.path.join(datapath, "BG.png"))

