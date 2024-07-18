# shockwave.py

import pygame
from sprites.sprite import Sprite

class Shockwave(Sprite):
    def __init__(self, x, y, full = False):
        self.shockwaves.append(self)
        self.x = x
        self.y = y
        self.color = (255, 255, 255)  # White color for the shockwave
        self.radius = 0
        self.max_radius = 10000
        self.growth_speed = 10
        self.alpha = 255  # Max opacity
        self.width = 10
        self.full = full

    def update(self):
        self.radius += self.growth_speed
        self.alpha -= 10  # Fade out effect
        if self.alpha < 0:
            self.alpha = 0
            self.shockwaves.remove(self)


    def draw(self, screen):
        if self.radius < self.max_radius:
            pygame.draw.circle(screen, (self.color[0], self.color[1], self.color[2], self.alpha),
                               (int(self.x), int(self.y)), self.radius, 0 if self.full else self.width)
