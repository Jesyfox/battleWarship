import pygame, sys

from options import *
import Objects
pygame.init()

def game_update():
    for Area_Row in Player_Area:
        for Area_block in Area_Row: (Area_block.render(),Area_block.refresh())


def Connect_ships():
    '''func that draws connections on ships'''
    Ten = list(range(0,10))
    ship_check = False

    for j in Ten:
        for i in Ten:
            if Player_Area[j][i].health_status and Player_Area[j][i].ship.new_ship:
                ship_check = True
            #if left and right are neighbours - connect it
            if Player_Area[j][i].health_status and Player_Area[j-1][i].health_status:
                Player_Area[j][i].ship.connect_Left = True
                Player_Area[j-1][i].ship.connect_Right = True
            # if Up and Down are neighbours - connetct it
            if Player_Area[j][i].health_status and Player_Area[j][i-1].health_status:
                Player_Area[j][i].ship.connect_Up = True
                Player_Area[j][i-1].ship.connect_Down = True
            #disable side connections
            if Player_Area[0][i].health_status:Player_Area[0][i].ship.connect_Left = False
            if Player_Area[i][0].health_status:Player_Area[i][0].ship.connect_Up = False      
            if Player_Area[i][-1].health_status:Player_Area[i][-1].ship.connect_Down = False
            if Player_Area[-1][i].health_status:Player_Area[-1][i].ship.connect_Right = False
    return ship_check

def placeability(Bool):
    '''func that makes every location with placeability - False
    except arount section of the ship
    or reversed
    When - True ----- Disable all plasing except fresh ship'''

    Ten = list(range(0,10))

    #disable placeability in all area
    for Row in Ten:
        for Col in Ten:
            if not Player_Area[Row][Col].health_status:Player_Area[Row][Col].place_ability = Bool

    for Row in Ten:
        for Col in Ten:#if false, make placeability only around section of the ship
            if not Bool:
                if Player_Area[Row][Col].health_status and Player_Area[Row][Col].ship.new_ship:
                    try:
                        if not Row == 0:
                            if not Player_Area[Row-1][Col].health_status and not Player_Area[Row-1][Col].lock:
                                Player_Area[Row-1][Col].place_ability = not Bool #Left
                        if not Row == 9:
                            if not Player_Area[Row+1][Col].health_status and not Player_Area[Row+1][Col].lock:
                                Player_Area[Row+1][Col].place_ability = not Bool #Right

                        if not Player_Area[Row][Col-1].health_status and not Player_Area[Row][Col-1].lock:
                            Player_Area[Row][Col-1].place_ability = not Bool #Up
                        if not Player_Area[Row][Col+1].health_status and not Player_Area[Row][Col+1].lock:
                            Player_Area[Row][Col+1].place_ability = not Bool #Donw
                    except IndexError:
                        pass
            elif Bool: #if True disables areas around full ship
                if Player_Area[Row][Col].health_status and not Player_Area[Row][Col].ship.new_ship:
                    try:
                        if not Player_Area[Row-1][Col].health_status:Player_Area[Row-1][Col].lock = True
                    except IndexError:
                        pass #Left
                    try:
                        if not Player_Area[Row+1][Col].health_status:Player_Area[Row+1][Col].lock = True
                    except IndexError:
                        pass #Right
                    try:
                        if not Player_Area[Row][Col-1].health_status:Player_Area[Row][Col-1].lock = True
                    except IndexError:
                        pass #Up
                    try:
                        if not Player_Area[Row][Col+1].health_status:Player_Area[Row][Col+1].lock = True
                    except IndexError:
                        pass #Donw
                    try:
                        if not Player_Area[Row+1][Col+1].health_status:Player_Area[Row+1][Col+1].lock = True
                    except IndexError:
                        pass
                    try:
                        if not Player_Area[Row-1][Col-1].health_status:Player_Area[Row-1][Col-1].lock = True
                    except IndexError:
                        pass
                    try:
                        if not Player_Area[Row-1][Col+1].health_status:Player_Area[Row-1][Col+1].lock = True 
                    except IndexError:
                        pass
                    try:
                        if not Player_Area[Row+1][Col-1].health_status:Player_Area[Row+1][Col-1].lock = True 
                    except IndexError:
                        pass

def make_old():
    '''func that makes every ready ship  new_ship = False'''
    Ten = list(range(0,10))
    
    for Row in Ten:
        for Col in Ten:
            if Player_Area[Row][Col].health_status:Player_Area[Row][Col].ship.new_ship = False


          

def placement():
    '''func that count ships and sections '''
    ship_count = 1

    try:
        if Objects.Battle_ship.sections == 0: # new ship  
            Objects.Battle_ship.sections = SECTIONS.pop(-1) #send count information to Ship class
            ship_count =+ 1

            #make ship not new and lock areas around:
            make_old()
            placeability(True)
            
            
            if DEBUG:print('Ship number',ship_count,'with:',Objects.Battle_ship.sections,'sections')
            

        return True
    except IndexError: # when placement is done:
        if DEBUG:print('End of Placement, SECTIONS:',SECTIONS)
        return False

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Warship battle!")

Player_Area = Objects.draw_area(25, 25, 23, Objects.Location, screen) #Main player home grid

Objects.Battle_ship.sections = SECTIONS.pop(-1) # first ship init
if DEBUG:print('Place the first ship!(ship init)')

#MAIN GAME

while placement(): # place the ships state
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)

    if Connect_ships(): # if stating, you can only build on sides
        placeability(False)

    #battle area initial
    game_update()

    pygame.display.flip()

if DEBUG:print('End.')
