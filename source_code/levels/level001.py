from .levelbase import Level

class level(Level):
    """Level 1 of the PyMan Game"""

    def __init__(self,ai_settings):
        self.BLOCK = 1
        self.PACMAN = 2
        self.PELLET = 0
        self.POWER_PELLET = 3
        self.REDGHOST = 4
        self.BLUEGHOST = 5
        self.ORANGEGHOST = 6
        self.PINKGHOST = 7
        self.SCAREDGHOST = 8
        self.VERTPORTAL = 10
        self.HORZPORTAL = 11
        self.GATE = 12
        self.ai_settings = ai_settings

    def getLayout(self):
        return [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
        [9, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 9],\
        [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,0, 0, 0, 0, 0, 0, 0, 0, 10, 9],\
        [9, 1, 3, 1, 1, 0, 1, 1, 1, 0, 1 ,0, 1, 1, 1, 0, 1, 1, 3, 1, 9],\
        [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
        [9, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1 ,1, 1, 0, 1, 0, 1, 1, 0, 1, 9],\
        [9, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1 ,0, 0, 0, 1, 0, 0, 0, 0, 1, 9],\
        [9, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 9],\
        [9, 1, 1, 1, 1, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 1, 1, 1, 1, 9],\
        [9, 1, 1, 1, 1, 0, 1, 0, 1, 1, 12, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\
        [9, 1, 0, 0, 0, 0, 0, 0, 1, 5, 6, 7, 1, 0, 0, 0, 0, 0, 0, 1, 9],\
        [9, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\
        [9, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 9],\
        [9, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\
        [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
        [9, 1, 3, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 3, 1, 9],\
        [9, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 1, 9],\
        [9, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 9],\
        [9, 10, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 9],\
        [9, 1, 3, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 3, 1, 9],\
        [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
        [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1, 9]]

    def getSprites(self):
        block, rect = self.ai_settings.red_block_image
        vert_portal, rect = self.ai_settings.vert_portal_image
        horz_portal, rect = self.ai_settings.horz_portal_image
        pellet, rect = self.ai_settings.pellet_image
        pacman, rect = self.ai_settings.pacman_right_image
        power_pellet, rect = self.ai_settings.power_pellet_image
        red_ghost, rect = self.ai_settings.red_ghost_image
        blue_ghost, rect = self.ai_settings.blue_ghost_image
        orange_ghost, rect = self.ai_settings.orange_ghost_image
        pink_ghost, rect = self.ai_settings.pink_ghost_image
        scared_ghost, rect = self.ai_settings.scared_ghost_image
        gate, rect = self.ai_settings.gate_image
        return [pellet,block,pacman,power_pellet,red_ghost,blue_ghost,
                orange_ghost,pink_ghost,scared_ghost,vert_portal,horz_portal,gate]
