#My First PyGame, Julian Guevara, 12/1/21 2:00pm, v0.7

import pygame, sys
from pygame import draw
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
NOTRED = (2,140,155)

# Setup font.
basicFont = pygame.font.SysFont(None,48)

#Setup text.
text = basicFont.render('Hello, world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx= windowSurface.get_rect().centerx
textRect.centery= windowSurface.get_rect().centery

# Fill background color.
windowSurface.fill(white)

# Draw a polygon onto the screen.
pygame.draw.polygon(windowSurface, BLACK, ((146,0), (291,106), (236,277), (56,277), (0,106)))

# Draw lines on the screen
pygame.draw.line(windowSurface, GREEN, (60,60), (120,60), 4)
pygame.draw.line(windowSurface, BLUE, (256,300), (300,400), 3)
pygame.draw.line(windowSurface, NOTRED, (100,200), (140, 235), 2)

# Draw a circle.
pygame.draw.circle(windowSurface, RED, (300, 50), 20, 0)