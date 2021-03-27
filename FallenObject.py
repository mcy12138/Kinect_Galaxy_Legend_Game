#this file creates a class which is fallen objects from hitting enemies, with different objects and different funuctions

import pygame
from RedEnemy import *
import random

class FallenObject(pygame.sprite.Sprite):
	def __init__(self,screen,enemy):
		super().__init__()
		self.time=0
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.enemy=enemy
		self.type=random.randint(1,5)# {1:heart, add live; 2: star, add score; 3: blade, reinforce more powerful weapon}
		if self.type==1:#image from https://www.pinterest.com/vexels/love-valentines-day/?lp=true
			self.image=pygame.transform.scale(pygame.image.load("images/heart1.png").convert_alpha(),(100,140))
		elif self.type==2:#image from https://www.pinterest.com/pin/406520303841311059/?lp=true
			self.image=pygame.transform.scale(pygame.image.load("images/star.png").convert_alpha(),(100,140))
		elif self.type==3:#image from https://warosu.org/tg/thread/43314614
			self.image=pygame.transform.scale(pygame.image.load("images/blade.png").convert_alpha(),(180,240))
		elif self.type>3:#image from https://twitter.com/AndroidMX
			self.image=pygame.transform.scale(pygame.image.load("images/Bomb1.png").convert_alpha(),(140,160))
		self.rect=self.image.get_rect()
		self.mask=pygame.mask.from_surface(self.image)
		self.rect.centerx=self.enemy.rect.centerx
		self.rect.centery=self.enemy.rect.centery
		


	def update(self):
		self.time+=1
		if self.time//50%2==0:
			self.rect.x+=5
		else:
			self.rect.x-=5
		if self.time//200%2==0:
			self.rect.y+=5
		else:
			self.rect.y-=5

	def draw(self):
		self.screen.blit(self.image, self.rect)

