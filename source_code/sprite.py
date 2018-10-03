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

# class Pellet(pygame.sprite.Sprite):
#     def __init__(self, top_left, image = None):
#         pygame.sprite.Sprite.__init__(self)
#
#         if image == None:
#             self.image, self.rect = load_image('pellet.png',-1)
#         else:
#             self.image = image
#             self.rect = image.get_rect()
#
#         self.rect.topleft = top_left
