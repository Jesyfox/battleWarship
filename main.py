import pygame, sys

from options import *
import Objects
pygame.init()

def game_update():
    for Area_block in Player_Area: Area_block.render()
    for Area_block in Player_Area: Area_block.refresh()

def Connect_ships():
    index = list(range(1,110))

    for i in index:
        if Player_Area[i].health_status and Player_Area[i-1].health_status:
            Player_Area[i].ship.connect_Left = True
            Player_Area[i-1].ship.connect_Right = True

        if Player_Area[i].health_status and Player_Area[i+1].health_status:
            Player_Area[i+1].ship.connect_Left = True
            Player_Area[i].ship.connect_Right = True

def placement():
    '''func that count ships and sections and combine them'''
    try:
        if Objects.Battle_ship.sections == 0: # new ship
            #print('new ship',SECTIONS[-1])   
            Connect_ships()
            Objects.Battle_ship.sections = SECTIONS.pop(-1)

        return True
    except IndexError:
        return False

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Warship battle!")

Player_Area = Objects.draw_area(25, 25, 23, Objects.Location, screen)

Objects.Battle_ship.sections = SECTIONS.pop(-1) # first ship init

while placement(): # place the ships state
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)


    #battle area initial
    game_update()

    pygame.display.flip()
