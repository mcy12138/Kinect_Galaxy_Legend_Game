#this file is the class of enemies of created by the Boss

import pygame
from Gameobject import *
import random

class BossBullet(pygame.sprite.Sprite):
	def __init__(self,screen,boss):
		super().__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.boss=boss
		self.time=0
		#image from https://lovecraftianscience.wordpress.com/2016/04/17/the-arrival-of-the-insects-of-shaggai-part-1/
		self.image_orig =pygame.transform.scale(pygame.image.load("images/BossBullet1Cut.png").convert_alpha(),(100,80))
		self.image=self.image_orig.copy()
		self.rect = self.image.get_rect()
		self.rect.x=self.boss.rect.centerx
		self.rect.y=self.boss.rect.centery
		self.rot = 0
		self.rot_speed =10
		self.last_update = pygame.time.get_ticks()
		self.HP=300
		self.score=127
		self.dx=random.randrange(-10,10)
		self.dy=random.randrange(5,10)

	def update(self):
		self.rotate()
		self.rect.x+=self.dx
		self.rect.y+=self.dy
		

	def rotate(self):
		#get ideas from https://github.com/kidscancode/pygame_tutorials/blob/master/shmup/shmup-6.py
		now = pygame.time.get_ticks()
		if now - self.last_update > 50:
			self.last_update = now
			self.rot = (self.rot + self.rot_speed) % 360
			new_image = pygame.transform.rotate(self.image_orig, self.rot)
			old_center = self.rect.center
			self.image = new_image
			self.rect = self.image.get_rect()
			self.rect.center = old_center
			

	def draw(self):
		self.screen.blit(self.image, self.rect)