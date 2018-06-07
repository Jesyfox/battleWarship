import pygame
from options import *

loop_counter = 0

class Location(object):
    """Piece of battle area class
    State 1: Placement time
    State 2: Battle time"""
    def __init__(self, x, y, width, height, screen, state):
        #location pos
        self.x = x
        self.y = y
        #location size
        self.width = width
        self.height = height
        #screen attachment
        self.screen = screen
        #duh
        self.color = (10,10,120)
        #ship placemanet
        self.health_status = False
        self.place_ability = True
        #battle state variables
        self.was_shot = False
        #state of the game
        self.state = state
        self.lock = False

    def get_pos(self):
        return (self.x, self.y)

    def place_ship(self):
        '''func that places a ship, duh'''
        if self.place_ability:
            self.ship = Battle_ship(x=self.x, y=self.y,height=self.height, width=self.width, screen=self.screen)
            
            Battle_ship.sections -= 1
            self.health_status = True
            self.place_ability = False

    def refresh(self):
        '''func that makes logic'''

        if self.lock: #When True, you cant do stuff
            self.place_ability = False

        if pygame.mouse.get_pressed()[0] and self.insice_loc() and self.place_ability: #mouse logic
            self.click()

    def render(self):
        '''function that doing stuff with visualisation'''
        if self.insice_loc():
            self.color = (150,0,0)
        else:
            self.color = (10,10,120)
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.height, self.width])

        if self.health_status:
            # i will draw a ship
            self.ship.draw()

        #draw place ability
        if not self.health_status and self.place_ability and self.state is '1': # Green circle
            pygame.draw.circle(self.screen, (0,150,0), (self.x+10,self.y+10), 3)

        #draw place disability
        if not self.health_status and not self.place_ability and self.state is '1': # Red circle
            pygame.draw.circle(self.screen, (150,0,0), (self.x+10,self.y+10), 3)

        #draw 'X' if 'was_shot'
        if self.was_shot:
            pygame.draw.line(self.screen, (150,150,150), (self.x, self.y), (self.x + self.width, self.y + self.height), 2)
            pygame.draw.line(self.screen, (150,150,150), (self.x + self.width, self.y), (self.x, self.y + self.height), 2)

    def insice_loc(self):
        '''if cursor inside the location:'''
        self.c_x, self.c_y = pygame.mouse.get_pos()
        if self.c_x >= (self.x) and self.c_x <= (self.x+self.width) and self.c_y >= self.y and self.c_y <= (self.y+self.height):
            return True
        else:
            return False

    def click(self):
        '''do stuff here if clicked'''
        #if its a placement state:
        if self.state is "1":
            self.place_ship()
        elif self.state is "2":
            #self.get_shot()
            #bot will do it another way
            pass

    def get_shot(self):
        '''
        makes logic when this location is shot.
        if location has a ship, destroy him.
        makes location unshootable anymore.
        '''
        if not self.was_shot: # shoot location check
            self.was_shot = True
        else:
            if DEBUG:print('nothin here!\ntry another location!')


class Battle_ship(object):
    '''class that contains ship data'''
    def __init__(self, x, y, height, width, screen):
        self.radius = 7
        self.color = (100,100,0)
        self.new_ship = True
        #ship pos
        self.ship_x = x+int(width/2)
        self.ship_y = y+int(height/2)
        #screen attachment
        self.screen = screen
        #connections
        self.connect_Up = False
        self.connect_Down = False   
        self.connect_Left = False   
        self.connect_Right = False

    def draw(self):
        if not self.new_ship:
            self.color = (50,50,0)
        pygame.draw.circle(self.screen, self.color, (self.ship_x, self.ship_y), self.radius)

        #connections:
        if self.connect_Up:
            pygame.draw.rect(self.screen, self.color, [self.ship_x-3.5, self.ship_y-12, self.radius+1.5, self.radius+1.5])
        if self.connect_Down:
            pygame.draw.rect(self.screen, self.color, [self.ship_x-3.5, self.ship_y+3.5, self.radius+1.5, self.radius+1.5])
        if self.connect_Right:
            pygame.draw.rect(self.screen, self.color, [self.ship_x+3.5, self.ship_y-3.5, self.radius+1.5, self.radius+1.5])
        if self.connect_Left:
            pygame.draw.rect(self.screen, self.color, [self.ship_x-12, self.ship_y-3.5, self.radius+1.5, self.radius+1.5])

class Enem_Location(Location):
    """docstring for Enem_Location"""
    def __init__(self, x, y, width, height, screen, state):
        super(Enem_Location, self).__init__(x, y, width, height, screen, state)

    def refresh(self):
        '''func that makes logic'''
        if self.lock: #When True, you cant do stuff
            self.place_ability = False

        if pygame.mouse.get_pressed()[0] and self.insice_loc() and self.place_ability:
            #if its a placement state:
            if self.state == "1":
                #nothing to do
                if DEBUG:print('ENEMY AREA IS PRESSED!')
            if self.state == "2":
                self.click()

    def render(self):
        '''function that doing stuff with visualisation'''
        if self.insice_loc():
            self.color = (150,0,0)
        else:
            self.color = (10,10,120)
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.height, self.width])

        if DEBUG:
            if self.health_status:
                # i will draw a ship
                self.ship.draw()

            #draw place ability
            if not self.health_status and self.place_ability and self.state is '1': # Green circle
                pygame.draw.circle(self.screen, (0,150,0), (self.x+10,self.y+10), 3)

            #draw place disability
            if not self.health_status and not self.place_ability and self.state is '1': # Red circle
                pygame.draw.circle(self.screen, (150,0,0), (self.x+10,self.y+10), 3)

            #draw 'X' if 'was_shot'
            if self.was_shot:
                pygame.draw.line(self.screen, (150,150,150), (self.x, self.y), (self.x + self.width, self.y + self.height), 2)
                pygame.draw.line(self.screen, (150,150,150), (self.x + self.width, self.y), (self.x, self.y + self.height), 2)


    def click(self):
        '''do stuff here if clicked'''
        #if its a placement state:
        if self.state is "1":
            self.place_ship()
        elif self.state is "2":
            self.get_shot()
        



def draw_area(horiz, vertic, step, obj, screen):
    """func draws area grid with starting coordinates"""
    start_h = horiz
    start_w = vertic
    Area = []
    Cols = []
    for i in range(0,10):
        for i in range(0,10):
            Cols.append(obj(start_w, start_h, 20, 20, screen, '1'))
            start_h += step
        Area.append(Cols)
        Cols = []
        start_h = horiz
        start_w += step
    return Area

def Connect_ships(obj):
    '''func that draws connections on ships'''
    Ten = list(range(0,10))
    ship_check = False

    for j in Ten:
        for i in Ten:
            if obj[j][i].health_status and obj[j][i].ship.new_ship:
                ship_check = True
            #if left and right are neighbours - connect it
            if obj[j][i].health_status and obj[j-1][i].health_status:
                obj[j][i].ship.connect_Left = True
                obj[j-1][i].ship.connect_Right = True
            # if Up and Down are neighbours - connect it
            if obj[j][i].health_status and obj[j][i-1].health_status:
                obj[j][i].ship.connect_Up = True
                obj[j][i-1].ship.connect_Down = True
            #disable side connections
            if obj[0][i].health_status:obj[0][i].ship.connect_Left = False
            if obj[i][0].health_status:obj[i][0].ship.connect_Up = False      
            if obj[i][-1].health_status:obj[i][-1].ship.connect_Down = False
            if obj[-1][i].health_status:obj[-1][i].ship.connect_Right = False
    return ship_check

def placeability(Bool,obj):
    '''func that makes every location with placeability - False
    except arount section of the ship
    or reversed
    When - True ----- Disable all plasing except fresh ship
    When - False ---- Disable all, except left,right,up and down'''

    Ten = list(range(0,10))

    #disable placeability in all area
    for Row in Ten:
        for Col in Ten:
            if not obj[Row][Col].health_status:obj[Row][Col].place_ability = Bool

    for Row in Ten:
        for Col in Ten:#if false, make placeability only around section of the ship
            if not Bool:
                if obj[Row][Col].health_status and obj[Row][Col].ship.new_ship:
                    try:
                        if not Row == 0:
                            if not obj[Row-1][Col].health_status and not obj[Row-1][Col].lock:
                                obj[Row-1][Col].place_ability = not Bool #Left
                        if not Row == 9:
                            if not obj[Row+1][Col].health_status and not obj[Row+1][Col].lock:
                                obj[Row+1][Col].place_ability = not Bool #Right

                        if not obj[Row][Col-1].health_status and not obj[Row][Col-1].lock:
                            if Col-1 < 0: # if index is [-1] pass it!
                                pass
                            else:
                                obj[Row][Col-1].place_ability = not Bool #Up
                        if not obj[Row][Col+1].health_status and not obj[Row][Col+1].lock:
                            obj[Row][Col+1].place_ability = not Bool #Donw
                    except IndexError:
                        pass
            elif Bool: #if True disables areas around full ship
                if obj[Row][Col].health_status and not obj[Row][Col].ship.new_ship:
                    try:
                        if Row-1 < 0:
                            pass
                        else:
                            if not obj[Row-1][Col].health_status:obj[Row-1][Col].lock = True
                    except IndexError:
                        pass #Left
                    try:
                        if not obj[Row+1][Col].health_status:obj[Row+1][Col].lock = True
                    except IndexError:
                        pass #Right
                    try:
                        if Col-1 < 0:
                            pass
                        else:
                            if not obj[Row][Col-1].health_status:obj[Row][Col-1].lock = True
                    except IndexError:
                        pass #Up
                    try:
                        if not obj[Row][Col+1].health_status:obj[Row][Col+1].lock = True
                    except IndexError:
                        pass #Donw
                    try:
                        if not obj[Row+1][Col+1].health_status:obj[Row+1][Col+1].lock = True
                    except IndexError:
                        pass #Right Down
                    try:
                        if Row-1 < 0 or Col-1 < 0:
                            pass
                        else:
                            if not obj[Row-1][Col-1].health_status:obj[Row-1][Col-1].lock = True
                    except IndexError:
                        pass #Up Left
                    try:
                        if Row-1 < 0:
                            pass
                        else:
                            if not obj[Row-1][Col+1].health_status:obj[Row-1][Col+1].lock = True 
                    except IndexError:
                        pass #Left Down
                    try:
                        if Col-1 < 0:
                            pass
                        else:
                            if not obj[Row+1][Col-1].health_status:obj[Row+1][Col-1].lock = True 
                    except IndexError:
                        pass #Left Up

def make_old(obj):
    '''func that makes every ready ship  new_ship = False'''
    Ten = list(range(0,10))
    
    for Row in Ten:
        for Col in Ten:
            if obj[Row][Col].health_status:obj[Row][Col].ship.new_ship = False

def place_check(obj):
    '''
    func that checks place ability on areas, if he cant fing it, raises error
    '''
    Ten = list(range(0,10))
    Place_list = []

    for Row in Ten:
        for Col in Ten:
            if obj[Row][Col].place_ability:
                Place_list.append(obj[Row][Col])
            else:
                pass

    if Place_list == []:
        return True
    else:
        return False


def fix_defect(obj):
    '''func detect not finished ship, deletes him and blocks defect places'''
    Ten = list(range(0,10))

    for Row in Ten:
        for Col in Ten:
            try:
                if obj[Row][Col].ship.new_ship:
                    obj[Row][Col].lock = True
                    obj[Row][Col].health_status = False
                    obj[Row][Col].placeability = False
                else:
                    pass
            except AttributeError:
                pass

def ship_couner(obj):
    '''func that count placed not finished new ships'''
    Ten = list(range(0,10))
    count = 0
    for Row in Ten:
        for Col in Ten:
            try:
                if obj[Row][Col].ship.new_ship:
                    count += 1
                else:
                    pass
            except AttributeError:
                pass
    return count

loop_counter = 0
def Crack_check(obj):
    '''func that find unbuildible places and block them'''
    global loop_counter
    if place_check(obj): # dont have space to build:
        loop_counter += 1
        if loop_counter == 5: #wait 5 ticks after detect, then do stuff:
            if DEBUG:print('Unbuildible zone detect!\nRestart ship placing...')
            fix_defect(obj) # close unbuildable zone
            placeability(True, obj)# restart build a ship
            Battle_ship.sections += ship_couner(obj) # restart secton counter
            loop_counter = 0 #restart counter

def placement(obj,sections_list):
    '''func that count ships and sections
    Works like bool element in While loop in build stage '''
    try:
        if Battle_ship.sections == 0: # new ship  
            if DEBUG: print('start pop ship!')
            Battle_ship.sections = sections_list.pop(-1) #send count information to Ship class
            #so when i build a ship, class will know how many sections

            #make ship done and lock areas around:
            make_old(obj)

            #new ship init
            placeability(True, obj)            
            
            if DEBUG:print('Ship with:',Battle_ship.sections,'sections')

            if Battle_ship.sections == 0:
                raise IndexError
            

        return True
    except IndexError: # when placement is done:
        placeability(False, obj) #Lock all
        if DEBUG:print('End of Placement, SECTIONS:',sections_list)
        return False

def battle_state(obj):
    '''func that chane state in class'''
    Ten = list(range(0,10))

    for Row in Ten:
        for Col in Ten:
            obj[Row][Col].state = "2"
            obj[Row][Col].lock = False
            obj[Row][Col].place_ability = True