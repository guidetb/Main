import pygame
from pygame.locals import *
import random

class Player(object):
	def __init__(self, pos):
                (self.x, self.y) = pos
		self.random = random
		self.player = pygame.image.load("soldier.png")
		

	def move_up(self):
		self.y -= 5
		
	def move_down(self):
		self.y += 5
		

	def render(self, surface):
		pos = (int(self.x),int(self.y))
		
		surface.blit(self.player, pos)

class Zombie(object):
	def __init__(self, pos):
		(self.x, self.y) = pos
		
		self.zombie = pygame.image.load("zombie.png")
		

	def move(self):
		self.x += 2
		if (self.x > 900):
                        self.x = -300
                        self.x = random.randrange(-100,150,50)
		

	def render(self, surface):
		pos = (int(self.x),int(self.y))
		
		surface.blit(self.zombie, pos)
		
		

