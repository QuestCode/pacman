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
                pacman.move(event.key)
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,play_bttn,mouse_x,mouse_y)

def update_screen(ai_settings,screen,pacman,small_game_pellets):
    screen.fill(ai_settings.bg_color)
    pacman.draw(screen)
    small_game_pellets.draw(screen)
    pygame.display.flip()

def check_play_button(ai_settings,screen,play_button,mouse_x,mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked:
        print('pal')

def load_sprites(ai_settings,screen,small_game_pellets,blocks):
    """figure out how many pellets we can display"""
    x_offset = (ai_settings.block_size/2)
    y_offset = (ai_settings.block_size/2)

    """Load Level"""
    level1 = FirstLevel(ai_settings)
    layout = level1.getLayout()
    img_list = level1.getSprites()

    for y in range(len(layout)):
        for x in range(len(layout[y])):
            """Get the center point for the rects"""
            centerPoint = [(x*ai_settings.block_size)+x_offset,(y*ai_settings.block_size+y_offset)]
            if layout[y][x]==level1.BLOCK:
                block = sprite.Sprite(centerPoint, img_list[level1.BLOCK])
                blocks.add(block)
            elif layout[y][x]==level1.PACMAN:
                pacman = pacman_Sprite.PacMan(centerPoint,img_list[level1.PACMAN])
            elif layout[y][x]==level1.PELLET:
                pellet = sprite.Sprite(centerPoint, img_list[level1.PELLET])
                small_game_pellets.add(pellet)
                """Create the Snake group"""
    # self.snake_sprites = pygame.sprite.RenderPlain((self.snake))
    # size = 64
    # nNumHorizontal = int(ai_settings.screen_width/size)
    # nNumVertical = int(ai_settings.screen_height/size)
    # """Create all of the pellets and add them to the pellet_sprites group"""
    # for x in range(nNumHorizontal):
    #     for y in range(nNumVertical):
    #         small_game_pellets.add(pellets.Pellet(ai_settings,pygame.Rect(x*size, y*size, size, size)))

def check_pacman_pellet_collision(ai_settings,pacman,small_game_pellets):
    """Check for collision"""
    lstCols = pygame.sprite.spritecollide(pacman,small_game_pellets,True)
    if lstCols:
        """Update the amount of pellets eaten"""
        pacman.pellets = pacman.pellets + int(10*len(lstCols))
        ai_settings.play_sound('waka_waka.wav')
        print(pacman.pellets)
