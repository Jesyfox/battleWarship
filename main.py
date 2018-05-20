import pygame, sys

from options import *
import Objects
pygame.init()

def game_update(obj):
    for Area_Row in obj:
        for Area_block in Area_Row: (Area_block.render(),Area_block.refresh())
          

def placement():
    '''func that count ships and sections '''
    ship_count = 1

    try:
        if Objects.Battle_ship.sections == 0: # new ship  
            Objects.Battle_ship.sections = SECTIONS.pop(-1) #send count information to Ship class
            ship_count =+ 1

            #make ship done and lock areas around:
            Objects.make_old(Player_Area)
            #Objects.make_old(Enemy_Area)

            #new ship init
            Objects.placeability(True, Player_Area)
            #Objects.placeability(True, Enemy_Area)
            
            
            if DEBUG:print('Ship number',ship_count,'with:',Objects.Battle_ship.sections,'sections')
            

        return True
    except IndexError: # when placement is done:
        if DEBUG:print('End of Placement, SECTIONS:',SECTIONS)
        return False

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Warship battle!")

Player_Area = Objects.draw_area(25, 25, 23, Objects.Location, screen) #Main player home grid
Enemy_Area = Objects.draw_area(25, 300, 23, Objects.Enem_Location, screen)

Objects.Battle_ship.sections = SECTIONS.pop(-1) # first ship init
if DEBUG:print('Place the first ship!(ship init)')

#MAIN GAME

while placement(): # place the ships state
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)

    if Objects.Connect_ships(Player_Area): # if stating, you can only build on sides
        Objects.placeability(False, Player_Area)
    if Objects.Connect_ships(Enemy_Area): # if stating, you can only build on sides
        Objects.placeability(False, Enemy_Area)

    #battle area initial
    game_update(Player_Area)
    game_update(Enemy_Area)

    pygame.display.flip()

if DEBUG:print('End.')

