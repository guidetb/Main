import pygame
from pygame.locals import *
import random

from elements import Player
from elements import Zombie
import gamelib

class KILLER(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')

    def __init__(self):
        super(KILLER, self).__init__('Runner', KILLER.WHITE)
        self.player = Player((660,250))
        self.random = random
        self.zombies = []
        for i in range(0,5):
                    zombie = Zombie((random.randrange(-100,150,50),(i*120)+5))
                    self.zombies.append(zombie)

    def init(self):
        super(KILLER, self).init()

    def update(self):
        if self.is_key_pressed(K_UP):
            self.player.move_up()
        elif self.is_key_pressed(K_DOWN):
            self.player.move_down()
        for zombie in self.zombies :
                    zombie.move()

    def render(self, surface):
        self.player.render(surface)
        for zombie in self.zombies :
                    zombie.render(surface)

def main():
    game = KILLER()
    game.run()


if __name__ == '__main__':
    main()
