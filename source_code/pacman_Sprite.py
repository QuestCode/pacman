import sprite
import pygame

class Snake(sprite.Sprite):
    def __init__(self, centerPoint, image):
        """initialize base class"""
        basicSprite.Sprite.__init__(self, centerPoint, image)
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

    def update(self,block_group):
        """Called when the Snake sprit should update itself"""
        self.rect.move_ip(self.xMove,self.yMove)
        """IF we hit a block, don’t move – reverse the movement"""
        if pygame.sprite.spritecollide(self, block_group, False):
            self.rect.move_ip(-self.xMove,-self.yMove)
