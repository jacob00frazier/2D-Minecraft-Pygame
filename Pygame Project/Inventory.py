# Made by Jacob Frazier 12/12/7

import pygame, sys, random

from pygame.locals import *


BLACK = (0,0,0)
BROWN = (153,76,0)
GREEN = (0,225,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
RED = (255,0,0)
GREY = (211,211,211)

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
LAVA = 4
ROCK = 5
DIAMOND = 6

textures = {  DIRT : pygame.image.load("H:\Pygame Project\Textures\Dirt.png"),
             GRASS : pygame.image.load("H:\Pygame Project\Textures\Grass.png"),
             WATER : pygame.image.load("H:\Pygame Project\Textures\Water.png"),
              COAL : pygame.image.load("H:\Pygame Project\Textures\Coal.png"),
              LAVA : pygame.image.load("H:\Pygame Project\Textures\Lava.png"),
              ROCK : pygame.image.load("H:\Pygame Project\Textures\Rock.png"),
           DIAMOND : pygame.image.load("H:\Pygame Project\Textures\Diamond.png")
         }
inventory = {
	     DIRT:0,
	    GRASS:0,
	    WATER:0,
             COAL:0,
          DIAMOND:0,
	     ROCK:0,
	     LAVA:0
}


TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

PLAYER = pygame.image.load("H:\Pygame Project\Textures\Player.png")

playerPos = [0,0]

resources = [DIRT, GRASS, WATER, COAL, DIAMOND, ROCK, LAVA ]

tilemap = [ [DIRT for W in range(MAPWIDTH)] for h in range (MAPHEIGHT)
]

pygame.display.set_caption("Inventory")

pygame.init()

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE + 50))

INVFONT = pygame.font.SysFont("FreeSansBold", 18)

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
            tile = DIAMOND
        else:
            tile = DIRT

        tilemap[rw][cl] = tile


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #these are the controls for the PLAYER
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT and playerPos[0] < MAPWIDTH - 1:
                playerPos[0] += 1
            if event.key == K_LEFT and playerPos[0] > 0:
                playerPos[0] -= 1
            if event.key == K_UP and playerPos[1] > 0:
                playerPos[1] -= 1
            if event.key == K_DOWN and playerPos[1] < MAPHEIGHT - 1:
                playerPos[1] += 1
            if event.key == K_SPACE:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                inventory[currentTile] +=1
                tilemap[playerPos[1]][playerPos[0]] = DIRT

            if(event.key == K_1):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[DIRT] > 0:
                    inventory[DIRT] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = DIRT
                    inventory[currentTile] +=1
            if(event.key == K_2):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[GRASS] > 0:
                    inventory[GRASS] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = GRASS
                    inventory[currentTile] +=1
            if(event.key == K_3):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[WATER] > 0:
                    inventory[WATER] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = WATER
                    inventory[currentTile] +=1
            if(event.key == K_4):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[COAL] > 0:
                    inventory[COAL] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = COAL
                    inventory[currentTile] +=1
            if(event.key == K_5):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[DAIMOND] > 0:
                    inventory[DAIMOND] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = DIAMOND
                    inventory[currentTile] +=1
            if(event.key == K_6):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[ROCK] > 0:
                    inventory[ROCK] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = ROCK
                    inventory[currentTile] +=1
            if(event.key == K_7):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[LAVA] > 0:
                    inventory[LAVA] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = LAVA
                    inventory[currentTile] +=1


    for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                DISPLAYSURF.blit(textures[tilemap[row][column]],(column*TILESIZE,row*TILESIZE))

    DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))

    placePosition = 10
    for item in resources:
        DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
        placePosition += 30
        textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
        placePosition +=50
    pygame.display.update()

