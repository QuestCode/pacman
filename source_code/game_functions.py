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
    while True:
        check_events



def check_events(ai_settings,screen,pacman,play_bttn):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if ((event.key == K_RIGHT)
            or (event.key == K_LEFT)
            or (event.key == K_UP)
            or (event.key == K_DOWN)):
                pacman.move(event.key)
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,play_bttn,mouse_x,mouse_y)

def update_screen():
    pygame.display.flip()

def check_play_button(ai_settings,screen,play_button,mouse_x,mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked:
        print('pal')
