from source_code.settings import Settings
# from source_code import settings
import pygame
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.game_title)

run_game()
