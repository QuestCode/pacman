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

def check_events(ai_settings,screen,pacman,play_bttn):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if ((event.key == pygame.K_RIGHT)
            or (event.key == pygame.K_LEFT)
            or (event.key == pygame.K_UP)
            or (event.key == pygame.K_DOWN)):
                pacman.move(event.key)
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,play_bttn,mouse_x,mouse_y)

def update_screen(ai_settings,screen,pacman,game_pellets):
    screen.fill(ai_settings.bg_color)
    pacman.draw(screen)
    game_pellets.draw(screen)
    pygame.display.flip()

def check_play_button(ai_settings,screen,play_button,mouse_x,mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked:
        print('pal')

def load_sprites(ai_settings,screen,game_pellets):
    """figure out how many pellets we can display"""
    size = 48
    nNumHorizontal = int(ai_settings.screen_width/size)
    nNumVertical = int(ai_settings.screen_height/size)
    """Create all of the pellets and add them to the pellet_sprites group"""
    for x in range(nNumHorizontal):
        for y in range(nNumVertical):
            game_pellets.add(pellets.Pellet(ai_settings,pygame.Rect(x*size, y*size, size, size)))
