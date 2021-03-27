#this file is the class of the info button 

import pygame

class Info(object):
	def __init__(self,screen,name):
		self.screen=screen
		self.name=name
		self.screen_rect = screen.get_rect()
		self.width=370
		self.height=120
		self.bgColor=(255,51,51)
		self.textColor=(255,255,255)
		self.font=pygame.font.SysFont("constantia", 70)
		#mediate the button at the center
		self.rect=pygame.Rect(0, 0, self.width, self.height)
		self.rect.center=(750,800)
		#self.rect.center = self.screen_rect.center
		self.prep_msg(name)

	def prep_msg(self, name):
		self.msg_image=self.font.render(name, True, self.textColor,
			self.bgColor)
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center

	def draw(self):
		self.screen.fill(self.bgColor,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)