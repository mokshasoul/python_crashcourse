class Settings():
    """ A class to store all game settigns """

    def __init__(self):
        """ Initialize game settings """
        # Game Screen
        self.screen_width = 1024
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed_factor = 1.5
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # +1 = right, -1 = left
        self.fleet_direction = 1
        self.ship_limit = 3