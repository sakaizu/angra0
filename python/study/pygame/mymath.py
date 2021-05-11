import os
import sys

def clamp(input, mn, mx):
    return max(mn, min(input, mx))


# Collision Check by Rect
def check_collision(self_rect, tile_array):
    colcount = 0
    hitlist = []
    hit = False
    for tile in tile_array:
        if tile.isblock:
            if self_rect.colliderect(tile.rect):
                if self_rect == tile.rect:
                    pass #Ignore Myself
                else:
                    colcount += 1
                    hitlist.append(tile.rect)
    if colcount > 0:
        hit = True
    return hit, hitlist


# Collision Check by Character
def check_collision_char(self_rect, char_array):
    colcount = 0
    charlist = []
    hit = False
    for char in char_array:
        if self_rect.colliderect(char.rect):
            if self_rect == char.rect:
                pass #Ignore myself
            else:
                colcount += 1
                charlist.append(char)
    if colcount > 0:
        hit = True
    return hit, charlist

