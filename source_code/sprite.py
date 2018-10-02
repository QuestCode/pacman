import pygame
from pygame.sprite import Sprite

class Sprite(Sprite):

    def __init__(self, centerPoint, image):
        super(Sprite,self).__init__()
        """Set the image and the rect"""
        self.image = image
        self.rect = image.get_rect()
        """Move the rect into the correct position"""
        self.rect.center = centerPoint
