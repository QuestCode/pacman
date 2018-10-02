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
    """tell pygame to keep sending up keystrokes when they are held down"""
    pygame.key.set_repeat(500, 30)
    pacman = PacMan(ai_settings,screen)
    pacman_sprites = pygame.sprite.RenderPlain(pacman)
    play_bttn = Button(ai_settings,screen,'Play')

    game_pellets = Group()

    gf.load_sprites(ai_settings,screen,game_pellets)

    while True:
        gf.check_events(ai_settings,screen,pacman,play_bttn)
        gf.check_pacman_pellet_collision(pacman,game_pellets)
        gf.update_screen(ai_settings,screen,pacman_sprites,game_pellets)

    pygame.display.flip()

run_game()
