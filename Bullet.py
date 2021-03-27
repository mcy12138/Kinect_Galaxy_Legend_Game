import pygame
from Gameobject import *
from PlayerFighter import *

class Bullet(pygame.sprite.Sprite):
	def __init__(self,screen,playerFighter,x,y):
		super().__init__()
		self.screen=screen
		#image from https://forums.spacebattles.com/threads/spacebattles-dimensional-clash-the-ic.282738/page-8
		self.image=pygame.transform.scale(pygame.image.load("images/Laser_BulletPro.png").convert_alpha(),(7,60))
		self.rect=self.image.get_rect()
		self.rect.centerx=x
		self.rect.centery=y
		self.rect.top = playerFighter.rect.top
		self.damage=50

	def update(self):
		self.rect.y-=20

	def draw(self):
		self.screen.blit(self.image, self.rect)
