import pygame
from pygame.locals import *

from elements import Ship,EnemyBot,Bullet
import gamelib
import random

class SpaceShipGame(gamelib.SimpleGame):
    
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    

    
    
    def __init__(self):
        super(SpaceShipGame, self).__init__('SpaceShip', SpaceShipGame.BLACK)
        self.ship = Ship((320,500))
        self.random = random
        self.bullets = []
        self.enemies = []
        self.reload = 0
        self.hp = 10
        self.score = 0
        self.game_over = False
        
        for i in range(0,5):
            enemy = EnemyBot((i*160,random.randrange(-400,-100,10)))
            self.enemies.append(enemy)
        for bullet in range(0,100):
            bullet = Bullet((-10,-400),(0,-7))
            self.bullets.append(bullet)
    
    def init(self):
        super(SpaceShipGame, self).init()
        self.render_score()
        self.render_hp()
    def update(self):
        
        if not self.game_over: 
            self.reload -= 1
            if self.is_key_pressed(K_LEFT):
                self.ship.move_left()
            elif self.is_key_pressed(K_RIGHT):
                self.ship.move_right()
            
            if self.is_key_pressed(K_SPACE) and self.reload <= 0:

                for bullet in self.bullets:
                    if(bullet.getY() <= -10):
                        bullet.setposbullet(self.ship.getX()+33,self.ship.getY())
                        self.reload = 20
                        break

            for enemy in self.enemies:
                enemy.movement()
                if enemy.y > 620:
                    enemy.y = random.randrange(-600,-400,10) 
                    self.hp -= 1
                    self.render_hp()
                    #print self.hp
                    
                if ((enemy.y+30 > self.ship.y-30) and (self.ship.y+30 > enemy.y-30) and (self.ship.x-40 < enemy.x < self.ship.x+40 )):   
                    enemy.y = random.randrange(-800,-600,10)
                    self.hp -= 1
                    self.render_hp()
                    #print self.hp

                for bullet in self.bullets:
                    if (enemy.y-30 < bullet.y < enemy.y+30) and (enemy.x-40< bullet.x < enemy.x+40):
                        bullet.x = -10
                        bullet.y = -400
                        enemy.y =  random.randrange(-1000,-600,5)
                        self.score += 1
                        self.render_score()
                    if bullet.y < 0:
                        bullet.x = -10
                        bullet.y = -400  

            for bullet in self.bullets:
                bullet.bulletmove()

        if self.hp == 0:
            self.game_over = True
    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, SpaceShipGame.WHITE)
    
    def  render_hp(self):
        self.hp_image = self.font.render("HP = %d" % self.hp, 0, SpaceShipGame.WHITE)

    def render(self, surface):
        self.ship.render(surface)
        for enemy in self.enemies:
            enemy.render(surface)
        for bullet in self.bullets:
            bullet.render(surface)
        surface.blit(self.score_image, (10,10))
        surface.blit(self.hp_image, (680,10))
def main():
    game = SpaceShipGame()
    game.run()

if __name__ == '__main__':
    main()
    
