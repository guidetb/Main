import pygame
import random
from pygame.locals import *

class Army(object):

    def __init__(self, pos):
        (self.x, self.y) = pos
        
        self.image = pygame.image.load("soldier.png")

    def getX(self):
        return int(self.x)

    def getY(self):
        return int(self.y)

    def move_left(self):
        self.x -= 8
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += 8
        if self.x > 750:
            self.x = 750
   
    
    def render(self, surface):
        pos = (int(self.x),int(self.y))
        surface.blit(self.image,pos)

class EnemyBot(object):
    

    def __init__(self, pos):
        (self.x, self.y) = pos
        self.random = random
        self.image = pygame.image.load("zombie.png")

    def movement(self):
        self.y += random.randrange(3,5,1)


    #def  wrapup(self):
     #   self.random = random
      #  if self.y > 620:
       #     self.y = random.randrange(-300,-100,50) 
            
        
    
    def render(self, surface):
        pos = (int(self.x),int(self.y))
        surface.blit(self.image,pos)
        

class Bullet(object):

    
    def __init__(self, pos, speed):
        self.x = pos[0]
        self.y = pos[1]
        (self.vx, self.vy) = speed 
        self.image = pygame.image.load("Bullet.png")
    
    def getY(self):
        return self.y 

        

    def  bulletmove(self):
        
        self.x += self.vx
        self.y += self.vy

    def setposbullet(self, x, y):
        self.x = x
        self.y = y

    def render(self, surface):
        pos = (int(self.x),int(self.y))
        surface.blit(self.image,pos)
        

    
