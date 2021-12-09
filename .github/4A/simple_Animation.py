# Simple Animation with Pygame, Julian Guevara, 12/09/21, 2:19pm, v0.2

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

movespeed = 4
