import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to manage individual bullets."""

    def __init__(self, game: 'AlienInvasion', x: float, y: float):
        """
        Initialize a new bullet object at the ship's current position.
        
        :param game: The main game instance, providing access to screen and settings.
        """
        super().__init__()
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        # Load the bullet image and scale it to the specified size.
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))

        # Create a bullet rect at (0, 0) and then position it based on the ship's current position.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Store the bullet's exact vertical position as a float for smoothness
        self.y = float(self.rect.y)
    
    def update(self):
        pass

    def draw_alien(self):
        """
        Draw the bullet to the screen.
        
        This method draws the bullet image at its current position.
        """
        self.screen.blit(self.image, self.rect)
