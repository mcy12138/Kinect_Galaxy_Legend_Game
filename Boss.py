#this file is the class of the boss

import pygame
from Gameobject import *
import random

class Boss(pygame.sprite.Sprite):
	def __init__(self,screen):
		super().__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		#image from http://millionthvector.blogspot.com/
		self.image=pygame.transform.scale(pygame.image.load("images/bossPro.png").convert_alpha(),(500,500))
		self.HP=12000
		self.rect=self.image.get_rect()
		self.mask=pygame.mask.from_surface(self.image)
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=0
		self.alive=True
		self.score=12138

	def draw(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.rect.top<0:
			self.rect.y+=5