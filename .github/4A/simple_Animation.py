# Simple Animation with Pygame, Julian Guevara, 1/27/22, 2:30pm, v0.6

from _typeshed import ReadableBuffer
import pygame, sys, time
from pygame.locals import *

#setup pygame
pygame.init()

# setup the window
windowwidth = 400
windowheight = 400
windowSurface = pygame.display.set_mode((windowwidth, windowheight), 0, 32)
pygame.displat.set caption('Animation Example!')

# setup the direction variables.
downleft = 'downleft'
downright = 'downright'
upleft = 'upleft'
upright = 'upright'

movespeed =  4

# setup color values.
white = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
BLUE = (0, 255, 0)

#setup the box data.
b1 = {'rect' :pygame.rect(300, 80, 50, 100), 'color':RED, 'dir':upright}
b2 = {'rect' :pygame.rect(200, 200, 20, 20), 'color':RED, 'dir':upright}
b3 = {'rect' :pygame.rect(100, 150, 60, 60), 'color':RED, 'dir':upright}
boxes = [b1, b2, b3]

# Run the game loop.
while True: 
    # Check for QUIT event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(white)

    for b in boxes:
        # Move the box data structure.
        if b['dir'] == downleft:
            b['rect'].left -= movespeed
            b['rect'].top += movespeed
            if b['dir'] == downright:
                b['rect'].left += movespeed
                b['rect'].top += movespeed
                if b['dir'] == upleft:
                    b['rect'].left -= movespeed
                    b['rect'].top -= movespeed
                    if b['dir']  == upright:
                        b['rect'].left += movespeed
                        b['rect'].top -= movespeed
