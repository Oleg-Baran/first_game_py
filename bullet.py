import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen
        # Create a bullet rect at (0, 0) and then set correct position.
        self.ai_settings = ai_settings
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.x = ship.rect.x
        self.rect.y = ship.rect.y + 38
        self.rect.right = ship.rect.centerx
        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        self.direction = 1
    
    def update(self):
        """Move the bullet right the screen."""
        # Update the decimal position of the bullet.
        self.x += self.speed_factor * self.direction
        self.rect.x = self.x
        # if self.direction == -1:
        #     self.x -= self.speed_factor
        #     self.rect.x = self.x

       
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)