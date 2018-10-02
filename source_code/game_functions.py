import sys
import pygame
from pygame.sprite import Group

from . import settings,pellets

def prep_game():
    pygame.init()
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.game_title)

    """Load Images"""
    ai_settings.load_images()

    pellets = Group()

def start_loop():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # elif event.type == KEYDOWN:
            #     if ((event.key == K_RIGHT)
            #     or (event.key == K_LEFT)
            #     or (event.key == K_UP)
            #     or (event.key == K_DOWN)):
            #         self.snake.move(event.key)

    pygame.display.flip()
