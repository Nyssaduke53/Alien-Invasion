import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Represents a single alien in the fleet."""

    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """Create an alien at a given position."""
        super().__init__()

        self.fleet = fleet
        self.screen = fleet.game.screen
        self.settings = fleet.game.settings
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move alien horizontally with fleet."""
        speed = self.settings.fleet_speed
        self.x += speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """Return True if alien hits screen edge."""
        return self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left

    def draw_alien(self):
        """Draw alien on the screen."""
        self.screen.blit(self.image, self.rect)
