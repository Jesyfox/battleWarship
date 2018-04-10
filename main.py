import pygame, sys

from options import *
import Objects
pygame.init()

screen = pygame.display.set_mode(SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)


    Area = Objects.Location(HEIGHT/2,WIDTH/2)
    pygame.draw.rect(screen,Area.color,Area)

    pygame.display.flip()