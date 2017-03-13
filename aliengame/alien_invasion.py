import pygame

import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    """ main function for the game, programm entry point """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption("Alien Invastion")

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
