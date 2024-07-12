# explosion_particle.py
import math

import pygame
import random

class ExplosionParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 0)  # Yellow color for the particles
        self.radius = random.randint(5, 15)  # Larger initial radius
        self.speed = random.uniform(1, 3)  # Slower initial speed
        self.direction = random.uniform(0, 2 * math.pi)

    def update(self):
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)
        self.radius -= 0.1  # Decrease radius over time

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.radius))
