import pygame
import random

class Explosion(pygame.sprite.Sprite):
    @staticmethod
    def init():
        choice=random.randint(1,5)
        #get ideas from https://www.youtube.com/watch?v=xa6kpf_CTzM
        if choice==1:# image from https://www.pinterest.com/pin/487373990902211838/?lp=true
            image=pygame.transform.scale(pygame.image.load('images/Explosion2.png'),(550,550))
            rows, cols=5,5
            width, height =image.get_size()
            cellWidth, cellHeight=width/cols, height/rows
            Explosion.frames=[]
            for i in range(rows):
                for j in range(cols):
                    subImage = image.subsurface(
                        (j * cellWidth, i * cellHeight, cellWidth, cellHeight))
                    Explosion.frames.append(subImage)


        elif choice==2:
            image=pygame.transform.scale(pygame.image.load('images/Explosion3.png'),(500,500))
            rows, cols = 4, 4
            width, height=image.get_size()
            cellWidth, cellHeight=width/cols, height/rows
            Explosion.frames =[]
            for i in range(rows):
                for j in range(cols):
                    subImage = image.subsurface(
                        (j * cellWidth, i * cellHeight, cellWidth, cellHeight))
                    Explosion.frames.append(subImage)


        elif choice==3 or choice==4 or choice==5:
            image=pygame.transform.scale(pygame.image.load('images/Explosion4.png'),(700,700))
            rows, cols=4,4
            width,height = image.get_size()
            cellWidth, cellHeight=width / cols, height / rows
            Explosion.frames=[]
            for i in range(rows):
                for j in range(cols):
                    subImage = image.subsurface(
                        (j * cellWidth, i * cellHeight, cellWidth, cellHeight))
                    Explosion.frames.append(subImage)


        #music from https://www.freesoundeffects.com/free-sounds/explosion-10070/
        sound=pygame.mixer.Sound("Explosion+3.wav")
        sound.set_volume(0.3)
        sound.play()


    def __init__(self, x, y, screen):
        super(Explosion, self).__init__()
        Explosion.init()
        '''self.sound=pygame.mixer.Sound("explosion-02.wav")
        self.sound.set_volume(0.5)'''
        self.screen=screen
        self.x, self.y = x, y
        self.frame = 0
        self.frameRate = 10
        self.aliveTime = 0

        self.updateImage()

    def updateImage(self):
        self.image = Explosion.frames[self.frame]
        w, h = self.image.get_size()
        self.rect = pygame.Rect(self.x - w / 2, self.y - h / 2, w, h)

    def update(self, dt):
        self.aliveTime += dt
        self.frame = self.aliveTime // (1000 // self.frameRate)
        if self.frame < len(Explosion.frames):
            self.updateImage()
        else:
            self.kill()

    def draw(self):
        self.screen.blit(self.image, self.rect)
