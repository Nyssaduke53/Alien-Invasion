import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from bullet_manager import BulletManager
from alien_fleet import AlienFleet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, create game resources, and set up the game environment."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Set up the display screen.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.name)

        # Create ship and its BulletManager.
        self.ship = Ship(self, BulletManager(self))
        self.bullets = pygame.sprite.Group()
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()
        #self.alien = Alien(self, 20, 20)

        # Load and scale background image.
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_width, self.settings.screen_height))

        # Initialize the sound mixer and load the laser sound.
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.5)

        self.impact = pygame.mixer.Sound(self.settings.impact)
        self.impact.set_volume(0.5)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self.alien_fleet.update_fleet()
            self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):

        if self.ship.check_collisions(self.alien_fleet.fleet):
            self.reset_level()

        if self.alien_fleet.check_fleet_bottom():
            self.reset_level()
        
        collisions = self.alien_fleet.check_collisions(self.ship.bullet_manager.active_bullets)
        if collisions:
            self.impact.play()
            self.impact.fadeout(500)


    def reset_level(self):
        self.ship.bullet_manager.active_bullets.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_amount:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        # Blit background and ship, then update the display.
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.ship.bullet_manager.update_active_bullets() 

if __name__ == '__main__':
    # Create an instance of the game and start the main loop.
    ai = AlienInvasion()
    ai.run_game()
