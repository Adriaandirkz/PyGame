# main.py

import pygame
import sys
import random
from sprites.turret import Turret
from sprites.droid import Droid
from instance.game import Game
from sprites.sprite import Sprite

# Initialize Pygame
pygame.init()

# Set up display variables
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Simple 2D Game with Turret and Droids")
game = Game()
screen = game.display.screen
display = game.display
# Set up the clock for managing the frame rate
clock = pygame.time.Clock()




# Create an instance of the Turret
turret = Turret(display.screen_width//2,display.screen_height//2)



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


    # Spawn a new droid every 5 seconds
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time >= 5000:  # 5 seconds
        droid_x = random.randint(0, display.screen_width - 20)  # Random x position
        droid = Droid(droid_x, 0)  # Spawn at the top of the screen
        last_spawn_time = current_time






    turret = Sprite.turrets[0]
    for turret in Sprite.turrets:
        turret.update()
        turret.draw(screen)
    for droid in Sprite.droids:
        droid.update()
        droid.draw(screen)
    for bullet in Sprite.bullets:
        bullet.update()
        bullet.draw(screen)
    for shockwave in Sprite.shockwaves:
        shockwave.update()
        shockwave.draw(screen)

    if turret.active != True:
        font = pygame.font.Font(None, 74)  # Create a larger font for the Game Over message
        text = font.render("Game Over", True, (255, 0, 0))  # Render the text in red color
        text_rect = text.get_rect(center=(display.screen_width // 2, display.screen_height // 2))  # Center the text
        screen.blit(text, text_rect)  # Draw the text on the screen

        gameover = True
        while gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = False
                    running = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    print("Restart")  # Move turret left
            pygame.display.flip()
            clock.tick(10)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)

# Clean up and close the game
pygame.quit()
sys.exit()
