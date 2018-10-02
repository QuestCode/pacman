import source_code.game_functions as gf
from source_code.settings import Settings
from source_code.pacman import PacMan
from source_code.button import Button
import pygame
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.game_title)

    """Load Images"""
    ai_settings.load_images()
    pacman = PacMan(ai_settings,screen)
    play_bttn = Button(ai_settings,screen,'Play')

    pellets = Group()

    while 1:
        gf.check_events(ai_settings,screen,pacman,play_bttn)

    pygame.display.flip()

run_game()
