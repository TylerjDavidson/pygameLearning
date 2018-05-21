#!/usr/bin/python

import pygame, sys
from pygame.locals import *
import math

pygame.init()
## Set up window ##

# Change stripe width to change size of flag #
stripeW = 40

width = 13*stripeW
length = int(math.floor(1.9*width))
DISPLAYSURF = pygame.display.set_mode((length,width))
pygame.display.set_caption('Drawing Practice')

## Set up Colors ##
RED = (255,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

## Draw on surface object ##
DISPLAYSURF.fill(WHITE)

# Red Stripes
stripeW = width/13 #stripe width
stripeL = length   #stripe Length
i = 0   #Stripe position indicator
n = 0
while n <= width:
    pygame.draw.rect(DISPLAYSURF,RED,(0,n,stripeL,stripeW))
    i = i+1
    n = i*2*stripeW

#Blue Union
UnionL =int(round(0.76*width))
UnionW = int(round(0.5385*width))
pygame.draw.rect(DISPLAYSURF,BLUE,(0,0,UnionL,UnionW))

#White Stars
starposx = int(math.floor(0.065*width))
starposy = int(math.floor(0.065*width))
starRad = int(math.floor(0.0315*width))
starDiam =int(math.floor(0.065*width))

j = 0
k = 0
z = 0
b = 1
starnum = 0
while starnum <= 31:
    pygame.draw.circle(DISPLAYSURF,WHITE,(starposx,starposy),starRad)
    j = j + 1
    starnum = starnum + 1
    if j < 7:
        pygame.draw.circle(DISPLAYSURF,WHITE,(starposx + ((j-1)*2*starDiam),starposy + 2*z*starDiam),starRad)
        if k < 5:
            pygame.draw.circle(DISPLAYSURF,WHITE,(2*starposx + (k*2*starDiam),starposy + starDiam + 2*z*starDiam),starRad)
            k = k + 1
    if j > 7:
        j = 0
        k = 0
        z = z + 1
    if z > 4:
        pygame.draw.circle(DISPLAYSURF,WHITE,(starposx + (j*2*starDiam),starposy + 2*z*starDiam),starRad)


#Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
