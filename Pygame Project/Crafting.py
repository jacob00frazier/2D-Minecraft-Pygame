# Made by Jacob Frazier 12/18/17

import pygame, sys, random

from pygame.locals import *



BLACK = (0,0,0)
BROWN = (153,76,0)
GREEN = (0,225,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
RED = (255,0,0)
GREY = (211,211,211)

cloudx = -200
cloudx2 = -200
Birdx = -400
Birdy = 50
cloudy = 120
cloudy2 = 0


DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
LAVA = 4
ROCK = 5
DIAMOND = 6
CLOUD = 7
BIRD = 8
FIRE = 9
SAND = 10
GLASS = 11
STONE = 13
BRICK = 14
WOOD = 15


textures = {  DIRT : pygame.image.load("H:\Pygame Project\Textures\Dirt.png"),
             GRASS : pygame.image.load("H:\Pygame Project\Textures\Grass.png"),
             WATER : pygame.image.load("H:\Pygame Project\Textures\Water.png"),
              COAL : pygame.image.load("H:\Pygame Project\Textures\Coal.png"),
              LAVA : pygame.image.load("H:\Pygame Project\Textures\Lava.png"),
              ROCK : pygame.image.load("H:\Pygame Project\Textures\Rock.png"),
           DIAMOND : pygame.image.load("H:\Pygame Project\Textures\Diamond.png"),
             CLOUD : pygame.image.load("H:\Pygame Project\Textures\Cloud.png"),
              BIRD : pygame.image.load("H:\Pygame Project\Textures\Bird.png"),
               WOOD: pygame.image.load("H:\Pygame Project\Textures\Wood.png"),
               FIRE: pygame.image.load("H:\Pygame Project\Textures\Fire.png"),
               SAND: pygame.image.load("H:\Pygame Project\Textures\Sand.png"),
              GLASS: pygame.image.load("H:\Pygame Project\Textures\Glass.png"),
              STONE: pygame.image.load("H:\Pygame Project\Textures\Stone.png"),
              BRICK: pygame.image.load("H:\Pygame Project\Textures\Brick.png")
}

inventory = {
	     DIRT:0,
	    GRASS:0,
	    WATER:0,
             COAL:0,
          DIAMOND:0,
	     ROCK:0,
	     LAVA:0,
             WOOD:0,
             FIRE:0,
             SAND:0,
            GLASS:0,
            STONE:0,
            BRICK:0
}
controls = {
            DIRT:96,
	    GRASS:49,
	    WATER:50,
             COAL:51,
          DIAMOND:52,
	     ROCK:53,
	     LAVA:54,
             WOOD:55,
             FIRE:56,
             SAND:57,
            GLASS:48,
            STONE:45,
            BRICK:61,
}
craft = {
            FIRE : { WOOD : 2, ROCK : 2},
           STONE : { ROCK : 2},
           GLASS : { FIRE: 1, SAND : 2},
         DIAMOND : { WOOD : 2, COAL : 3},
           BRICK : { ROCK : 2, FIRE : 1},
            SAND : { ROCK : 2}
}
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 20

PLAYER = pygame.image.load("H:\Pygame Project\Textures\Player.png")

playerPos = [0,0]

resources = [DIRT, GRASS, WATER, COAL, DIAMOND, ROCK, LAVA,
             WOOD, FIRE, SAND, GLASS, STONE, BRICK]

tilemap = [ [DIRT for W in range(MAPWIDTH)] for h in range (MAPHEIGHT)
]


pygame.display.set_icon(pygame.image.load("H:\Pygame Project\Textures\Player.png"))

pygame.init()

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE + 50))

INVFONT = pygame.font.SysFont("FreeSansBold", 18)

fpsClock = pygame.time.Clock()

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
        elif randomNumber == 17:
            tile = WOOD
        else:
            tile = DIRT

        tilemap[rw][cl] = tile


while True:
    pygame.display.set_caption("Minecraft--2D")
    DISPLAYSURF.fill(BLACK)
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

            for key in controls:
                if(event.key == controls[key]):
                    if pygame.mouse.get_pressed()[0]:
                        if key in craft:
                            canBeMade = True
                            for i in craft[key]:
                                if craft[key][i] > inventory[i]:
                                    canBeMade = False
                                    break
                            if canBeMade == True:
                                for i in craft[key]:
                                    inventory[i] -= craft[key][i]
                                inventory[key] +=1                    
    
                    else:
                        currentTile = tilemap[playerPos[1]][playerPos[0]]
                        if inventory[key] > 0:
                            inventory[key] -= 1
                            inventory[currentTile] +=1
                            tilemap[playerPos[1]][playerPos[0]] = key
                 

            
    for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                DISPLAYSURF.blit(textures[tilemap[row][column]],(column*TILESIZE,row*TILESIZE))

    DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))
	
    DISPLAYSURF.blit(textures[CLOUD].convert_alpha(),(cloudx,cloudy))
    cloudx+=1
    if cloudx> MAPWIDTH*TILESIZE:
	    cloudy = random.randint(0,MAPHEIGHT*TILESIZE)
	    cloudx = -200

    DISPLAYSURF.blit(textures[CLOUD].convert_alpha(),(cloudx2,cloudy2))
    cloudx2+=2
    if cloudx2> MAPWIDTH*TILESIZE:
	    cloudy2 = random.randint(0,MAPHEIGHT*TILESIZE)
	    cloudx2 = -200

    DISPLAYSURF.blit(textures[BIRD].convert_alpha(),(Birdx,Birdy))
    Birdx+=4
    if Birdx> MAPWIDTH*TILESIZE:
	    Birdy = random.randint(0,MAPHEIGHT*TILESIZE-50)
	    Birdx = -400
   

    fpsClock.tick(24)
	
    placePosition = 10
    for item in resources:
        DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*TILESIZE+20))
        placePosition += 10
        textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*TILESIZE+20))
        placePosition +=30
    pygame.display.update()

