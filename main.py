import pygame, sys

from options import *
import Objects
pygame.init()

state_game = STATE1

def game_update():
    for Area_block in Player_Area: Area_block.render()
    for Area_block in Player_Area: Area_block.refresh()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Warship battle!")

Player_Area = Objects.draw_area(25, 25, 23, Objects.Location, screen)

while state_game == "1": # place the ships
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)

    #battle area initial
    game_update()

    pygame.display.flip()
