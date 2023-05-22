import pygame
#from level0 import *
from setup import *
from importcsv import import_folder

class TILE(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((tileSIZE, tileSIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
    def update(self, shift):
        self.rect.x += shift

class STATICFILE(TILE):
    def __init__(self, size, x, y, surface):
        super().__init__(size,x,y)
        self.image = surface

class COIN(STATICFILE):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load("C:/Users/User/PycharmProjects/pythonProject2/CHARSprites"
                                                       "/Mossy Assets/Mossy Tileset/light.png").convert_alpha())
        offset_y = y + size
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))

class VINE(STATICFILE):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load("C:/Users/User/PycharmProjects/pythonProject2/CHARSprites"
                                                       "/Mossy Assets/Mossy Tileset/vine1.png").convert_alpha())
        offset_y = y + size
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))

class PLANT(STATICFILE):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load("C:/Users/User/PycharmProjects/pythonProject2/CHARSprites"
                                                       "/Mossy Assets/Mossy Tileset/vine5.png").convert_alpha())
        offset_y = y + size
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))

class SPIKES(STATICFILE):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load("C:/Users/User/PycharmProjects/pythonProject2/CHARSprites"
                                                       "/Mossy Assets/Mossy Tileset/plant6.png").convert_alpha())
        offset_y = y + size
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))

class ROCKTALL(STATICFILE):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load("C:/Users/User/PycharmProjects/pythonProject2/CHARSprites"
                                                       "/Mossy Assets/Mossy Tileset/plant3.png").convert_alpha())
        offset_y = y + size
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))

class ROCKSMALL(STATICFILE):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load("C:/Users/User/PycharmProjects/pythonProject2/CHARSprites"
                                                       "/Mossy Assets/Mossy Tileset/plant1.png").convert_alpha())
        offset_y = y + size
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))

'''
class ANIMATEDSPRITES(TILE):
    def __init__(self, size, x, y, path):
        super().__init__(size, x, y)
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        self.frame_index += 0.15
        self.image = self.frames[int(self.frame_index)]'''

