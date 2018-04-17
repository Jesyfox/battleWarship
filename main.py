import pygame, sys

from options import *
import Objects
pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Warship battle!")

Player_Area = Objects.draw_area(25, 25, 23, Objects.Location, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)

    #battle area initial
    for Area_block in Player_Area: Area_block.render()

    pygame.display.flip()
