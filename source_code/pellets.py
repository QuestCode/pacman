import pygame
from pygame.sprite import Sprite


class Pellet(Sprite):

    def __init__(self,ai_settings):
        super(Pellet,self).__init__()
        self.image, self.rect = ai_settings.pellet_image
