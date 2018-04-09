import pygame, sys

from options import *
pygame.init()

screen = pygame.display.set_mode(SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)


    pygame.draw.rect(screen, GREEN, [HEIGHT/2, WIDTH/2, BOX_SIZE, BOX_SIZE])


    pygame.display.flip()