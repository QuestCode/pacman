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
    play_bttn = Button(ai_settings,screen,'Play')

    pacman_sprites = Group()
    small_game_pellets = Group()
    power_game_pellets = Group()
    blocks = Group()

    gf.load_sprites(ai_settings,small_game_pellets,power_game_pellets,blocks)
    """Create the pacman group"""
    # pacman_sprites = pygame.sprite.RenderUpdates(pacman)

    while True:
        gf.check_events(ai_settings,screen,pacman,play_bttn)
        gf.check_pacman_pellet_collision(ai_settings,pacman,small_game_pellets,power_game_pellets)
        gf.update_screen(ai_settings,screen,pacman_sprites,small_game_pellets,power_game_pellets,blocks)

    pygame.display.flip()

run_game()
