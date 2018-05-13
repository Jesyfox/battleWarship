import pygame, sys

from options import *
import Objects
pygame.init()

def game_update():
    for Area_Row in Player_Area:
        for Area_block in Area_Row: (Area_block.render(),Area_block.refresh())

def Connect_ships():
    Ten = list(range(0,10))

    for j in Ten:
        for i in Ten:
            #if left and right are neighbours - connect it
            if Player_Area[j][i].health_status and Player_Area[j-1][i].health_status:
                Player_Area[j][i].ship.connect_Left = True
                Player_Area[j-1][i].ship.connect_Right = True
            # if Up and Down are neighbours - connetct it
            if Player_Area[j][i].health_status and Player_Area[j][i-1].health_status:
                Player_Area[j][i].ship.connect_Up = True
                Player_Area[j][i-1].ship.connect_Down = True
            try:
                Player_Area[0][i].ship.connect_Left = False
                Player_Area[-1][i].ship.connect_Right = False
            except AttributeError:
                continue
            try:
                Player_Area[i][0].ship.connect_Up = False
            except AttributeError:
                pass
            try:
                Player_Area[i][-1].ship.connect_Down = False
            except AttributeError:
                pass

def placement():
    '''func that count ships and sections '''
    try:
        if Objects.Battle_ship.sections == 0: # new ship
            #print('new ship',SECTIONS[-1])   
            Objects.Battle_ship.sections = SECTIONS.pop(-1) #send count information to Ship class
            Connect_ships()
        return True
    except IndexError:
        return False

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Warship battle!")

Player_Area = Objects.draw_area(25, 25, 23, Objects.Location, screen) #Main player home grid

Objects.Battle_ship.sections = SECTIONS.pop(-1) # first ship init

#MAIN GAME

while placement(): # place the ships state
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)


    #battle area initial
    game_update()

    pygame.display.flip()
