from pathlib import Path
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'starbasesnow.png'
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'

        self.ship_width = 40
        self.ship_height = 60
        self.name = "Alien Invasion"
        self.FPS = 60

        # Ship settings
        self.ship_speed = 7.5

        # Bullet settings
        self.bullet_speed = 8.0
        self.bullet_width = 9
        self.bullet_height = 45
        self.bullet_color = (60, 60, 60)
        self.bullet_amount = 3