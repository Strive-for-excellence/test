import pygame

class Menu:
    def __init__(self):
        self.difficulty = 'Easy'
        self.font = pygame.font.Font(None, 36)

    def draw(self, WIN):
        # Draw the menu and the difficulty selection
        text = self.font.render(f"Difficulty: {self.difficulty}", True, (255, 255, 255))
        WIN.blit(text, (10, 10))

    def change_difficulty(self, difficulty):
        self.difficulty = difficulty