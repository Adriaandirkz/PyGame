import sys
import pygame
from instance.play import Play

pygame.init()

game = Play()
game.play()
# Clean up and close the game
pygame.quit()
sys.exit()