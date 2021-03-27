#Created by Carl Yang 12/06/2017
#yufeiy3@andrew.cmu.edu
#No business use. All rights reserved.
#the main run function of my project; run this file to play the game

'''
pygame main run function cited from lecture notes, created by Lukas Peraza from 15112 pygame gitbook
A lot of ideas from https://www.pygame.org/news//pygame official website
https://www.pygame.org/news
'''
import pygame
from Gameobject import *
from PlayerFighter import *
from Bullet import *
from RedEnemy import *
from Button import *
from Explosion import *
from Bomb import *
from FallenObject import *
from BossBullet import *
from Boss import *
from Info import *
import math
import random
#Kinect import

#if you don't need a Kinect, comment the next 6 lines below!
from pykinect2 import PyKinectV2, PyKinectRuntime
from pykinect2.PyKinectV2 import *
from KinectControl import *
import ctypes
import _ctypes
import sys


class PygameGame(object):

    def init(self):
        #image from https://www.nature.com/articles/548288a
        self.bg=pygame.image.load("images/bg1.jpg").convert_alpha()
        #self.bg=pygame.transform.scale(bg,(500,800))
        self.time=0
        self.playButton=Button(self.screen,"PLAY")
        self.info=Info(self.screen,"info")
        self.playerFighter=PlayerFighter(self.screen)
        self.bullets=pygame.sprite.Group()
        self.enemies=pygame.sprite.Group()
        self.bombs=pygame.sprite.Group()
        self.fallenObjects=pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.gaming=False
        self.getBoss=True
        self.bossAlive=False
        self.win=False
        self.damage=0
        self.score=0
        self.showInfo=False
        

        #if you don't need a Kinect, comment the line below!
        self.KC=KinectUpdate(self.screen,self.playerFighter,self)

    def mousePressed(self, x, y):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.playButton.rect.collidepoint(mouse_x, mouse_y) and self.gaming==False and self.showInfo==False:
            self.init()
            self.gaming=True
        if self.info.rect.collidepoint(mouse_x, mouse_y) and self.gaming==False:
            self.showInfo=True

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        if keyCode==pygame.K_RIGHT:
            self.playerFighter.movingRight=True
        if keyCode==pygame.K_LEFT:
            self.playerFighter.movingLeft=True
        if keyCode==pygame.K_UP:
            self.playerFighter.movingUp=True
        if keyCode==pygame.K_DOWN:
            self.playerFighter.movingDown=True
        if keyCode==pygame.K_SPACE:
            self.playerFighter.fireByHand=True
        if keyCode==pygame.K_b and self.playerFighter.bombs>0 and self.gaming==True:
            self.playerFighter.bombs-=1
            newBomb=Bomb(self.screen)
            self.bombs.add(newBomb)
        if keyCode==pygame.K_i and self.gaming==False and self.showInfo==True:
            self.showInfo=False
                

    def keyReleased(self, keyCode, modifier):
        if keyCode==pygame.K_RIGHT:
            self.playerFighter.movingRight=False
        if keyCode==pygame.K_LEFT:
            self.playerFighter.movingLeft=False
        if keyCode==pygame.K_UP:
            self.playerFighter.movingUp=False
        if keyCode==pygame.K_DOWN:
            self.playerFighter.movingDown=False
        if keyCode==pygame.K_SPACE:
            self.playerFighter.fireByHand=False

        

    def timerFired(self, dt):
        if self.gaming==True:

            self.time+=1

            #use Kinect to control; keyboard still activated
            #if you don't need a Kinect, comment the line below!
            self.KC.update()

            self.playerFighter.update()
            

            #create enemies
            if self.score<5000:
                if self.time%70==0:
                    newEnemy=RedEnemy(self.screen,self.playerFighter)
                    self.enemies.add(newEnemy)
            elif self.score>=5000 and self.score<10000:
                if self.time%50==0:
                    newEnemy=RedEnemy(self.screen,self.playerFighter)
                    self.enemies.add(newEnemy)
            elif self.score>=10000 and self.score<15000:
                if self.time%30==0:
                    newEnemy=RedEnemy(self.screen,self.playerFighter)
                    self.enemies.add(newEnemy)
            elif self.score>=15000 and self.score<20000:
                if self.time%17==0:
                    newEnemy=RedEnemy(self.screen,self.playerFighter)
                    self.enemies.add(newEnemy)
            elif self.score>=20000 and self.score<25000:
                if self.time%10==0:
                    newEnemy=RedEnemy(self.screen,self.playerFighter)
                    self.enemies.add(newEnemy)
            elif self.score>=25000:
                if self.getBoss==True:
                    self.boss=Boss(self.screen)
                    #self.enemies.add(newEnemy)
                    self.enemies.add(self.boss)
                    self.getBoss=False
                    self.bossAlive=True
                if self.bossAlive==True and self.time%30==0:
                    newEnemy=BossBullet(self.screen,self.boss)
                    self.enemies.add(newEnemy)


            self.enemies.update()

            #handle different levels of bullets
            if self.playerFighter.fireByHand==True or self.playerFighter.fireByKC==True:
                if self.time%10==0:
                    if self.playerFighter.level==1:
                        newBullet=Bullet(self.screen,self.playerFighter,self.playerFighter.rect.centerx,self.playerFighter.rect.centery)
                        self.bullets.add(newBullet)
                    elif self.playerFighter.level==2:
                        newBullet1=Bullet(self.screen,self.playerFighter,self.playerFighter.rect.centerx-10,self.playerFighter.rect.centery)
                        newBullet2=Bullet(self.screen,self.playerFighter,self.playerFighter.rect.centerx+10,self.playerFighter.rect.centery)
                        self.bullets.add(newBullet1)
                        self.bullets.add(newBullet2)
                    elif self.playerFighter.level==3:
                        newBullet1=Bullet(self.screen,self.playerFighter,self.playerFighter.rect.centerx-8,self.playerFighter.rect.centery)
                        newBullet2=Bullet(self.screen,self.playerFighter,self.playerFighter.rect.centerx-16,self.playerFighter.rect.centery)
                        newBullet3=Bullet(self.screen,self.playerFighter,self.playerFighter.rect.centerx+8,self.playerFighter.rect.centery)
                        newBullet4=Bullet(self.screen,self.playerFighter,self.playerFighter.rect.centerx+16,self.playerFighter.rect.centery)
                        self.bullets.add(newBullet1)
                        self.bullets.add(newBullet2)
                        self.bullets.add(newBullet3)
                        self.bullets.add(newBullet4)
                    elif self.playerFighter.level>=4:
                        newBullet1=Bullet(self.screen,self.playerFighter,self.playerFighter.rect.centerx-5,self.playerFighter.rect.centery)
                        newBullet2=Bullet(self.screen,self.playerFighter,self.playerFighter.rect.centerx+5,self.playerFighter.rect.centery)
                        newBullet3=Bullet(self.screen,self.playerFighter,self.playerFighter.rect.centerx+15,self.playerFighter.rect.centery)
                        newBullet4=Bullet(self.screen,self.playerFighter,self.playerFighter.rect.centerx-15,self.playerFighter.rect.centery)
                        newBullet5=Bullet(self.screen,self.playerFighter,self.playerFighter.rect.centerx+25,self.playerFighter.rect.centery)
                        newBullet6=Bullet(self.screen,self.playerFighter,self.playerFighter.rect.centerx-25,self.playerFighter.rect.centery)
                        self.bullets.add(newBullet1)
                        self.bullets.add(newBullet2)
                        self.bullets.add(newBullet3)
                        self.bullets.add(newBullet4)
                        self.bullets.add(newBullet5)
                        self.bullets.add(newBullet6)


            self.bullets.update()

            self.bombs.update()


            #kill enemies that fly out of the screen
            for enemy in self.enemies.copy():
                if enemy.rect.top>=self.screen_rect.bottom or enemy.rect.right<=0 or enemy.rect.left>=self.screen_rect.right:
                    self.enemies.remove(enemy)

            #kill extra bullets that fly out of screen
            for bullet in self.bullets.copy():
                if bullet.rect.bottom<=0:
                    self.bullets.remove(bullet)

            #kill extra fallenObjects that fly out of screen
            for fallenObject in self.fallenObjects.copy():
                if fallenObject.rect.top>=self.screen_rect.bottom or fallenObject.rect.right<=0 or fallenObject.rect.left>=self.screen_rect.right\
                    or fallenObject.rect.bottom<=0:
                    self.fallenObjects.remove(fallenObject)

            self.explosions.update(dt)

            self.fallenObjects.update()

            #bullets hit enemy
            for enemy in pygame.sprite.groupcollide(self.enemies, self.bullets, False, True):
                for bullet in self.bullets:
                    self.damage=bullet.damage
                    break
                enemy.HP-=self.damage           
                if enemy.HP<=0:
                    self.score+=enemy.score
                    temp=random.randint(1,4)
                    if temp==1:
                        self.fallenObjects.add(FallenObject(self.screen,enemy))
                    self.explosions.add(Explosion(enemy.rect.x,enemy.rect.y,self.screen))
                    if isinstance(enemy,Boss):
                        self.win=True
                        self.gaming=False
                    self.enemies.remove(enemy)


            for enemy in pygame.sprite.groupcollide(self.enemies, self.bombs, False, False):
                for bomb in self.bombs:
                    self.bombDamage=bomb.damage
                    break
                if not isinstance(enemy,Boss):
                    enemy.HP-=self.bombDamage
                if enemy.HP<=0:
                    self.score+=enemy.score
                    temp=random.randint(1,3)
                    if temp==1:
                        self.fallenObjects.add(FallenObject(self.screen,enemy))
                    self.explosions.add(Explosion(enemy.rect.x,enemy.rect.y,self.screen))
                    if isinstance(enemy,Boss):
                        self.win=True
                        self.gaming=False
                    self.enemies.remove(enemy)


            #use mask type to check collison
            for enemy in self.enemies:
                if pygame.sprite.collide_mask(self.playerFighter, enemy):
                    self.explosions.add(Explosion(enemy.rect.x,enemy.rect.y,self.screen))
                    if not isinstance(enemy,Boss):
                        enemy.kill()
                    self.playerFighter.lives-=1
                    self.playerFighter.level=1
                    if self.playerFighter.lives<=0:
                        self.gaming=False
                    print("Oh! You are hit!")

            #use rect type to check collison
            '''if pygame.sprite.spritecollideany(self.playerFighter, self.enemies):
                self.enemies.remove(pygame.sprite.spritecollideany(self.playerFighter, self.enemies))
                self.playerFighter.lives-=1
                if self.playerFighter.lives<=0:
                    self.gaming=False
                print("Oh! You are hit!")
                #pygame.time.wait(500)''' 
            
            #get rewards if player hits any fallenObjects
            for fallenObject in self.fallenObjects:
                if pygame.sprite.collide_mask(self.playerFighter, fallenObject):
                    if fallenObject.type==1:
                        self.playerFighter.lives+=1
                    elif fallenObject.type==2:
                        self.score+=500
                    elif fallenObject.type==3:
                        self.playerFighter.level+=1
                    elif fallenObject.type==4 or fallenObject.type==5:
                        self.playerFighter.bombs+=1
                    fallenObject.kill()



    def redrawAll(self,screen):
        if self.gaming==True:
            self.playerFighter.draw()
            for enemy in self.enemies.sprites():
                enemy.draw()
            for bullet in self.bullets.sprites():
                bullet.draw()
            for bomb in self.bombs.sprites():
                bomb.draw()
            for explosion in self.explosions.sprites():
                explosion.draw()
            for fallenObject in self.fallenObjects.sprites():
                fallenObject.draw()

        elif self.win==True:#win, gaming is False
            if self.showInfo==True:
                Font=pygame.font.SysFont("Times New Roman", 30)
                Text=Font.render("Hello, welcome to the Galaxy Legend game!", 1, (255,255,255))
                self.screen.blit(Text, (50,150))
                Text=Font.render("In this game, you can drive a fighter and kill all enemies on the screen.", 1, (255,255,255))
                self.screen.blit(Text, (50,200))
                Text=Font.render("You can use arrow keys to move the fighter and press space to shoot.", 1, (255,255,255))
                self.screen.blit(Text, (50,250))
                Text=Font.render("You can also press 'b' to release a large, powerful bomb, with limited times.", 1, (255,255,255))
                self.screen.blit(Text, (50,300))
                Text=Font.render("Your lives left and bombs have are shown on the bottom-left corner.", 1, (255,255,255))
                self.screen.blit(Text, (50,350))
                Text=Font.render("When you hit an enemy, there's certain chance it drops a bonus object, go and get it!", 1, (255,255,255))
                self.screen.blit(Text, (50,400))
                Text=Font.render("You can also use Kinect to play: use you right hand to control the position of your fighter and raise your left hand to a certain ", 1, (255,255,255))
                self.screen.blit(Text, (50,450))
                Text=Font.render("height to shoot; use left hand to draw a large circle (not too small) to release a bomb.", 1, (255,255,255))
                self.screen.blit(Text, (50,500))
                Text=Font.render("There are three kinds of enemies in the game:", 1, (255,255,255))
                self.screen.blit(Text, (50,550))
                Text=Font.render("one goes vertically, another one goes zigzag movement, the third one is the most dangerous: ", 1, (255,255,255))
                self.screen.blit(Text, (50,600))
                Text=Font.render("It TRACKS WHERE YOU ARE!!! Just like a homing missile. Definitely be careful with it.", 1, (255,255,255))
                self.screen.blit(Text, (50,650))
                Text=Font.render("When your score reaches certain point, you will meet the Boss! Beat it and you win!", 1, (255,255,255))
                self.screen.blit(Text, (50,700))
                Text=Font.render("That's it. Happy playing!", 1, (255,255,255))
                self.screen.blit(Text, (50,750))
                Text=Font.render("Press 'i' to back to the menu", 1, (255,255,255))
                self.screen.blit(Text, (50,800))

            else:
                self.playButton.draw()
                self.info.draw()

                Font=pygame.font.SysFont("acaslonproregularopentype", 80)
                Text=Font.render("YOU WIN!", 1, (255,255,255))
                self.screen.blit(Text, (550,250))

        else:#die, gaming is False
            if self.showInfo==True:
                Font=pygame.font.SysFont("Times New Roman", 30)
                Text=Font.render("Hello, welcome to the Galaxy Legend game!", 1, (255,255,255))
                self.screen.blit(Text, (50,150))
                Text=Font.render("In this game, you can drive a fighter and kill all enemies on the screen.", 1, (255,255,255))
                self.screen.blit(Text, (50,200))
                Text=Font.render("You can use arrow keys to move the fighter and press space to shoot.", 1, (255,255,255))
                self.screen.blit(Text, (50,250))
                Text=Font.render("You can also press 'b' to release a large, powerful bomb, with limited times.", 1, (255,255,255))
                self.screen.blit(Text, (50,300))
                Text=Font.render("Your lives left and bombs have are shown on the bottom-left corner.", 1, (255,255,255))
                self.screen.blit(Text, (50,350))
                Text=Font.render("When you hit an enemy, there's certain chance it drops a bonus object, go and get it!", 1, (255,255,255))
                self.screen.blit(Text, (50,400))
                Text=Font.render("You can also use Kinect to play: use you right hand to control the position of your fighter and raise your left hand to a certain ", 1, (255,255,255))
                self.screen.blit(Text, (50,450))
                Text=Font.render("height to shoot; use left hand to draw a large circle (not too small) to release a bomb.", 1, (255,255,255))
                self.screen.blit(Text, (50,500))
                Text=Font.render("There are three kinds of enemies in the game:", 1, (255,255,255))
                self.screen.blit(Text, (50,550))
                Text=Font.render("one goes vertically, another one goes zigzag movement, the third one is the most dangerous: ", 1, (255,255,255))
                self.screen.blit(Text, (50,600))
                Text=Font.render("It TRACKS WHERE YOU ARE!!! Just like a homing missile. Definitely be careful with it.", 1, (255,255,255))
                self.screen.blit(Text, (50,650))
                Text=Font.render("When your score reaches certain point, you will meet the Boss! Beat it and you win!", 1, (255,255,255))
                self.screen.blit(Text, (50,700))
                Text=Font.render("That's it. Happy playing!", 1, (255,255,255))
                self.screen.blit(Text, (50,750))
                Text=Font.render("Press 'i' to back to the menu", 1, (255,255,255))
                self.screen.blit(Text, (50,800))

            else:    
                self.playButton.draw()
                self.info.draw()

                #draw game over
                Font=pygame.font.SysFont("acaslonproregularopentype", 80)
                Text=Font.render("Game Over!", 1, (255,255,255))
                self.screen.blit(Text, (550,250))

        #draw player's bombs left
        Font=pygame.font.SysFont("broadway", 30)
        Text=Font.render("Bombs: %d"%(self.playerFighter.bombs), 1, (220,20,60))
        self.screen.blit(Text, (19,900))


        #draw player's lives left
        Font=pygame.font.SysFont("broadway", 30)
        Text=Font.render("Lives: %d"%(self.playerFighter.lives), 1, (255,255,255))
        self.screen.blit(Text, (20,950))

        #draw highest score
        Font=pygame.font.SysFont("Algerian", 30)
        Text=Font.render("Highest Record: %d"%(self.HS), 1, (0,191,255))
        self.screen.blit(Text, (600,50))


        #draw scores
        Font=pygame.font.SysFont("Impact", 20)
        Text=Font.render("Score: %d"%(self.score), 1, (127,255,212))
        self.screen.blit(Text, (700,100))


    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=1600, height=1000, fps=50, title="Galaxy Legend"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (0, 0, 0)
        self.HS=0
        self.y=0
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen_rect=self.screen.get_rect()
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()

        #display background music
        pygame.mixer.init()
        #music from http://file3.data.weipan.cn.wscdns.com/17376349
        pygame.mixer.music.load("bgmusic.mp3")
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play(-1)

        playing = True
        while playing:
            #record the highest score
            if self.HS<self.score:
                self.HS=self.score
            #print(self.HS)
            
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            self.screen.fill(self.bgColor)


            #make bg constantly scrolling down
            #get ideas from https://www.youtube.com/watch?v=US3HSusUBeI
            self.rel_y=self.y%self.bg.get_rect().height
            self.screen.blit(self.bg,(0,self.rel_y-self.bg.get_rect().height))
            if self.rel_y>0:
                self.screen.blit(self.bg,(0,self.rel_y))
            self.y+=1
            
            #print(self.y)
            self.redrawAll(self.screen)
            
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()