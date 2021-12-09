# Simple Animation with Pygame, Julian Guevara, 12/09/21, 2:44pm, v0.3

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