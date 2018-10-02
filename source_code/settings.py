import pygame
import os, sys
from pygame.locals import *

class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen Settings
        self.game_title = 'Pac Man'
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0,0,0)
        self.button_color = (0,0,0)
        self.text_color = (255,255,255)

        # Ship settings
        self.pacman_limit = 3


        try:
            self.winner_font = pygame.font.Font("fonts/Megadeth.ttf", 70)
        except:
            self.winner_font = pygame.font.Font(None, 70)


    def load_images(self):
        self.pacman_image = self.__load_image('pacman.png',-1)
        self.blue_ghost_image = self.__load_image('blue_ghost.png',-1)
        self.orange_ghost_image = self.__load_image('orange_ghost.png',-1)
        self.red_ghost_image = self.__load_image('red_ghost.png',-1)
        self.pellet_image = self.__load_image('pellet.png',-1)

    def __load_image(self,name, colorkey=None):
        fullname = os.path.join('assets', 'images')
        fullname = os.path.join(fullname, name)
        try:
            image = pygame.image.load(fullname)
        except:
            print ('Cannot load image:', fullname)
            raise SystemExit
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image, image.get_rect()


    def play_sound(self,name):
        fullname = os.path.join('assets', 'sounds')
        fullname = os.path.join(fullname, name)
        try:
            pygame.mixer.music.load(fullname)
            pygame.mixer.music.play()
        except :
            pass
