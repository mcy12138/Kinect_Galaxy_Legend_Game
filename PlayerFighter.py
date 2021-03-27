#this file is the class of the player's fighter

import pygame
import math
from Gameobject import *


class PlayerFighter(GameObject):
    	#PlayerFighter.fighterImage=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/Fighter1.png").convert_alpha(),(60,100)),-90)

    def __init__(self,screen):
        self.screen=screen
        #image from https://www.simpleplanes.com/a/x4Mu0s/Lockheed-Martin-F-22-Raptor
        self.image=pygame.transform.scale(pygame.image.load("images/Fighter1.png").convert_alpha(),(60,100))
        #self.image=pygame.image.load("images/Fighter1.png")
        self.rect=self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)
        self.screen_rect=screen.get_rect()
        #put the player on the bottom center of the screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.movingLeft=False
        self.movingRight=False
        self.movingUp=False
        self.movingDown=False

        #use hand to control keyboard to fire
        self.fireByHand=False

        #use Kinect detection to fire
        self.fireByKC=False
        self.lives=3
        self.bombs=3
        self.level=1

        

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.movingLeft==True and self.rect.left>0:
            self.rect.centerx-=10
        elif self.movingRight==True and self.rect.right<self.screen_rect.right:
            self.rect.centerx+=10
        elif self.movingUp==True and self.rect.top>0:
            self.rect.centery-=10
        elif self.movingDown==True and self.rect.bottom<self.screen_rect.bottom:
            self.rect.centery+=10



     



