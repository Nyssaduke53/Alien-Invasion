import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to manage individual aliens."""

    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """
        Initialize a new alien object at the ship's current position.
        
        :param game: The main game instance, providing access to screen and settings.
        """
        super().__init__()
        self.fleet = fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        # Load the alien image and scale it to the specified size.
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))

        # Create an alien rect and then position it based on given coords.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Store the alien's exact position as floats for smoothness
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    
    def update(self):
        temp_speed = self.settings.fleet_speed

        #if self.check_edges():
            #self.settings.fleet_direction *= -1
            #self.y += self.settings.fleet_drop_speed
        self.x += (temp_speed * self.fleet.fleet_direction)
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        return (self.rect.right >= self.boundaries.right) or (self.rect.left <= self.boundaries.left)

    def draw_alien(self):
        """
        Draw the alien to the screen.
        
        This method draws the alien image at its current position.
        """
        self.screen.blit(self.image, self.rect)
