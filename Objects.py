import pygame

class Location(object):
    """Piece of battle area class
    State 1: Placing time"""
    def __init__(self, x, y, width, height, screen, state):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.color = (10,10,120)
        self.health_status = False
        self.state = state
        self.place_ability = True

    def get_pos(self):
    	return (self.x, self.y)

    def place_ship(self, sections=1):
        '''func that places a ship, duh'''
        if self.place_ability:
            self.ship = Battle_ship(sections)

            self.health_status = True
            self.ship_x = self.x+int(self.width/2)
            self.ship_y = self.y+int(self.height/2)
            self.place_ability = False

    def refresh(self):
        '''func that makes logic'''
        if pygame.mouse.get_pressed()[0] and self.insice_loc():
            self.place_ship()

    def render(self):
        '''function that doing stuff with visualisation'''
        self.c_x, self.c_y = pygame.mouse.get_pos()

        if self.insice_loc():
            self.color = (150,0,0)
        else:
            self.color = (10,10,120)
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.height, self.width])

        if self.health_status:
        	# i will draw a ship
        	pygame.draw.circle(self.screen, self.ship.color, (self.ship_x, self.ship_y), self.ship.radius)

    def insice_loc(self):
    	'''if inside the location:'''
    	if self.c_x >= (self.x) and self.c_x <= (self.x+self.width) and self.c_y >= self.y and self.c_y <= (self.y+self.height):
    		return True
    	else:
    		return False



class Battle_ship(object):
    '''class that contains ship data'''
    def __init__(self,sections):
        self.sections = sections
        self.radius = 5
        self.color = (100,100,0)
    

def draw_area(horiz, vertic, step, obj, screen):
    """func draws area grid with starting coordinates"""
    start_h = horiz
    start_w = vertic
    Area = []
    for i in range(0,10):
        Area.append(obj(start_w, start_h, 20, 20, screen, "1"))
        for j in range(0,10):
            start_w += step
            Area.append(obj(start_w, start_h, 20, 20, screen, "1"))
        start_w = vertic
        start_h += step
    return Area

