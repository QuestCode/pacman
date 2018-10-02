import pygame
import os, sys
from pygame.locals import *

x = os.chdir("../assets")
fullname = os.path.join('../assets', 'images')
fullname = os.path.join(fullname, 'pacman.png')
print(fullname)

try:
    image = pygame.image.load(fullname)
except:
    print ('Cannot load image:', fullname)

print(image.get_rect())
