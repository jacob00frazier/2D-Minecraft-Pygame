# Made by Jacob Frazier 12/6/7

import pygame, sys, random

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
DAIMOND = 6 

textures = {  DIRT : pygame.image.load("H:\Pygame Project\Textures\Dirt.png"),
             GRASS : pygame.image.load("H:\Pygame Project\Textures\Grass.png"),
             WATER : pygame.image.load("H:\Pygame Project\Textures\Water.png"),
              COAL : pygame.image.load("H:\Pygame Project\Textures\Coal.png"),
              LAVA : pygame.image.load("H:\Pygame Project\Textures\Lava.png"),
              ROCK : pygame.image.load("H:\Pygame Project\Textures\Rock.png"),
           DAIMOND : pygame.image.load("H:\Pygame Project\Textures\Daimond.png")
         }


TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20


tilemap = [ [DIRT for W in range(MAPWIDTH)] for h in range (MAPHEIGHT)
]



pygame.init()

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

for rw in range(MAPHEIGHT):
    for cl in range(MAPWIDTH):
        randomNumber = random.randint(0,20)
        if randomNumber == 0:
            tile = COAL
        elif randomNumber == 1 or randomNumber == 2:
            tile = WATER
        elif randomNumber >= 3 and randomNumber <= 10:
            tile = GRASS
        elif randomNumber >= 11 and randomNumber <= 12:
            tile = LAVA
        elif randomNumber >= 13 and randomNumber <= 15:
            tile = ROCK
        elif randomNumber == 16:
            tile = DAIMOND
        else:
            tile = DIRT

        tilemap[rw][cl] = tile

pygame.display.set_caption("Lists")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                DISPLAYSURF.blit(textures[tilemap[row][column]],(column*TILESIZE,row*TILESIZE))

    pygame.display.update()

