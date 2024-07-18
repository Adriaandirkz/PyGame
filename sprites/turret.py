# turret.py

import pygame
from sprites.bullet import Bullet
from sprites.sprite import Sprite
from sprites.shockwave import Shockwave


class Turret(Sprite):
    def __init__(self, x, y):
        self.turrets.append(self)
        self.active = True
        self.x = x
        self.y = y
        self.color = (255, 0, 0)  # Red color for the turret
        self.width = 20
        self.height = 20
        self.dragging = False
        self.last_shot_time = pygame.time.get_ticks()

    def update(self):
        self.shoot()


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
        if current_time - self.last_shot_time >= 2000 and self.active:  # 2 seconds
            Bullet(self.x + self.width // 2, self.y)
            self.last_shot_time = current_time


    def explode(self):
        self.active = False
        self.shockwaves.append(Shockwave(self.x,self.y,full=True))
        print("Collision")


