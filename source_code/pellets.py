import pygame
from pygame.sprite import Sprite


class Pellet(Sprite):

    def __init__(self,ai_settings,rect=None):
        super(Pellet,self).__init__()
        self.image, self.rect = ai_settings.pellet_image
        if rect != None:
            self.rect = rect
