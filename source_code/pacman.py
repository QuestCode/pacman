import pygame
from pygame.sprite import Sprite


class PacMan(Sprite):
    """A class to represent a pacman sprite."""
    def __init__(self,ai_settings, screen):
        super(PacMan,self).__init__()
        self.image, self.rect = ai_settings.pacman_image
        self.pellets = 0
        """Set the number of Pixels to move each time"""
        self.x_dist = 5
        self.y_dist = 5

    def move(self, key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        xMove = 0;
        yMove = 0;

        if (key == pygame.K_RIGHT):
            xMove = self.x_dist
        elif (key == pygame.K_LEFT):
            xMove = -self.x_dist
        elif (key == pygame.K_UP):
            yMove = -self.y_dist
        elif (key == pygame.K_DOWN):
            yMove = self.y_dist
        #self.rect = self.rect.move(xMove,yMove);
        self.rect.move_ip(xMove,yMove);
