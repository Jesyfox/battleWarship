import pygame

class Location(pygame.Rect):
	def __init__(self,left, top, width=30, height=30):
		super().__init__(left, top, width, height)
		self.color = (0,150,0)

		self.c_x, self.c_y = pygame.mouse.get_pos() #mouse cordinates

		if self.c_x >= (left) and self.c_x <= (left+width) and self.c_y >= top and self.c_y <= (top+height):
			#if cursor inside rectangle then:
			self.color = (150,0,0)
		else:
			self.color = (0,150,0)	
		
