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

if DEBUG:
    print('Debug state:\n 1 - Player placement\n 2 - Bot placement')
    Chose = input('Chose:')
    if Chose == '1':
        Objects.Battle_ship.sections = 4 # first ship init

        if DEBUG:print('Place the first ship!(ship init)')

        #MAIN GAME
        #STATE #1
        #Bot.click(1,10)

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

            pygame.display.flip()

        if DEBUG:print('End.')
        Chose = '2'

    if Chose == '2':

        Objects.Battle_ship.sections = 4

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

            Bot.click(Enemy_Area,1,10)

            pygame.display.flip()
        Chose = '1'


