#My First PyGame, Julian Guevara, 11/29/21 2:25pm, v0.3

import pygame, sys
from pygame.locals import *

#Start Pygame
pygame.init()

#setup our window. 1
windowSurface = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Hello, world!')

# Setup Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)