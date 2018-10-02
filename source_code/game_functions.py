import sys
import pygame
from pygame.sprite import Group

from . import settings,pellets,sprite,pacman_Sprite
from .levels.level001 import FirstLevel

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
                pacman.MoveKeyDown(event.key)
        elif event.type == pygame.KEYUP:
            if ((event.key == pygame.K_RIGHT)
            or (event.key == pygame.K_LEFT)
            or (event.key == pygame.K_UP)
            or (event.key == pygame.K_DOWN)):
                pacman.MoveKeyUp(event.key)
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,play_bttn,mouse_x,mouse_y)

def update_screen(ai_settings,screen,pacman,small_game_pellets,power_game_pellets,blocks):
    screen.fill(ai_settings.bg_color)

    # pacman_sprites.clear(screen,self.background)
    # pacman.draw(screen)
    power_game_pellets.draw(screen)
    small_game_pellets.draw(screen)
    blocks.draw(screen)
    # pacman_sprites.draw(self.screen)
    pygame.display.flip()

def check_play_button(ai_settings,screen,play_button,mouse_x,mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked:
        print('pal')

def load_sprites(ai_settings,small_game_pellets,power_game_pellets,blocks):

    """Load Level"""
    level1 = FirstLevel(ai_settings)
    create_level(ai_settings,level1,small_game_pellets,power_game_pellets,blocks)


def create_level(ai_settings,level,small_game_pellets,power_game_pellets,blocks):
    """figure out how many pellets we can display"""
    x_offset = (ai_settings.block_size/2)
    y_offset = (ai_settings.block_size/2)

    layout = level.getLayout()
    img_list = level.getSprites()
    for y in range(len(layout)):
        for x in range(len(layout[y])):
            """Get the center point for the rects"""
            centerPoint = [(x*ai_settings.block_size)+x_offset,(y*ai_settings.block_size+y_offset)]
            if layout[y][x]==level.BLOCK:
                block = sprite.Sprite(centerPoint, img_list[level.BLOCK])
                blocks.add(block)
            elif layout[y][x]==level.PACMAN:
                pacman = pacman_Sprite.PacMan(centerPoint,img_list[level.PACMAN])
            elif layout[y][x]==level.PELLET:
                pellet = sprite.Sprite(centerPoint, img_list[level.PELLET])
                small_game_pellets.add(pellet)
            elif layout[y][x]==level.POWER_PELLET:
                power_pellet = sprite.Sprite(centerPoint, img_list[level.POWER_PELLET])
                power_game_pellets.add(power_pellet)

    return pacman


def check_pacman_pellet_collision(ai_settings,pacman,small_game_pellets,power_game_pellets):
    """Check for collision"""
    pellet_Cols = pygame.sprite.spritecollide(pacman,small_game_pellets,True)
    power_pellet_Cols = pygame.sprite.spritecollide(pacman,power_game_pellets,True)
    if pellet_Cols:
        """Update the amount of pellets eaten"""
        pacman.pellets = pacman.pellets + int(10*len(pellet_Cols))
        ai_settings.play_sound('waka_waka.wav')
        print(pacman.pellets)
    elif power_pellet_Cols:
        """Update the amount of pellets eaten"""
        pacman.pellets = pacman.pellets + int(50*len(power_pellet_Cols))
        ai_settings.play_sound('waka_waka.wav')
        print(pacman.pellets)
