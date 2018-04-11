import pygame

class Location(pygame.Rect):
	"""Piece of battle area class"""


	def __init__(self, left, top, width=20, height=20): 
		super().__init__(left, top, width, height)
		self.color = (0,150,0)

		self.c_x, self.c_y = pygame.mouse.get_pos() #mouse cordinates

		if self.c_x >= (left) and self.c_x <= (left+width) and self.c_y >= top and self.c_y <= (top+height):
			#if cursor inside rectangle then:
			self.color = (150,0,0)
		else:
			self.color = (0,150,0)	
		

def draw_area(horiz, vertic,step, obj):
	"""func draws area grid with starting coordinates"""
    start_h = horiz
    start_w = vertic
    Area = []
    for i in range(0,10):
        Area.append(obj(start_w,start_h))
        for j in range(0,10):
            start_w += step
            Area.append(obj(start_w,start_h))
        start_w = vertic
        start_h += step
    return Area