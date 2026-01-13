from .physicEntities import Square

import pygame

class Box(Square):
    def __init__(self, size, pos, speed, direction = pygame.Vector2(), color = 'white'):
        super().__init__(size, pos, speed)
        

    def update(self):
        pass