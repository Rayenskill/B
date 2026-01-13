import pygame

class Box:
    def __init__(self, size, pos, speed, color):
        self.pos = pygame.Vector2(pos)
        self.speed = speed
        self.color = color
        self.rect = pygame.Rect(0, 0, size, size)
        self.rect.center = self.pos

    def update(self):
        pass