import sys
import pygame
from pygame.sprite import Group

from source_code import settings,pellets,sprite,pacman,button,ghost
from source_code.levels import level001
from source_code.levels import level002
from source_code.levels import level003

class GameFunctions:

    def __init__(self,ai_settings,screen):
        self.ai_settings = ai_settings
        self.screen = screen

        """Load Images"""
        self.ai_settings.load_images()
        """tell pygame to keep sending up keystrokes when they are held down"""
        # pygame.key.set_repeat(500, 30)

        """Play game sound at beginning"""
        self.ai_settings.play_sound('beginning.wav')

        self.load_sprites()

        """Create Background"""
        self.background = pygame.Surface(screen.get_size())
        self.background = self.background.convert()
        self.background.fill(self.ai_settings.bg_color)
        """Draw the blocks onto the background,"""
        self.block_sprites.draw(self.screen)
        self.block_sprites.draw(self.background)
        self.gate_sprites.draw(self.screen)
        self.gate_sprites.draw(self.background)
        self.horz_portal_sprites.draw(self.screen)
        self.horz_portal_sprites.draw(self.background)
        self.vert_portal_sprites.draw(self.screen)
        self.vert_portal_sprites.draw(self.background)

        pygame.display.flip()

        while True:
            self.pacman_sprites.clear(self.screen,self.background)
            self.ghost_sprites.clear(self.screen,self.background)
            self.check_events()
            self.update_screen()

    def check_events(self):
        # for e in pygame.event.get():
        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if ((e.key == pygame.K_RIGHT)
            or (e.key == pygame.K_LEFT)
            or (e.key == pygame.K_UP)
            or (e.key == pygame.K_DOWN)):
                self.pacman.MoveKeyDown(e.key)
        elif e.type == pygame.KEYUP:
            if ((e.key == pygame.K_RIGHT)
            or (e.key == pygame.K_LEFT)
            or (e.key == pygame.K_UP)
            or (e.key == pygame.K_DOWN)):
                self.pacman.MoveKeyUp(e.key)
            elif e.key == pygame.K_q:
                sys.exit()

        self.pacman_sprites.update(self.block_sprites
                                    ,self.vert_portal_sprites
                                    ,self.horz_portal_sprites
                                    ,self.small_game_pellets
                                    ,self.power_game_pellets
                                    ,self.ghost_sprites)
        self.ghost_sprites.update(self.block_sprites
                                    ,self.vert_portal_sprites
                                    ,self.horz_portal_sprites)

    def update_screen(self):
        self.screen.blit(self.background, (0, 0))

        textpos = 0
        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render("Score %s" % self.pacman.pellets
                                , 1, (255, 255, 255))
            textpos = text.get_rect(centerx=self.background.get_width()/2)
            self.screen.blit(text, textpos)

        reclist = [textpos]
        # pacman_sprites.clear(screen,self.background)
        # pacman.draw(screen)
        reclist += self.power_game_pellets.draw(self.screen)
        reclist += self.small_game_pellets.draw(self.screen)
        reclist += self.pacman_sprites.draw(self.screen)
        reclist += self.ghost_sprites.draw(self.screen)
        pygame.display.update(reclist)


    def load_sprites(self):
        """Load Level"""
        self.ghost_sprites = pygame.sprite.RenderUpdates()
        self.small_game_pellets = pygame.sprite.RenderUpdates()
        self.power_game_pellets = pygame.sprite.RenderUpdates()
        self.block_sprites = pygame.sprite.RenderUpdates()
        self.horz_portal_sprites = pygame.sprite.RenderUpdates()
        self.vert_portal_sprites = pygame.sprite.RenderUpdates()
        self.gate_sprites = pygame.sprite.RenderUpdates()

        # level_ch = level.CurrentLevel(self.ai_settings,'level1.txt')
        level1 = level001.level(self.ai_settings)
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
                elif layout[x][y]==level.VERTPORTAL:
                    portal = sprite.Sprite(centerPoint, img_list[level.VERTPORTAL-1])
                    self.vert_portal_sprites.add(portal)
                elif layout[x][y]==level.HORZPORTAL:
                    portal = sprite.Sprite(centerPoint, img_list[level.HORZPORTAL-1])
                    self.horz_portal_sprites.add(portal)
                elif layout[x][y]==level.GATE:
                    gate = sprite.Sprite(centerPoint, img_list[level.GATE-1])
                    self.gate_sprites.add(gate)
                elif layout[x][y]==level.PACMAN:
                    self.pacman = pacman.PacMan(self.ai_settings,centerPoint,img_list[level.PACMAN])
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
                    """We also need pellets where the monsters are"""
                    pellet = sprite.Sprite(centerPoint, img_list[level.PELLET])
                    self.small_game_pellets.add(pellet)
                elif layout[x][y]==level.BLUEGHOST:
                    ghost_sprite = ghost.Ghost(centerPoint, img_list[level.BLUEGHOST],img_list[level.SCAREDGHOST])
                    self.ghost_sprites.add(ghost_sprite)
                elif layout[x][y]==level.ORANGEGHOST:
                    ghost_sprite = ghost.Ghost(centerPoint, img_list[level.ORANGEGHOST],img_list[level.SCAREDGHOST])
                    self.ghost_sprites.add(ghost_sprite)
                elif layout[x][y]==level.PINKGHOST:
                    ghost_sprite = ghost.Ghost(centerPoint, img_list[level.PINKGHOST],img_list[level.SCAREDGHOST])
                    self.ghost_sprites.add(ghost_sprite)
        self.pacman_sprites = pygame.sprite.RenderUpdates(self.pacman)
