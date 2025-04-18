import pygame
from bullet import Bullet

class BulletManager:
    """A class to manage the ship's bullets."""

    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize the active_bullets, setting up the necessary game settings.
        
        :param game: The main game instance.
        """
        self.game = game
        self.settings = game.settings
        self.active_bullets = pygame.sprite.Group()

    def update_active_bullets(self):
        """
        Update the status of all bullets in the active_bullets.
        
        This method is called every frame to update the bullets and
        remove any that are off-screen.
        """
        self.active_bullets.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """
        Remove bullets that are off the top of the screen.
        
        Bullets are removed when their bottom edge is less than or equal to 0.
        """
        for bullet in self.active_bullets.copy():
            if bullet.rect.bottom <= 0:
                self.active_bullets.remove(bullet)

    def draw(self):
        """
        Draw all bullets in the active_bullets on the screen.
        
        This method iterates through each bullet in the active_bullets and calls
        their draw method to display them.
        """
        for bullet in self.active_bullets:
            bullet.draw_bullet()

    def fire_bullet(self):
        """
        Fire a new bullet and add it to the active_bullets.
        
        :return: Boolean indicating whether the bullet was successfully fired.
        """
        if len(self.active_bullets) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.active_bullets.add(new_bullet)
            return True
        return False
