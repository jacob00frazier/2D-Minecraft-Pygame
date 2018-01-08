# Made by Jacob Frazier 12/6/6

import pygame

import pygame, sys

from pygame.locals import *

pygame.init()


DISPLAYSURF = pygame.display.set_mode((300,300))

pygame.display.set_caption("Intro-Python")



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.draw.rect(DISPLAYSURF,(0,255,0),(50,50,20,20))
    pygame.draw.rect(DISPLAYSURF,(255,0,0),(100,50,30,30))
    pygame.draw.rect(DISPLAYSURF,(0,0,255),(160,50,40,40))
    pygame.draw.rect(DISPLAYSURF,(160,32,240),(230,50,50,50))
    pygame.draw.polygon(DISPLAYSURF, (255,0,0), [[100, 100], [0, 200], [200, 200]], 0)
    pygame.draw.ellipse(DISPLAYSURF, (0,0,255), [225, 10, 50, 20], 0) 
    pygame.draw.circle(DISPLAYSURF, (0,255,0) , [60, 250], 40)

    pygame.display.update()
    
    
       

