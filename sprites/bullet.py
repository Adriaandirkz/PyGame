# bullet.py

import pygame
from sprites.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, x, y):
        self.bullets.append(self)
        self.active = True
        self.age = 0
        self.x = x
        self.y = y
        self.color = (0, 255, 0)  # Green color for the bullet
        self.radius = 5
        self.speed = 10
        self.shockwave = None

    def update(self):
        self.y -= self.speed  # Move the bullet upward
        if self.y < 0:  # Remove the bullet if it goes off-screen
            self.bullets.remove(self)
        self.collides_with_droids()


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        if self.shockwave:
            self.shockwave.draw(screen)

    def collides_with_droids(self):
        for droid in self.droids:
            distance = self.distance(droid)
            if distance < self.radius + droid.width +5 / 2:
                droid.explode()
                self.explode()


    def explode(self):
        self.bullets.remove(self)
