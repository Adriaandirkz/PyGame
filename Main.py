# main.py

import pygame
import sys
import random
from turret import Turret
from droid import Droid
from shockwave import Shockwave

# Initialize Pygame
pygame.init()

# Set up display variables
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple 2D Game with Turret and Droids")

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

# Create an instance of the Turret
turret = Turret(screen_width // 2, screen_height // 2)

# List to hold droids
droids = []

# List to hold shockwaves
shockwaves = []

# Timer to track when to spawn the next droid
last_spawn_time = pygame.time.get_ticks()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if turret.is_clicked(event.pos):
                    turret.dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                turret.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if turret.dragging:
                turret.update_position(event.pos)

    # Fill the screen with a color (e.g., black)
    screen.fill((0, 0, 0))

    # Update and draw the turret
    turret.draw(screen)
    turret.shoot()

    # Spawn a new droid every 5 seconds
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time >= 5000:  # 5 seconds
        droid_x = random.randint(0, screen_width - 20)  # Random x position
        droid = Droid(droid_x, 0)  # Spawn at the top of the screen
        droids.append(droid)
        last_spawn_time = current_time

    # Remove exploded droids and update the remaining droids
    droids = [d for d in droids if not d.exploded]
    turret.update_bullets(droids)

    # Update and draw each droid
    for droid in droids:
        droid.move_towards(turret.x + turret.width // 2, turret.y + turret.height // 2)
        if droid.collides_with(turret):
            turret.explode()
        droid.draw(screen)
        if droid.shockwave:
            shockwaves.append(Shockwave(droid.x,droid.y))



    for shockwave in shockwaves:
        shockwave.update()
        if shockwave.alpha <= 0:
            shockwaves.remove(shockwave)
        else:
            shockwave.draw(screen)


    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)

# Clean up and close the game
pygame.quit()
sys.exit()
