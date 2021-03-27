#this file is the Kinect control part of the game: update changes observed by Kinect; can co-exist with keyboard

import pygame
from pykinect2 import PyKinectV2, PyKinectRuntime
from pykinect2.PyKinectV2 import *
import ctypes
import _ctypes
import sys
import math
from PlayerFighter import *
from Bomb import *
from GalaxyLegend import *

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

class KinectUpdate(object):
    def __init__(self,screen,PlayerFighter,PygameGame):
        self.playerFighter=PlayerFighter
        self.PygameGame=PygameGame
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body)
        self.bodies=None
        self.frame_surface=pygame.Surface((self.kinect.color_frame_desc.Width,self.kinect.color_frame_desc.Height),0,32)
        self.cur_right_hand_y=0
        self.cur_right_hand_x=0
        self.cur_left_hand_y=0
        self.cur_left_hand_x=0
        self.prev_right_hand_y=0
        self.prev_right_hand_x=0
        self.prev_left_hand_y=0
        self.prev_left_hand_x=0
        self.dx=0
        self.dy=0
        self.circle=[None]*20
        self.count=0



    def update(self):
        if self.kinect.has_new_color_frame():
            self.bodies=self.kinect.get_last_body_frame()
            if self.bodies is not None:
                for i in range(0,self.kinect.max_body_count):
                    body=self.bodies.bodies[i]
                    if not body.is_tracked:
                        continue

                    joints=body.joints
                    if joints[PyKinectV2.JointType_HandRight].TrackingState==PyKinectV2.TrackingState_Tracked:
                        self.cur_right_hand_y=joints[PyKinectV2.JointType_HandRight].Position.y
                        self.cur_right_hand_x=joints[PyKinectV2.JointType_HandRight].Position.x
                    if joints[PyKinectV2.JointType_HandLeft].TrackingState==PyKinectV2.TrackingState_Tracked:
                        self.cur_left_hand_x=joints[PyKinectV2.JointType_HandLeft].Position.x
                        self.cur_left_hand_y=joints[PyKinectV2.JointType_HandLeft].Position.y
                        self.circle.append((self.cur_left_hand_x,self.cur_left_hand_y))
                        self.circle.pop(0)



                    self.dx=self.cur_right_hand_x-self.prev_right_hand_x
                    self.dy=self.cur_right_hand_y-self.prev_right_hand_y

                    self.prev_right_hand_x=self.cur_right_hand_x
                    self.prev_right_hand_y=self.cur_right_hand_y

        '''if self.kinect.has_new_color_frame():
            frame=self.kinect.get_last_color_frame()
            #self.draw_color_frame(frame,self.frame_surface)
            frame=None'''

        self.playerFighter.rect.centerx+=self.dx*1500                  
        self.playerFighter.rect.centery-=self.dy*1000
        

        if self.playerFighter.rect.bottom>self.screen_rect.bottom:
            self.playerFighter.rect.bottom=self.screen_rect.bottom
        if self.playerFighter.rect.top<0:
            self.playerFighter.rect.top=0
        if self.playerFighter.rect.left<0:
            self.playerFighter.rect.left=0
        if self.playerFighter.rect.right>self.screen_rect.right:
            self.playerFighter.rect.right=self.screen_rect.right
        if self.cur_left_hand_y>=0.1:
            self.playerFighter.fireByKC=True
        else:
            self.playerFighter.fireByKC=False

        if not None in self.circle:
            sumx,sumy=0, 0
            for point in self.circle:
                sumx+=point[0]
                sumy+=point[1]
            cx=sumx/20
            cy=sumy/20
            radius=distance(self.circle[0][0],self.circle[0][1],cx,cy)
            
            flag = True
            for point in self.circle:
                d=distance(point[0],point[1],cx,cy)
                
                if d>radius*2 or d<radius*0.5 or radius<0.2:
                    flag = False
                    break
            if flag:
                if self.playerFighter.bombs>0:
                    self.playerFighter.bombs-=1
                    self.circle=[None]*20
                    newBomb=Bomb(self.screen)
                    self.PygameGame.bombs.add(newBomb)



