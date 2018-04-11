import pygame, sys

from options import *
import Objects
pygame.init()

screen = pygame.display.set_mode(SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)

    #battle area drawing
    Player_Area = Objects.draw_area(25, 25, 23, Objects.Location)
    Enemy_Area = Objects.draw_area(25,350,23,Objects.Location)

    for i in range(len(Player_Area)): #Fill with the color logic
        pygame.draw.rect(screen,Player_Area[i].color,Player_Area[i])
        pygame.draw.rect(screen,Enemy_Area[i].color,Enemy_Area[i])

    pygame.display.flip()