import pygame
from abc import ABC, abstractmethod

class PhysicEntity(ABC):

    def __init__(self, size, pos, speed, direction = pygame.Vector2(), color = 'white'):
        self.size = size * 2
        self.pos = pygame.Vector2(pos)
        self.speed = speed
        self.direction = direction
        self.color = color

    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def render(self):
        pass


class Square(PhysicEntity):
    def __init__(self, size, pos, speed, direction=pygame.Vector2(), color='white'):
        super().__init__(size, pos, speed)
        self.rect = pygame.Rect(0, 0, *self.size)
        self.rect.center = self.pos

    def update(self):
        pass
    
    def create(self):
        pass

    def render(self):
        pass