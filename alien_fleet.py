import pygame
from alien import Alien
from random import randint

class AlienFleet:
    """Controls the alien fleet's creation, behavior, and interactions."""

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """Create a new fleet of aliens."""
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_width
        screen_h = self.settings.screen_height

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

        #fleet type
        self._create_random_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """Fill the screen with a grid of aliens."""
        for row in range(fleet_h):
            for col in range(fleet_w):
                if col % 2 == 0 or row % 2 == 0:
                    continue
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                self._create_alien(current_x, current_y)

    def _create_cross_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """Fill the screen with a grid of aliens."""
        for row in range(fleet_h):
            for col in range(fleet_w):
                if col != (row * 2):
                    continue
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                self._create_alien(current_x, current_y)

    def _create_random_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        for row in range(fleet_h):
            for col in range(fleet_w):
                pick = randint(0,5)
                if pick != 1:
                    continue
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """Center the fleet in the upper half of the screen."""
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = (screen_w - fleet_horizontal_space) // 2
        y_offset = (self.settings.screen_height // 2 - fleet_vertical_space) // 2
        return x_offset, y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """Determine how many aliens fit horizontally and vertically."""
        fleet_w = screen_w // alien_w
        fleet_h = (screen_h // 2) // alien_h

        fleet_w = fleet_w - 1 if fleet_w % 2 == 0 else fleet_w - 2
        fleet_h = fleet_h - 1 if fleet_h % 2 == 0 else fleet_h - 2

        return int(fleet_w), int(fleet_h)

    def _create_alien(self, current_x, current_y):
        """Create an individual alien and add it to the fleet."""
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    def check_fleet_edges(self):
        """Reverse fleet direction and drop if any alien reaches the edge."""
        for alien in self.fleet:
            if alien.check_edges():
                self.fleet_direction *= -1
                self._drop_alien_fleet()
                break

    def _drop_alien_fleet(self):
        """Move the fleet downward."""
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def update_fleet(self):
        """Update the fleet's position."""
        self.check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """Draw all aliens on the screen."""
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """Remove aliens and colliding sprites on impact."""
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    def check_fleet_bottom(self) -> bool:
        """Check if any alien has reached the bottom of the screen."""
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_height:
                return True
        return False

    def check_destroyed_status(self):
        """Return True if all aliens are destroyed."""
        return not self.fleet
