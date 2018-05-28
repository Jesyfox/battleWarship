import pygame, sys, copy

from options import *
import Objects
pygame.init()

def game_update(obj):
    for Area_Row in obj:
        for Area_block in Area_Row:
            Area_block.render()
            Area_block.refresh()

def placement():
    '''func that count ships and sections
    Works like bool element in While loop in build stage '''
    try:
        if Objects.Battle_ship.sections == 0: # new ship  
            Objects.Battle_ship.sections = SECTIONS.pop(-1) #send count information to Ship class
            #so when i build a ship, class will know how many sections

            #make ship done and lock areas around:
            Objects.make_old(Player_Area)
            #Objects.make_old(Enemy_Area)

            #new ship init
            Objects.placeability(True, Player_Area)
            #Objects.placeability(True, Enemy_Area)
            
            
            if DEBUG:print('Ship with:',Objects.Battle_ship.sections,'sections')
            

        return True
    except IndexError: # when placement is done:
        if DEBUG:print('End of Placement, SECTIONS:',SECTIONS)
        sections_counter = 0
        return False

#--------------------------------------------Game initial--------------------------------------------------
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Warship battle!")

Player_Area = Objects.draw_area(25, 25, 23, Objects.Location, screen) #Main player home grid
Enemy_Area = Objects.draw_area(25, 300, 23, Objects.Enem_Location, screen)

loop_counter = 0

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

    #if dont have place ability:
    if Objects.place_check(Player_Area):
        #then block unbuildible places
        loop_counter += 1
        if loop_counter == 5: #wait 5 ticks after detect, then do stuff
            if DEBUG:print('Unbuildible zone detect!\nrestart ship placing...')
            Objects.fix_defect(Player_Area) # close unbuildable zone
            Objects.placeability(True, Player_Area)# restart build a ship
            Objects.Battle_ship.sections += Objects.ship_couner(Player_Area) # restart secton counter
            loop_counter = 0

    pygame.display.flip()

if DEBUG:print('End.')

