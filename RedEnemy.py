#this file is the class of enemies in the game

import pygame
from GalaxyLegend import *
from Gameobject import *
import random
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

class RedEnemy(pygame.sprite.Sprite):
	def __init__(self,screen,playerFighter):
		super().__init__()
		self.screen=screen
		self.time=0
		self.playerFighter=playerFighter
		self.angle=0
		self.type=random.randint(1,6)
		if self.type==1 or self.type==2 or self.type==3:
			#image from https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwiTpID2-vbXAhWpS98KHTz3B9YQjhwIBQ&url=https%3A%2F%2Fwww.123rf.com
			self.image=pygame.transform.scale(pygame.image.load("images/Enemy1Pro.png").convert_alpha(),(70,70))
			self.HP=100
			self.score=127
		elif self.type==4 or self.type==5:#image from http://wiki.bravofleet.com/index.php?title=Arrow_class
			self.image=pygame.transform.scale(pygame.image.load("images/Enemy2Pro.png").convert_alpha(),(100,170))
			self.HP=350
			self.score=364
		elif self.type==6:#image from https://www.pinterest.com/pin/308778118172104144/?lp=true
			self.image=pygame.transform.scale(pygame.image.load("images/Enemy3Pro.png").convert_alpha(),(80,150))
			self.HP=100
			self.score=256


		self.rect=self.image.get_rect()
		#https://www.youtube.com/watch?v=Dspz3kaTKUg
		#get mask object
		self.mask=pygame.mask.from_surface(self.image)
		self.screen_rect=screen.get_rect()
		self.rect.x=random.randint(0,self.screen_rect.width-self.rect.width)
		self.rect.top=self.screen_rect.top
		'''self.rect.x=self.rect.width
		self.rect.y=self.rect.height'''
		self.alive=True

	def draw(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		self.time+=1
		if self.type==1 or self.type==2 or self.type==3: # the red enemy
			if self.time//70%2==0:
				self.rect.x+=5
			else:
				self.rect.x-=5
			self.rect.y+=6
		elif self.type==4 or self.type==5: # the blue enemy
			self.rect.y+=3
		elif self.type==6:
			cx=self.playerFighter.rect.centerx
			cy=self.playerFighter.rect.centery
			#d=distance(self.rect.centerx,self.rect.centery,cx,cy)
			if self.rect.centerx-cx!=0 and self.time%20==1:
				self.angle=math.tan((self.rect.centery-cy)/(self.rect.centerx-cx))
			self.rect.centerx+=10*math.cos(self.angle)
			self.rect.centery+=5
			

		