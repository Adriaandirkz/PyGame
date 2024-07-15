# turret.py

import pygame
from bullet import Bullet
from shockwave import Shockwave


class Turret:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 0, 0)  # Red color for the turret
        self.width = 20
        self.height = 20
        self.dragging = False
        self.bullets = []
        self.last_shot_time = pygame.time.get_ticks()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        for bullet in self.bullets:
            bullet.draw(screen)

    def is_clicked(self, mouse_pos):
        mx, my = mouse_pos
        return self.x <= mx <= self.x + self.width and self.y <= my <= self.y + self.height

    def update_position(self, mouse_pos):
        mx, my = mouse_pos
        self.x = mx - self.width // 2
        self.y = my - self.height // 2

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= 2000:  # 2 seconds
            bullet = Bullet(self.x + self.width // 2, self.y)
            self.bullets.append(bullet)
            self.last_shot_time = current_time

    def update_bullets(self, droids):
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.y < 0:  # Remove the bullet if it goes off-screen
                self.bullets.remove(bullet)
            else:
                for droid in droids:
                    if bullet.collides_with(droid):
                        droid.explode()
                        self.bullets.remove(bullet)
                        break

    def explode(self):
        print("Collision")
        self.shockwave = Shockwave(self.x,self.y,full=True)
        self.shockwave.draw()

