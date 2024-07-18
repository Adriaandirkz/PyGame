# droid.py

import pygame
import math
#from explosion import Explosion
from sprites.shockwave import Shockwave
from sprites.sprite import Sprite


class Droid(Sprite):
    def __init__(self, x, y, speed=1):
        self.droids.append(self)
        self.active = True
        self.x = x
        self.y = y
        self.color = (0, 0, 255)  # Blue color for the droid
        self.width = 20
        self.height = 20
        self.speed = speed
        self.explosion_particles = []
        self.shockwave = None


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        for particle in self.explosion_particles:
            particle.draw(screen)

    def update(self):
        turret = self.turrets[0]
        target_x, target_y = turret.x,turret.y
        self.move_towards(target_x,target_y)


        if self.collides_with(turret):
            turret.explode()


    def move_towards(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance > 0:
            dx /= distance
            dy /= distance

            self.x += dx * self.speed
            self.y += dy * self.speed

    def explode(self):
        #self.create_explosion_particles()
        self.shockwaves.append(Shockwave( self.x,self.y))
        self.droids.remove(self)


    def collides_with(self, turret):
        distance = ((self.x - turret.x) ** 2 + (self.y - turret.y) ** 2) ** 0.5
        return distance < self.width + turret.width +3 / 2