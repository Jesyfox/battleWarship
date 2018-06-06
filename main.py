import pygame, sys, copy

from options import *
import Objects
import Bot

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Warship battle!")

def game_update(obj):
    for Area_Row in obj:
        for Area_block in Area_Row:
            Area_block.render()
            Area_block.refresh()

#--------------------------------------------Game initial--------------------------------------------------

Player_Area = Objects.draw_area(25, 25, 23, Objects.Location, screen) #Main player home grid
Enemy_Area = Objects.draw_area(25, 300, 23, Objects.Enem_Location, screen)

Objects.Battle_ship.sections = 4

#MAIN GAME: Placement
# --------------------Bot turn-------------------------------------------------:

while Objects.placement(Enemy_Area, EN_SECTIONS): # place the ships state Bot turn
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)

    if Objects.Connect_ships(Enemy_Area): # if stating, you can only build on sides
        Objects.placeability(False, Enemy_Area)

    #battle area initial
    game_update(Player_Area)
    game_update(Enemy_Area)

    #if dont have place ability:
    Objects.Crack_check(Enemy_Area)
        
    #Bot placing logic
    try:
        Bot.random_build(Enemy_Area)
    except IndexError: #if all done, stop
        break

    pygame.display.flip()

Objects.Battle_ship.sections = 4 # first ship init

if DEBUG:print('Place the first ship!(ship init)')

# -------------------Player turn---------------------------------------------:

while Objects.placement(Player_Area,SECTIONS): # place the ships state
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)

    if Objects.Connect_ships(Player_Area): # if stating, you can only build on sides
        Objects.placeability(False, Player_Area)

    #battle area initial
    game_update(Player_Area)
    game_update(Enemy_Area)

    #if dont have place ability:
    Objects.Crack_check(Player_Area)

    if DEBUG:
        try:
            Bot.random_build(Player_Area)
        except IndexError: #if all done, stop
            break

    pygame.display.flip()

if DEBUG:print('End of placement')

#MAIN GAME: Battle

Objects.battle_state(Player_Area)
Objects.battle_state(Enemy_Area)

print(Player_Area[4][2].state)

while True: # place the ships state
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)

    #battle area initial
    game_update(Player_Area)
    game_update(Enemy_Area)

    pygame.display.flip()