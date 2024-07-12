# droid.py

import pygame
import math
from explosion_particle import ExplosionParticle
from shockwave import Shockwave


class Droid:
    def __init__(self, x, y, speed=1):
        self.x = x
        self.y = y
        self.color = (0, 0, 255)  # Blue color for the droid
        self.width = 20
        self.height = 20
        self.speed = speed
        self.exploded = False
        self.explosion_particles = []
        self.shockwave = None

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        for particle in self.explosion_particles:
            particle.draw(screen)

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
        self.create_explosion_particles()
        self.create_shockwave()
        self.exploded = True



    def create_explosion_particles(self):
        for _ in range(50):  # Increase number of particles for a denser explosion
            particle = ExplosionParticle(self.x + self.width // 2, self.y + self.height // 2)
            self.explosion_particles.append(particle)

    def create_shockwave(self):
        self.shockwave = True

    def update_explosion_particles(self):
        for particle in self.explosion_particles[:]:
            particle.update()
            if particle.radius <= 0:  # Remove particles that are too small
                self.explosion_particles.remove(particle)

