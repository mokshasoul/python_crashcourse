class GameStats():
    """ Track statistics for Alien Invasion """

    def __init__(self, ai_settings):
        """ Initialize satistics """
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """ Initialize stas which change during game """
        self.ships_left = self.ai_settings.ship_limit