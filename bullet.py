import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize a new bullet object at the ship's current position.
        
        :param game: The main game instance, providing access to screen and settings.
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load the bullet image and scale it to the specified size.
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_width, self.settings.bullet_height))

        # Create a bullet rect at (0, 0) and then position it based on the ship's current position.
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop

        # Store the bullet's exact vertical position as a float.
        self.y = float(self.rect.y)
    
    def update(self):
        """
        Move the bullet up the screen.
        
        This method is called every frame to update the bullet's position.
        """
        # Update the bullet's exact vertical position.
        self.y -= self.settings.bullet_speed
        # Update the rect's vertical position to match the bullet's new position.
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Draw the bullet to the screen.
        
        This method draws the bullet image at its current position.
        """
        self.screen.blit(self.image, self.rect)
