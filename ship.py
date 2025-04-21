import pygame
from bullet_manager import BulletManager

class Ship:
    """A class to manage a ship in the game."""

    def __init__(self, game, bullet_manager: 'bullet_manager'):
        """
        Initialize the ship and set its starting position.
        
        :param game: The main game instance.
        :param bullet_manager: The ship's bullet manager.
        """
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.bullet_manager = bullet_manager

        # Load and scale the ship image once during initialization.
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_width, self.settings.ship_height))
        self.rect = self.image.get_rect()

        # Position the ship at the bottom center of the screen.
        self._center_ship()

        # Movement flags: The ship starts stationary.
        self.moving_right = False
        self.moving_left = False

    def _center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        

    def update(self):
        """
        Update the ship's movement and arsenal.
        
        This method is called every frame to update the ship's position
        and the status of its bullets.
        """
        self.update_ship_movement()
        self.bullet_manager.update_active_bullets()

    def update_ship_movement(self):
        """
        Update the ship's horizontal movement based on user input.
        
        The ship's position is constrained to the screen's boundaries.
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the ship's rect position based on the updated x value.
        self.rect.x = self.x

    def draw(self):
        """
        Draw the ship at its current position on the screen.
        
        This method also draws the ship's arsenal (bullets).
        """
        self.bullet_manager.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """
        Fire a bullet from the ship's arsenal.
        
        :return: Boolean indicating if the bullet was successfully fired.
        """
        return self.bullet_manager.fire_bullet()
    
    def check_collisions(self, other_group):
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False
