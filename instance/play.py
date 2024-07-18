import pygame
import random
from sprites.turret import Turret
from sprites.droid import Droid
from instance.game import Game
from sprites.sprite import Sprite

class Play(Game):


    def __init__(self):
        Game.__init__(self)
        self.game = Game()
        self.screen = self.game.display.screen
        self.clock = pygame.time.Clock()
        self.running = True

    def droid_spawn(self,last_spawn_time):
        """"Write here shortly what this function does"""
        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time >= 5000:  # 5 seconds
            droid_x = random.randint(0, self.display.screen_width - 20)  # Random x position
            droid = Droid(droid_x, 0)  # Spawn at the top of the screen
            last_spawn_time = current_time
            return last_spawn_time
        return last_spawn_time

    def update(self):
        self.screen.fill((0, 0, 0))
        for turret in Sprite.turrets:
            turret.update()
            turret.draw(self.screen)
        for droid in Sprite.droids:
            droid.update()
            droid.draw(self.screen)
        for bullet in Sprite.bullets:
            bullet.update()
            bullet.draw(self.screen)
        for shockwave in Sprite.shockwaves:
            shockwave.update()
            shockwave.draw(self.screen)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if self.turret.is_clicked(event.pos):
                        self.turret.dragging = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    self.turret.dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if self.turret.dragging:
                    self.turret.update_position(event.pos)

    def check_gamestates(self):
        if self.turret.active != True:
            font = pygame.font.Font(None, 74)  # Create a larger font for the Game Over message
            text = font.render("Game Over", True, (255, 0, 0))  # Render the text in red color
            text_rect = text.get_rect(
                center=(self.display.screen_width // 2, self.display.screen_height // 2))  # Center the text
            self.screen.blit(text, text_rect)  # Draw the text on the screen

            gameover = True
            while gameover:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameover = False
                        self.running = False
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_r]:
                        print("Restart")  # Move turret left
                pygame.display.flip()
                self.clock.tick(10)

    def play(self):
        # Create an instance of the Turret Needed for control management
        self.turret = Turret(self.display.screen_width // 2, self.display.screen_height // 2)

        # Timer to track when to spawn the next droid
        last_spawn_time = pygame.time.get_ticks()

        # Main game loop
        while self.running:
            #Check all inputs
            self.input()
            # Spawn a new droid every 5 seconds
            last_spawn_time = self.droid_spawn(last_spawn_time)
            #Update all sprites
            self.update()
            #Check game over condition
            self.check_gamestates()
            # Update the display
            pygame.display.flip()

            # Cap the frame rate at 60 frames per second
            self.clock.tick(60)