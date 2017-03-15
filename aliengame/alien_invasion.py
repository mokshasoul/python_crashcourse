import pygame

import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats

def run_game():
    """ main function for the game, programm entry point """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    # Make group to store bullet objects
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    pygame.display.set_caption("Alien Invastion")
    stats = GameStats(ai_settings)
    while True:
        gf.check_events(ai_settings, screen, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            # Delete oos bullets
            gf.update_bullets(ai_settings, stats, screen, ship, bullets, aliens)
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
