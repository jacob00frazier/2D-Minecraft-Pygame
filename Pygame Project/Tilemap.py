# Made by Jacob Frazier 12/6/6

import pygame, sys
from pygame.locals import *


BLACK = (0,0,0)
BROWN = (153,76,0)
GREEN = (0,225,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREY = (211,211,211)

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
LAVA = 4
ROCK = 5

colours = {  DIRT : BROWN,
            GRASS : GREEN,
            WATER : BLUE,
             COAL : BLACK,
             LAVA : RED,
             ROCK : GREY
         }

tilemap = [ [GRASS, ROCK, DIRT, WATER, ROCK],
            [WATER, WATER, GRASS, DIRT, LAVA],
            [COAL, GRASS, WATER, GRASS, LAVA],
            [LAVA, LAVA, COAL, WATER, COAL],
            [GRASS, WATER, DIRT, ROCK, ROCK],
            
        ]


TILESIZE = 40
MAPWIDTH = 5
MAPHEIGHT = 5

pygame.init()

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

pygame.display.set_caption("TIlemap")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]],(column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))

    pygame.display.update()

