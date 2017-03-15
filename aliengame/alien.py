import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent the alien ships """

    def __init__(self, ai_settings, screen):
        """ Init dem aliens """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images\\alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        """ Return true if at edge """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        """ put sprite on screen """
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_settings.fleet_direction*self.ai_settings.alien_speed_factor)
        self.rect.x = self.x
