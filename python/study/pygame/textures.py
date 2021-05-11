import pygame
import sys
import os

datapath = os.path.join(os.getcwd(), "data")

#player image
player_image_r = pygame.image.load(os.path.join(datapath, "player_01.png"))
player_image_l = pygame.image.load(os.path.join(datapath, "player_02.png"))


monster_image_1 = pygame.image.load(os.path.join(datapath, "mon_01.png"))


#background image
bg_image = pygame.image.load(os.path.join(datapath, "BG.png"))
bg_moss_01 = pygame.image.load(os.path.join(datapath, "BG_moss_01.png"))
bg_moss_02 = pygame.image.load(os.path.join(datapath, "BG_moss_02.png"))

bg_test_01 = pygame.image.load(os.path.join(datapath, "BG_test_01.png"))


