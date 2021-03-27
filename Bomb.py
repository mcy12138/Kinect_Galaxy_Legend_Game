import pygame
from Gameobject import *

class Bomb(pygame.sprite.Sprite):
	def __init__(self,screen):
		super().__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		# image from https://kyanshorney.deviantart.com/art/Energy-Beam-86086782
		self.image=pygame.transform.scale(pygame.image.load("images/ult1Cut.png").convert_alpha(),(350,1150))
		self.rect=self.image.get_rect()
		self.rect.x=0
		self.rect.top=0
		#self.rect.top = playerFighter.rect.top
		self.damage=1000

	def update(self):
		self.rect.x+=30
		if self.rect.x>self.screen_rect.right:
			self.kill()

	def draw(self):
		self.screen.blit(self.image, self.rect)