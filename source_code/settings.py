import pygame
import os, sys
from pygame.locals import *

class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen Settings
        self.game_title = 'Pac Man'
        self.screen_width = 500
        self.screen_height = 600
        self.bg_color = (0,0,0)
        self.button_color = (0,0,0)
        self.text_color = (255,255,255)
        self.read_score_file()

        # Pacman settings
        self.pacman_limit = 3


        self.block_size = 24



    def load_images(self):
        self.pacman_image = self.__load_image('pacman.png',-1)
        self.pacman_up_image = self.__load_image('player_u1.png',-1)
        self.pacman_up_open_image = self.__load_image('player_u0.png',-1)
        self.pacman_right_image = self.__load_image('player_r14.png',-1)

        self.pacman_lf_close_image = self.__load_image('leftClose.png',-1)
        self.pacman_lf_open_image = self.__load_image('leftOpen.png',-1)
        self.pacman_rt_close_image = self.__load_image('rightClose.png',-1)
        self.pacman_rt_open_image = self.__load_image('rightOpen.png',-1)
        self.pacman_up_close_image = self.__load_image('upClose.png',-1)
        self.pacman_up_open_image = self.__load_image('upOpen.png',-1)
        self.pacman_down_close_image = self.__load_image('downClose.png',-1)
        self.pacman_down_open_image = self.__load_image('downOpen.png',-1)
        # Ghost
        self.blue_ghost_image = self.__load_image('inky.png',-1)
        self.orange_ghost_image = self.__load_image('clyde.png',-1)
        self.red_ghost_image = self.__load_image('blinky.png',-1)
        self.pink_ghost_image = self.__load_image('pinky.png',-1)
        self.scared_ghost_image = self.__load_image('frightened.png',-1)
        # Objects
        self.pellet_image = self.__load_image('pellet.png',-1)
        self.power_pellet_image = self.__load_image('big_pellet.png',-1)
        self.red_block_image = self.__load_image('square_red.png')
        self.horz_portal_image = self.__load_image('horz_line_orange.png')
        self.vert_portal_image = self.__load_image('vert_line_blue.png')
        self.gate_image = self.__load_image('gate.png')

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
        fullname = os.path.join(fullname,'pacman_'+name)
        try:
            pygame.mixer.music.load(fullname)
            pygame.mixer.music.play()
        except :
            pass

    def read_score_file(self):
        filename = os.path.join('assets', 'scores.txt')
        try:
            self.r_scoreFile = open(filename,'r')
        except :
            print('no file')
            pass

    def write_score_file(self):
        filename = os.path.join('assets', 'scores.txt')
        try:
            self.w_scoreFile = open(filename,'w')
        except :
            print('no file')
            pass
