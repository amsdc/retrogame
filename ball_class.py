import pygame
from pygame.locals import (K_UP,KEYDOWN,K_DOWN,K_LEFT,K_RIGHT)

class Ball():
    def __init__(self):
        super().__init__()
        self.size = 76
        self.surf = pygame.Surface((76,76))
        self.surf.fill((245,27,2))
        self.rect = self.surf.get_rect()



