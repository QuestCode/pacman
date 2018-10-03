import sys
import pygame
from pygame.sprite import Group

from . import settings,pellets,sprite,pacman,button,ghost
from .levels.level001 import FirstLevel

class GameFunctions:

    def __init__(self,ai_settings,screen):
        self.ai_settings = ai_settings
        self.screen = screen

        """Load Images"""
        self.ai_settings.load_images()
        """tell pygame to keep sending up keystrokes when they are held down"""
        pygame.key.set_repeat(500, 30)

        self.play_bttn = button.Button(ai_settings,screen,'Play')

        self.ghost_sprites = Group()
        self.small_game_pellets = Group()
        self.power_game_pellets = Group()
        self.block_sprites = Group()

        """Create Background"""
        self.background = pygame.Surface(screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))

        self.load_sprites()

        while True:
            self.pacman_sprites.clear(self.screen,self.background)
            self.ghost_sprites.clear(self.screen,self.background)
            self.check_events()
            self.check_pacman_pellet_collision()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if ((event.key == pygame.K_RIGHT)
                or (event.key == pygame.K_LEFT)
                or (event.key == pygame.K_UP)
                or (event.key == pygame.K_DOWN)):
                    self.pacman.MoveKeyDown(event.key)
            elif event.type == pygame.KEYUP:
                if ((event.key == pygame.K_RIGHT)
                or (event.key == pygame.K_LEFT)
                or (event.key == pygame.K_UP)
                or (event.key == pygame.K_DOWN)):
                    self.pacman.MoveKeyUp(event.key)
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                self.check_play_button(mouse_x,mouse_y)

            self.pacman_sprites.update(self.block_sprites,self.small_game_pellets,self.power_game_pellets,self.ghost_sprites)
            self.ghost_sprites.update(self.block_sprites)

    def update_screen(self):
        self.screen.fill(self.ai_settings.bg_color)
        self.screen.blit(self.background, (0, 0))
        self.block_sprites.draw(self.background)

        # pacman_sprites.clear(screen,self.background)
        # pacman.draw(screen)
        self.power_game_pellets.draw(self.screen)
        self.small_game_pellets.draw(self.screen)
        self.pacman_sprites.draw(self.screen)
        self.ghost_sprites.draw(self.screen)
        pygame.display.flip()

    def check_play_button(self,mouse_x,mouse_y):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_x,mouse_y)
        if button_clicked:
            print('pal')


    def load_sprites(self):
        """Load Level"""
        level1 = FirstLevel(self.ai_settings)
        self.create_level(level1)


    def create_level(self,level):
        """figure out how many pellets we can display"""
        x_offset = (self.ai_settings.block_size/2)
        y_offset = (self.ai_settings.block_size/2)

        layout = level.getLayout()
        img_list = level.getSprites()
        for x in range(len(layout)):
            for y in range(len(layout[x])):
                """Get the center point for the rects"""
                centerPoint = [(y*self.ai_settings.block_size)+y_offset,(x*self.ai_settings.block_size+x_offset)]
                if layout[x][y]==level.BLOCK:
                    block = sprite.Sprite(centerPoint, img_list[level.BLOCK])
                    self.block_sprites.add(block)
                elif layout[x][y]==level.PACMAN:
                    self.pacman = pacman.PacMan(centerPoint,img_list[level.PACMAN])
                    # print(x,y)
                elif layout[x][y]==level.PELLET:
                    pellet = sprite.Sprite(centerPoint, img_list[level.PELLET])
                    self.small_game_pellets.add(pellet)
                elif layout[x][y]==level.POWER_PELLET:
                    power_pellet = sprite.Sprite(centerPoint, img_list[level.POWER_PELLET])
                    self.power_game_pellets.add(power_pellet)
                elif layout[x][y]==level.REDGHOST:
                    ghost_sprite = ghost.Ghost(centerPoint, img_list[level.REDGHOST],img_list[level.SCAREDGHOST])
                    self.ghost_sprites.add(ghost_sprite)
                elif layout[x][y]==level.BLUEGHOST:
                    ghost_sprite = ghost.Ghost(centerPoint, img_list[level.BLUEGHOST],img_list[level.SCAREDGHOST])
                    self.ghost_sprites.add(ghost_sprite)
                elif layout[x][y]==level.ORANGEGHOST:
                    ghost_sprite = ghost.Ghost(centerPoint, img_list[level.ORANGEGHOST],img_list[level.SCAREDGHOST])
                    self.ghost_sprites.add(ghost_sprite)
                elif layout[x][y]==level.PINKGHOST:
                    ghost_sprite = ghost.Ghost(centerPoint, img_list[level.PINKGHOST],img_list[level.SCAREDGHOST])
                    self.ghost_sprites.add(ghost_sprite)
        self.pacman_sprites = pygame.sprite.RenderPlain(self.pacman)


    def check_pacman_pellet_collision(self):
        """Check for collision"""
        pellet_Cols = pygame.sprite.spritecollide(self.pacman,self.small_game_pellets,True)
        power_pellet_Cols = pygame.sprite.spritecollide(self.pacman,self.power_game_pellets,True)
        if pellet_Cols:
            """Update the amount of pellets eaten"""
            self.pacman.pellets = self.pacman.pellets + int(10*len(pellet_Cols))
            self.ai_settings.play_sound('chump.wav')
            print(self.pacman.pellets)
        elif power_pellet_Cols:
            """Update the amount of pellets eaten"""
            self.pacman.pellets = self.pacman.pellets + int(50*len(power_pellet_Cols))
            self.ai_settings.play_sound('chump.wav')
            print(self.pacman.pellets)
