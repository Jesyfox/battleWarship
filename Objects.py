import pygame

class Location(object):
    """Piece of battle area class
    State 1: Placement time"""
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
        #state of the game
        self.state = state

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
        if pygame.mouse.get_pressed()[0] and self.insice_loc():
            #if its a placement state:
            if self.state == "1":
                self.place_ship()
            #if its war stage:
            #fire!

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

    def insice_loc(self):
        '''if inside the location:'''
        self.c_x, self.c_y = pygame.mouse.get_pos()
        if self.c_x >= (self.x) and self.c_x <= (self.x+self.width) and self.c_y >= self.y and self.c_y <= (self.y+self.height):
            return True
        else:
            return False

class Battle_ship(object):
    '''class that contains ship data'''
    def __init__(self, x, y, height, width, screen):
        self.radius = 7
        self.color = (100,100,0)
        self.ship_x = x+int(width/2)
        self.ship_y = y+int(height/2)
        self.screen = screen
        self.connect_Up = False
        self.connect_Down = False	
        self.connect_Left = False	
        self.connect_Right = False

    def draw(self):
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


def draw_area(horiz, vertic, step, obj, screen):
    """func draws area grid with starting coordinates"""
    start_h = horiz
    start_w = vertic
    Area = []
    Cols = []
    for i in range(0,10):
        for i in range(0,10):
            Cols.append(obj(start_w, start_h, 20, 20, screen, "1"))
            start_h += step
        Area.append(Cols)
        Cols = []
        start_h = horiz
        start_w += step
    return Area
