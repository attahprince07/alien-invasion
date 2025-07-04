import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullets fired by ship"""

    def __init__(self, ai_settings, screen, ship):
        """Make a bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Make a bullet rect at (0, 0) and set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_width)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store bullet position as decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)