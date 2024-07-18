import pygame





class Display():
    def __init__(self, screen_width = 800, screen_height = 600):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Simple 2D Game with Turret and Droids")

    def display_game_over(self, screen):
        font = pygame.font.Font(None, 74)  # Create a larger font for the Game Over message
        text = font.render("Game Over", True, (255, 0, 0))  # Render the text in red color
        text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))  # Center the text
        screen.blit(text, text_rect)  # Draw the text on the screen

    def flip(self):
        pygame.display.flip()
