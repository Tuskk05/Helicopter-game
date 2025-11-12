import pygame
from abc import ABC, abstractmethod

class GameSprite(pygame.sprite.Sprite, ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def clone(self):
        pass
