# bullet.py

import pygame
from shockwave import Shockwave

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 255, 0)  # Green color for the bullet
        self.radius = 5
        self.speed = 5
        self.shockwave = None

    def update(self):
        self.y -= self.speed  # Move the bullet upward
        if self.shockwave:
            self.shockwave.update()
            if self.shockwave.alpha <= 0:
                self.shockwave = None

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        if self.shockwave:
            self.shockwave.draw(screen)

    def collides_with(self, droid):
        distance = ((self.x - droid.x) ** 2 + (self.y - droid.y) ** 2) ** 0.5
        return distance < self.radius + droid.width / 2

    def handle_collision(self, droid):
        droid.explode()

        # Create shockwave at droid's position
        self.shockwave = Shockwave(droid.x + droid.width // 2, droid.y + droid.height // 2)
