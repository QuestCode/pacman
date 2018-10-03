from . import sprite
import pygame

class PacMan(sprite.Sprite):
    def __init__(self,ai_settings,centerPoint, image):
        """initialize base class"""
        # super(PacMan,centerPoint,image)
        sprite.Sprite.__init__(self, centerPoint, image)
        self.ai_settings = ai_settings
        """Initialize the number of pellets eaten"""
        self.pellets = 0
        """Set the number of Pixels to move each time"""
        self.x_dist = 3
        self.y_dist = 3
        """Initialize how much we are moving"""
        self.xMove = 0
        self.yMove = 0

    def MoveKeyDown(self, key):
        """This function sets the xMove or yMove variables that will
        then move the snake when update() function is called. The
        xMove and yMove values will be returned to normal when this
        keys MoveKeyUp function is called."""

        if (key == pygame.K_RIGHT):
            self.xMove += self.x_dist
        elif (key == pygame.K_LEFT):
            self.xMove += -self.x_dist
        elif (key == pygame.K_UP):
            self.yMove += -self.y_dist
        elif (key == pygame.K_DOWN):
            self.yMove += self.y_dist

    def MoveKeyUp(self, key):
        """This function resets the xMove or yMove variables that will
        then move the snake when update() function is called. The
        xMove and yMove values will be returned to normal when this
        keys MoveKeyUp function is called."""

        if (key == pygame.K_RIGHT):
            self.xMove += -self.x_dist
        elif (key == pygame.K_LEFT):
            self.xMove += self.x_dist
        elif (key == pygame.K_UP):
            self.yMove += self.y_dist
        elif (key == pygame.K_DOWN):
            self.yMove += -self.y_dist

    def update(self,block_group,pellet_group,power_pellet_group,ghost_group):
        """Called when the Snake sprit should update itself"""

        if (self.xMove==0)and(self.yMove==0):
            """If we arn'te moveing just get out of here"""
            return
        """All right we must be moving!"""
        self.rect.move_ip(self.xMove,self.yMove)

        if pygame.sprite.spritecollideany(self, block_group):
            """IF we hit a block, don't move - reverse the movement"""
            self.rect.move_ip(-self.xMove,-self.yMove)

        """Check to see if we hit a Monster!"""
        lstGhost = pygame.sprite.spritecollide(self, ghost_group, False)
        if lstGhost:
            """Allright we have hit a Monster!"""
            self.ghostCollide(lstGhost)
        else:
            """Alright we did move, so check collisions"""
            """Check for a snake collision/pellet collision"""
            lstCols = pygame.sprite.spritecollide(self, pellet_group, True)
            pwrLstCol = pygame.sprite.spritecollide(self, power_pellet_group, True)
            if lstCols:
                """Update the amount of pellets eaten"""
                self.pellets += 10*len(lstCols)
                self.ai_settings.play_sound('chomp.wav')
                print(self.pellets)
                """if we didn't hit a pellet, maybe we hit a power pellet?"""
            elif pwrLstCol:
                """We have collided with a power pellet! Time to become Super!"""
                self.superState = True
                self.ai_settings.play_sound('chump.wav')
                # pygame.event.post(pygame.event.Event(SUPER_STATE_START,{}))
                # """Start a timer to figure out when the super state ends"""
                # pygame.time.set_timer(SUPER_STATE_OVER,0)
                # pygame.time.set_timer(SUPER_STATE_OVER,3000)

    def ghostCollide(self, lstGhost):
        """This Function is called when the snake collides with the a Monster
        lstMonstes is a list of Monster sprites that it has hit."""

        if (len(lstGhost)<=0):
            """If the list is empty, just get out of here"""
            return

        """Loop through the ghosts and see what should happen"""
        for ghost in lstGhost:
            if (ghost.scared):
                ghost.Eaten()
            # else:
            #     """Looks like we're dead"""
            #     pygame.event.post(pygame.event.Event(SNAKE_EATEN,{}))
