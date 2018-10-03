from source_code.game_functions import GameFunctions
from source_code.settings import Settings
import pygame
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.game_title)

    gf = GameFunctions(ai_settings,screen)


run_game()
